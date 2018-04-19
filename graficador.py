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
from pyqtgraph.ptime import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 371, 51))
        self.label.setObjectName("label")
        self.lineEditPuerto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPuerto.setGeometry(QtCore.QRect(360, 180, 271, 31))
        self.lineEditPuerto.setObjectName("lineEditPuerto")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 120, 241, 31))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.graficar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Bienvenido a ECGPythonProcessing</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Ingrese el puerto por donde se leeran los datos:"))
        self.pushButton.setText(_translate("MainWindow", "Iniciar"))
        
    def graficar(self):
        mensaje = QtWidgets.QMessageBox()
        if(len(self.lineEditPuerto.text()) == 0):
            mensaje.about(mensaje,'Error',"El puerto no puede quedar vacio")
        else:
            self.iniciar()
            
            
         
    def update(self):
        global curva,data,puerto1
        print("Entro al update")
        try:
            line = puerto1.readline().decode().strip()
            data.append(float(line))
            xdata = np.array(data,dtype="float64")
            curva.setData(xdata)
            QtGui.QApplication.instance().processEvents()
        except Exception as e:
            print(e)
        
    def iniciar(self):
        global curva,data,puerto1
        curva = self.graphicsView.getPlotItem().plot()
        data = [0]
        puerto1 = serial.Serial(self.lineEditPuerto.text(),9600)
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(1000)
        print("Antes")
        QtGui.QApplication.instance().exec_()
        print("Despues")
        
            

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

