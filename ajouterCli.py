from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QDate
import datetime
from les_classes.class_Client import *

class Ui_AjouterCli(object):
    def setupUi(self, AjouterCli):
        AjouterCli.setObjectName("AjouterCli")
        AjouterCli.resize(1033, 880)
        AjouterCli.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AjouterCli.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(AjouterCli)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(210, 10, 541, 601))
        self.widget_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(79, 150, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(79, 210, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(170, 520, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:2, y1:1, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1   #CFE9C2);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:2, y1:1, x2:1, y2:0, stop:0 #CFE9C2, stop:1 rgba(11, 131, 120, 219));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0   #CFE9C2, stop:1 rgba(11, 131, 120, 219));\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 10, 50, 28))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-fermer-la-fenêtre-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:AjouterCli.close())
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(79, 270, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(79, 330, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(79, 390, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.dateEdit = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit.setGeometry(QtCore.QRect(79, 450, 371, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, 440, 141, 16))
        self.label.setStyleSheet("color: rgb(148, 148, 148);")
        self.label.setObjectName("label")
        AjouterCli.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AjouterCli)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 26))
        self.menubar.setObjectName("menubar")
        AjouterCli.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AjouterCli)
        self.statusbar.setObjectName("statusbar")
        AjouterCli.setStatusBar(self.statusbar)

        self.retranslateUi(AjouterCli)
        QtCore.QMetaObject.connectSlotsByName(AjouterCli)

        ####
        self.pushButton.clicked.connect(self.ajouter)
        self.pushButton.clicked.connect(lambda:AjouterCli.close())
        ####
        #############
    def ajouter(self):
        print("hello")
        Edt1 = self.lineEdit_2.text()
        Edt2 = self.lineEdit_3.text()
        Edt3 = self.lineEdit_4.text()
        Edt4 = self.lineEdit_5.text()
        Edt5 = self.lineEdit_6.text()
        qdate = self.dateEdit.date()  # récupérer la date sous forme d'objet QDate
        date = datetime.date(qdate.year(), qdate.month(), qdate.day())  # convertir en datetime.date
        client = Client(Edt1, Edt2, Edt3, Edt4, Edt5, date)
        ajou = client.Ajouter()
        
        #############


    def retranslateUi(self, AjouterCli):
        _translate = QtCore.QCoreApplication.translate
        AjouterCli.setWindowTitle(_translate("AjouterCli", "AjouterCli"))
        self.lineEdit_2.setPlaceholderText(_translate("AjouterCli", "PRENOM/CLIENT"))
        self.lineEdit_3.setPlaceholderText(_translate("AjouterCli", "NOM CLIENT"))
        self.pushButton.setText(_translate("AjouterCli", "Ajouter"))
        self.label_6.setText(_translate("AjouterCli", "Ajouter Client"))
        self.lineEdit_4.setPlaceholderText(_translate("AjouterCli", "TELE"))
        self.lineEdit_5.setPlaceholderText(_translate("AjouterCli", "EMAIL"))
        self.lineEdit_6.setPlaceholderText(_translate("AjouterCli", "ADRESSE"))
        self.label.setText(_translate("AjouterCli", "DATE NAISSANCE"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_AjouterCli()
     AjouterCli = QtWidgets.QMainWindow()
     ui.setupUi(AjouterCli)
     AjouterCli.show()
     sys.exit(app.exec_())
