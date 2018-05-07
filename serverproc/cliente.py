import paho.mqtt.client as mqttClient
import time
class Cliente:
    def __init__(self,broker,port,func):
        self.broker=broker
        self.port=port
        self.client = mqttClient.Client("Servidor")
        self.client.on_message = func
        self.client.connect(self.broker, port=port)
        self.client.loop_start()
        self.client.subscribe("paciente/1")
        while True:
           time.sleep(2)
