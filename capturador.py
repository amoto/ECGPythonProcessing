import serial

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
                    print(self.lecturas)
                    f = open(self.archivo,'a')
                    f.write(str(self.lecturas))
                    self.lecturas = []
                else:
                    self.lecturas.append(value)
            except Exception as e:
                print(e)
