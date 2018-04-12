import hashlib
import csv
from login.error import Error
class Persistence:
    def __init__(self):
        try:
            f=open('users.csv','r')
        except:
            f=open('users.csv','w')

        f.close()
    def __consultarUsuario(self,username):
        f=open('users.csv','r')
        datos=csv.reader(f)
        user=None
        for line in datos:
            if username==line[0]:
                user=line
                break
        f.close()
        return user

    def guardarUsuario(self,username,password):
        if(self.__consultarUsuario(username)==None):
            f=open('users.csv','a+')
            datos=csv.writer(f)
            datos.writerow([username,hashlib.sha256(password.encode()).hexdigest()])
            f.close()
        else:
            raise Error('El usuario ya existe')

    def validarUsuario(self,username,password):
        user=self.__consultarUsuario(username)
        if(user!=None and user[1]==hashlib.sha256(password.encode()).hexdigest()):
            return True
        elif (user==None):
            raise Error('Usuario no existente')
        else:
            raise Error('Contraseña incorrecta')