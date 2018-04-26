import serial
import paho.mqtt.publish as publish
class Capturador:
    
    def __init__(self,puerto,archivo):
        self.puerto = serial.Serial(puerto,9600)
        self.lecturas = []
        self.archivo = archivo
        
    def capturar(self):
        while(True):
            try:
                value = self.puerto.readline()
                value = float(value.decode().strip())
                if(len(self.lecturas) == 512):
                    publish.single("paciente/1",str(self.lecturas),hostname="10.3.0.6")
                    print(self.lecturas)
                    f = open(self.archivo,'a')
                    f.write(str(self.lecturas)+'\n')
                    self.lecturas = []
                else:
                    self.lecturas.append(value)
            except Exception as e:
                print(e)
