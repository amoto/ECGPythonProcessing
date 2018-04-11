
from capturador import Capturador

def main():
    puerto = input("Ingrese el puerto por donde va a leer los datos: ")
    archivo = input("Ingrese el nombre del archivo donde se guardarán los datos: ")
    c = Capturador(puerto, archivo)
    c.capturar()
    
if __name__ == '__main__':
    main()
