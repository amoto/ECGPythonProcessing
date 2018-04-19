from pyqtgraph.Qt import QtGui,QtCore
import pyqtgraph as pg
import numpy as np
import serial
from pyqtgraph.ptime import time

class Grafica:
    
    def __init__(self,puerto,plotWidget):
        self.puerto = puerto
        self.plotWidget = plotWidget
        self.app = QtGui.QApplication([])
        
    def update(self):
        global curva,data,puerto1
        try:
            line = puerto1.readline().decode().strip()
            data.append(float(line))
            xdata = np.array(data,dtype="float64")
            curva.setData(xdata)
            self.app.processEvents()
        except Exception as e:
            print(e)
        
    def iniciar(self):
        global curva,data,puerto1
        curva = self.plotWidget.getPlotItem()
        data = [0]
        puerto1 = serial.Serial(self.puerto,9600)
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(1000)
        QtGui.QApplication.instance().exec_()


