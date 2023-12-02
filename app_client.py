
import json
import os
import time
from datetime import datetime, timezone

import django
import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT

# inicialização do django para esse arquivo unico
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

formatted_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

CounterFitConnection.init('localhost', 5000)
id = '0cfa84eb-47c0-4bcf-aa67-f9add0f5f0fa'
client_name = id + 'fazenda_client'
client_telemetry_topic = id + '/telemetry'
mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')
mqtt_client.loop_start()
print('MQTT connected')

sensor1 = DHT("11", 5)
sensor2 = DHT("11", 5)


# loop
while True:
    try:
        _, temperature1 = sensor1.read()
        _, temperature2 = sensor2.read()

        # Publicar dados do sensor no MQTT
        mqtt_client.publish(client_telemetry_topic, payload=json.dumps(
            {'temperature1': temperature1, 'temperature2': temperature2}))

        # salvamento no banco de dados
        try:
            from products.models import Temperatura

            Temperatura.objects.create(
                temperatura=temperature1,
                fk_sensor_id=1,
                data=datetime.now(timezone.utc)
            )
            Temperatura.objects.create(
                temperatura=temperature2,
                fk_sensor_id=2,
                data=datetime.now(timezone.utc)
            )
        except Exception as e:
            print(f"Erro desconhecido ao salvar no banco de dados: {e}")

        print(f'Temperature Sensor 1: {temperature1}°C ')
        print(f'Temperature Sensor 2: {temperature2}°C \n')

        time.sleep(2)

    except Exception as e:
        print(f"Erro na captação: {e}")
