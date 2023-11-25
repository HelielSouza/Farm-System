
import json
import time
from datetime import datetime

import paho.mqtt.client as mqtt
import pymssql
from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT

db_config = {
    'host': 'regulus.cotuca.unicamp.br',
    'user': 'BD22555',
    'password': 'BD22555',
    'database': 'BD22555',
}

formatted_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def insert_into_sql_server(temperature, fk_sensor_id):
    connection = pymssql.connect(**db_config)
    cursor = connection.cursor()

    # Exemplo de inserção, ajuste de acordo com sua tabela e esquema
    query = (
        f"INSERT INTO products_testetemperatura "
        f"(temperatura, fk_sensor_id, data) "
        f"VALUES ({temperature}, {fk_sensor_id}, '{formatted_datetime}')"
    )
    cursor.execute(query)

    connection.commit()
    connection.close()


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

        insert_into_sql_server(temperature1, 1)
        insert_into_sql_server(temperature2, 2)

        print(f'Temperature Sensor 1: {temperature1}°C ')
        print(f'Temperature Sensor 2: {temperature2}°C ')

        time.sleep(3)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
