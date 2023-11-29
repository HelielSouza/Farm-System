
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


try:
    from products.models import Sensor
    sensor = Sensor.objects.get(pk=1)
    print(sensor)
except Sensor.DoesNotExist:
    print("Sensor not found.")
except Exception as e:
    print(f"An error occurred: {e}")
