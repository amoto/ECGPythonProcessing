from mqtt.cliente import Cliente
from serverproc.procesamiento import Procesador
import threading
def main():
    c=Cliente("127.0.0.1",1883,proc)
def proc(client,userdata,message):
    print(message.topic)
    print(message.payload.decode())
    t=threading.Thread(target=func,args=(message.topic,message.payload.decode(),))
    t.start()
def func(topic,message):
    processor = Procesador(topic, message)
if __name__ == '__main__':
    main()