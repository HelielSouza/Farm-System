import json

import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection

# from counterfit_shims_seeed_python_dht import DHT

CounterFitConnection.init('localhost', 5000)
# Conexao do counterfit na porta 5000

# estabelece a conexao com o broker
id = '0cfa84eb-47c0-4bcf-aa67-f9add0f5f0fa'
# atribui um identificador único à variável id.
client_name = id + 'fazenda_client'
# cria um nome único para o cliente MQTT ao
# concatenar o id com a string 'fazenda_client'.
client_telemetry_topic = id + '/telemetry'
# define o tópico de telemetria para o cliente MQTT,
# concatenando o id com a string '/telemetry'.
mqtt_client = mqtt.Client(client_name)
# cria uma instância do cliente MQTT com o
#  nome do cliente especificado.
mqtt_client.connect('test.mosquitto.org')
# estabelece a conexão do cliente MQTT com
# o servidor MQTT hospedado no mosquitto

# confirma se o MQTT ta conectado
mqtt_client.loop_start()
print('MQTT connected')

# essa função handle_telemetry processa e imprime mensagens
# recebidas pelo cliente MQTT em um tópico específico.


def handle_telemetry(client, userdata, message):
    print('Received message on topic {}: {}'.format(
        message.topic, message.payload))
    try:
        payload = json.loads(message.payload.decode())
        print('Message decoded: ', payload)
    except json.JSONDecodeError as e:
        print('Error decoding JSON:', e)


# inscreve o cliente MQTT no tópico de telemetria e
# define a função de tratamento para as mensagens recebidas.
mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry
