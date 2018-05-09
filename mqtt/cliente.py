import paho.mqtt.client as mqttClient
import time
class Cliente:
    def __init__(self,broker,port,func,topic="paciente/1",id="Servidor"):
        self.broker=broker
        self.port=port
        print("antes de crear el cliente")
        self.client = mqttClient.Client(id)
        self.client.on_message = func
        print("conectar")
        self.client.connect(self.broker, port=port)
        print("antes de loop start")
        self.client.loop_start()
        print("antes de suscribir a",topic)
        self.client.subscribe(topic)
        while True:
           time.sleep(2)
