# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from login.login import Login

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 396)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 431, 231))
        self.tabs.setObjectName("tabs")
        self.loginTab = QtWidgets.QWidget()
        self.loginTab.setObjectName("loginTab")
        self.loginLabel = QtWidgets.QLabel(self.loginTab)
        self.loginLabel.setGeometry(QtCore.QRect(170, 20, 91, 17))
        self.loginLabel.setObjectName("loginLabel")
        self.loginButton = QtWidgets.QPushButton(self.loginTab)
        self.loginButton.setGeometry(QtCore.QRect(170, 140, 88, 29))
        self.loginButton.setObjectName("loginButton")
        self.userNameLabel = QtWidgets.QLabel(self.loginTab)
        self.userNameLabel.setGeometry(QtCore.QRect(15, 60, 121, 20))
        self.userNameLabel.setObjectName("userNameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.loginTab)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 100, 121, 20))
        self.passwordLabel.setObjectName("passwordLabel")
        self.userNameEdit = QtWidgets.QLineEdit(self.loginTab)
        self.userNameEdit.setGeometry(QtCore.QRect(140, 60, 231, 29))
        self.userNameEdit.setObjectName("userNameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.loginTab)
        self.passwordEdit.setGeometry(QtCore.QRect(140, 90, 231, 29))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.tabs.addTab(self.loginTab, "")
        self.registerTab = QtWidgets.QWidget()
        self.registerTab.setObjectName("registerTab")
        self.passwordLabelR = QtWidgets.QLabel(self.registerTab)
        self.passwordLabelR.setGeometry(QtCore.QRect(20, 90, 121, 20))
        self.passwordLabelR.setObjectName("passwordLabelR")
        self.registerLabel = QtWidgets.QLabel(self.registerTab)
        self.registerLabel.setGeometry(QtCore.QRect(190, 10, 51, 17))
        self.registerLabel.setObjectName("registerLabel")
        self.userNameLabelR = QtWidgets.QLabel(self.registerTab)
        self.userNameLabelR.setGeometry(QtCore.QRect(15, 50, 121, 20))
        self.userNameLabelR.setObjectName("userNameLabelR")
        self.registerButton = QtWidgets.QPushButton(self.registerTab)
        self.registerButton.setGeometry(QtCore.QRect(170, 150, 88, 29))
        self.registerButton.setObjectName("registerButton")
        self.confirmLabelR = QtWidgets.QLabel(self.registerTab)
        self.confirmLabelR.setGeometry(QtCore.QRect(10, 120, 131, 20))
        self.confirmLabelR.setObjectName("confirmLabelR")
        self.userNameEditR = QtWidgets.QLineEdit(self.registerTab)
        self.userNameEditR.setGeometry(QtCore.QRect(150, 40, 231, 29))
        self.userNameEditR.setObjectName("userNameEditR")
        self.passwordEditR = QtWidgets.QLineEdit(self.registerTab)
        self.passwordEditR.setGeometry(QtCore.QRect(150, 80, 231, 29))
        self.passwordEditR.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEditR.setObjectName("passwordEditR")
        self.confirmEditR = QtWidgets.QLineEdit(self.registerTab)
        self.confirmEditR.setGeometry(QtCore.QRect(150, 110, 231, 29))
        self.confirmEditR.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmEditR.setObjectName("confirmEditR")
        self.tabs.addTab(self.registerTab, "")
        self.img = QtWidgets.QFrame(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(9, 239, 421, 111))
        self.img.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(hearthecg.jpg);")
        self.img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img.setObjectName("img")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.setupLogic()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio de Sesión y Registro"))
        self.loginLabel.setText(_translate("MainWindow", "Inicio de Sesión"))
        self.loginButton.setText(_translate("MainWindow", "Iniciar Sesión"))
        self.userNameLabel.setText(_translate("MainWindow", "Nombre de Usuario"))
        self.passwordLabel.setText(_translate("MainWindow", "Contraseña"))
        self.tabs.setTabText(self.tabs.indexOf(self.loginTab), _translate("MainWindow", "Iniciar Sesión"))
        self.passwordLabelR.setText(_translate("MainWindow", "Contraseña"))
        self.registerLabel.setText(_translate("MainWindow", "Registro"))
        self.userNameLabelR.setText(_translate("MainWindow", "Nombre de Usuario"))
        self.registerButton.setText(_translate("MainWindow", "Registrar"))
        self.confirmLabelR.setText(_translate("MainWindow", "Confirmar Contraseña"))
        self.tabs.setTabText(self.tabs.indexOf(self.registerTab), _translate("MainWindow", "Registro"))
    def setupLogic(self):
        self.logic=Login()
        self.loginButton.clicked.connect(self.loginClick)
        self.registerButton.clicked.connect(self.registerClick)
    def loginClick(self):
        ans=self.logic.login(self.userNameEdit.text(),self.passwordEdit.text())
        about_box = QtWidgets.QMessageBox()
        if(ans[1]):
            about_box.about(about_box, 'Inicio de sesión exitoso', ans[0])
        else:
            about_box.about(about_box, 'Inicio de sesión fallido', ans[0])
    def registerClick(self):
        ans=self.logic.crearUsuario(self.userNameEditR.text().strip(),self.passwordEditR.text().strip(),self.confirmEditR.text().strip())
        about_box = QtWidgets.QMessageBox()
        if(ans[1]):
            about_box.about(about_box, 'Registro exitoso', ans[0])
        else:
            about_box.about(about_box, 'Registro fallido', ans[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

