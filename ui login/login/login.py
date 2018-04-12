
from login.persistence import Persistence
class Login:

    def __init__(self):
        self.persistence=Persistence()

    def __validar(self,passwd):
        if len(passwd)>=5 and passwd.isalnum():
            return True
        return False

    def crearUsuario(self,username,passwd,confirm):
        if not(self.__validar(passwd)):
            return 'Contraseña invalida.',False
        elif passwd!=confirm:
            return 'Las contraseñas no son iguales',False
        try:
            self.persistence.guardarUsuario(username,passwd)
            return 'Usuario creado exitosamente',True
        except Exception as err:
            return str(err),False

    def login(self,username,passwd):
        try:
            self.persistence.validarUsuario(username,passwd)
            return 'Bienvenido al sistema',True
        except Exception as err:
            return str(err),False

    def menu(self):
        print("Inicio se Sesión\n1. Crear cuenta\n2. Iniciar sesion\n3. Salir")
        res=int(input("Ingrese la opción que desea usar: "))
        sesion=False
        while(res<1 or res >3):
            res=int(input("-------->Seleccion invalida<--------\nIngrese la opción que desea usar: "))
        if(res==1):
            self.crearUsuario()
        elif(res==2):
            sesion=self.login()
        print("\n"*3)
        return res,sesion

    def main(self):
        seleccion=self.menu()
        while(seleccion[0]!=3 and not(seleccion[1])):
            seleccion=self.menu()
        if(seleccion[1]):
            print('Bienvenido al sistema')