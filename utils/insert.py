from datetime import datetime

import pymssql

from products.models import TESTETemperatura

formatted_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def insert_into_sql_server(temperature, fk_sensor_id):

    db_config = {
        'host': 'regulus.cotuca.unicamp.br',
        'user': 'BD22555',
        'password': 'BD22555',
        'database': 'BD22555',
    }

    connection = pymssql.connect(**db_config)
    cursor = connection.cursor()

    query = (
        f"INSERT INTO products_testetemperatura "
        f"(temperatura, fk_sensor_id, data) "
        f"VALUES ({temperature}, {fk_sensor_id}, '{formatted_datetime}')"
    )
    cursor.execute(query)

    connection.commit()
    connection.close()

    last_instance = TESTETemperatura.objects.latest('id')
    # Chama o método save() para acionar o sinal
    last_instance.save()
