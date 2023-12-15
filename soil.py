import os
import time
from datetime import datetime, timezone

import django
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


formatted_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

CounterFitConnection.init('127.0.0.1', 5000)


adc = ADC()
relay = GroveRelay(5)

while True:
    soil_moisture = adc.read(0)
    print("Soil moisture:", soil_moisture)

    try:
        from products.models import UmidadeValores

        UmidadeValores.objects.create(
            timestamp=datetime.now(timezone.utc),
            umidade=soil_moisture,
        )
        if soil_moisture > 450:
            print("Soil Moisture is too low, turning relay on.")

            relay.on()
        else:
            print("Soil Moisture is ok, turning relay off.")
            relay.off()

    except Exception as e:
        print(f"Erro desconhecido ao salvar no banco de dados: {e}")

    time.sleep(10)
