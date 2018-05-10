# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficadorPuerto.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtGui,QtCore
import pyqtgraph as pg
import numpy as np
import serial
import paho.mqtt.publish as publish
import threading
from mqtt.cliente import Cliente
from pyqtgraph.ptime import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        print('setup g')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 411, 51))
        self.label.setObjectName("label")
        self.lineEditPuerto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPuerto.setGeometry(QtCore.QRect(360, 180, 271, 31))
        self.lineEditPuerto.setObjectName("lineEditPuerto")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 120, 291, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 310, 961, 481))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hrlabel = QtWidgets.QLabel(self.centralwidget)
        self.hrlabel.setGeometry(QtCore.QRect(795, 40, 91, 20))
        self.hrlabel.setObjectName("hrlabel")
        self.hrresult = QtWidgets.QLabel(self.centralwidget)
        self.hrresult.setGeometry(QtCore.QRect(900, 40, 56, 17))
        #self.hrresult.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        #                            "border-color: rgb(0, 0, 0);")
        self.hrresult.setObjectName("hrresult")
        self.pnn50result = QtWidgets.QLabel(self.centralwidget)
        self.pnn50result.setGeometry(QtCore.QRect(900, 60, 56, 17))
        #self.pnn50result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        #                               "border-color: rgb(0, 0, 0);")
        self.pnn50result.setObjectName("pnn50result")
        self.pnn50label = QtWidgets.QLabel(self.centralwidget)
        self.pnn50label.setGeometry(QtCore.QRect(795, 60, 91, 20))
        self.pnn50label.setObjectName("pnn50label")
        self.pnn20result = QtWidgets.QLabel(self.centralwidget)
        self.pnn20result.setGeometry(QtCore.QRect(900, 80, 56, 17))
        #self.pnn20result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        #                              "border-color: rgb(0, 0, 0);")
        self.pnn20result.setObjectName("pnn20result")
        self.pnn20label = QtWidgets.QLabel(self.centralwidget)
        self.pnn20label.setGeometry(QtCore.QRect(795, 80, 91, 20))
        self.pnn20label.setObjectName("pnn20label")
        self.rmssdresult = QtWidgets.QLabel(self.centralwidget)
        self.rmssdresult.setGeometry(QtCore.QRect(900, 100, 56, 17))
        #self.rmssdresult.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        #                              "border-color: rgb(0, 0, 0);")
        self.rmssdresult.setObjectName("rmssdresult")
        self.rmssdlabel = QtWidgets.QLabel(self.centralwidget)
        self.rmssdlabel.setGeometry(QtCore.QRect(795, 100, 91, 20))
        self.rmssdlabel.setObjectName("rmssdlabel")

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.graficar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Bienvenido a ECGPythonProcessing</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Ingrese el puerto por donde se leeran los datos:"))
        self.pushButton.setText(_translate("MainWindow", "Iniciar"))
        self.hrlabel.setText(_translate("MainWindow", "Ritmo cardíaco"))
        self.hrresult.setText(_translate("MainWindow", "0"))
        self.pnn50result.setText(_translate("MainWindow", "0"))
        self.pnn50label.setText(_translate("MainWindow", "pnn50"))
        self.pnn20result.setText(_translate("MainWindow", "0"))
        self.pnn20label.setText(_translate("MainWindow", "pnn20"))
        self.rmssdresult.setText(_translate("MainWindow", "0"))
        self.rmssdlabel.setText(_translate("MainWindow", "rmssd"))
        self.chr = 0
        self.cpnn50 = 0
        self.cpnn20 = 0
        self.crmssd = 0
        t1=threading.Thread(target=self.subscribe,args=(self.chr,"paciente/1/hr",self.prochr,"hr"))
        t2 = threading.Thread(target=self.subscribe, args=(self.cpnn50, "paciente/1/pnn50", self.procpnn50,"pnn50"))
        t3 = threading.Thread(target=self.subscribe, args=(self.cpnn20, "paciente/1/pnn20", self.procpnn20,"pnn20"))
        t4 = threading.Thread(target=self.subscribe, args=(self.crmssd, "paciente/1/rmssd", self.procrmssd,"rmssd"))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
    def subscribe(self,var,topic,callback,id):
        var = Cliente("127.0.0.1", 1883, callback, topic=topic,id=id)
    def prochr(self ,client, userdata, message):
        self.hrresult.setText(message.payload.decode())
    def procpnn20(self ,client, userdata, message):
        self.pnn20result.setText(message.payload.decode())
    def procpnn50(self ,client, userdata, message):
        self.pnn50result.setText(message.payload.decode())
    def procrmssd(self ,client, userdata, message):
        self.rmssdresult.setText(message.payload.decode())
    def graficar(self):
        print('holi')
        mensaje = QtWidgets.QMessageBox()
        if(len(self.lineEditPuerto.text()) == 0):
            mensaje.about(mensaje,'Error',"El puerto no puede quedar vacio")
        else:
            self.iniciar()
            
            
         
    def update(self,valor):
        global curva,data
        try:
            data.append(float(valor))

            xdata = np.array(data,dtype="float64")
            curva.setData(xdata)
            #QtGui.QApplication.instance().processEvents()
            if(len(data)>2048):
                data.pop(0)
                #print(data)
        except Exception as e:
            print(e)
        
    def iniciar(self):
        global curva,data
        about_box = QtWidgets.QMessageBox()
        try:
            self.hilo1 = Hilo1(self.lineEditPuerto.text(),self.update,parent=self.MainWindow)
            data = [0 for i in range(2048)]
            self.lecturas=[]
            curva = self.graphicsView.getPlotItem().plot()
            self.hilo1.start()
            '''timer = QtCore.QTimer(self.graphicsView)
            timer.timeout.connect(self.update)
            timer.start(10)'''
            QtGui.QApplication.instance().allWidgets()
        except Exception as e:
            about_box.about(about_box, 'El puerto especificado no funciona', 'No se puede conectar al puerto '+self.lineEditPuerto.text())
        
        
        
        
        
class Hilo1(QtCore.QThread):
    sigf = QtCore.pyqtSignal(str)
    
    
    def __init__(self,puerto,callback,parent=None):
        super(Hilo1,self).__init__(parent)
        self.callback = callback
        self.puerto = serial.Serial(puerto,9600)
        #self.sigf.connect(callback)
        self.lecturas=[]

    def publicar(self,arreglo):
        print("publicando")
        print(arreglo)
        publish.single("paciente/1", arreglo, hostname="127.0.0.1")
        print("publicado")

        
    def run(self):
        while(True):
            try:
                valor = self.puerto.readline()
                valor = valor.decode().strip()
                self.callback(valor)
                self.lecturas.append(float(valor))
                if (len(self.lecturas) == 512):
                    try:
                        t = threading.Thread(target=self.publicar, args=(str(self.lecturas),))
                        t.start()
                        self.lecturas = []
                    except Exception as e:
                        print(e)
                        self.lecturas = []
                #self.sigf.emit(valor)
            except Exception as e:
                print(e)
        
            

from pyqtgraph import PlotWidget

def main(MainWindow):
    import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #sys.exit(app.exec_())
#if __name__ == "__main__":
#    main()

