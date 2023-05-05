from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from les_classes.class_produit import *


class Ui_SupprimerProduit(object):
    def setupUi(self, SupprimerProduit):
        SupprimerProduit.setObjectName("SupprimerProduit")
        SupprimerProduit.resize(800, 412)
        SupprimerProduit.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        SupprimerProduit.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(SupprimerProduit)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(130, 80, 541, 261))
        self.widget_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(170, 200, 191, 41))
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
        self.label_6.setGeometry(QtCore.QRect(140, 20, 301, 51))
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
        self.pushButton_2.clicked.connect(lambda:SupprimerProduit.close())
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(159, 130, 291, 35))
        self.comboBox.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SupprimerProduit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SupprimerProduit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SupprimerProduit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SupprimerProduit)
        self.statusbar.setObjectName("statusbar")
        SupprimerProduit.setStatusBar(self.statusbar)

        self.retranslateUi(SupprimerProduit)
        QtCore.QMetaObject.connectSlotsByName(SupprimerProduit)

    def retranslateUi(self, SupprimerProduit):
        _translate = QtCore.QCoreApplication.translate
        SupprimerProduit.setWindowTitle(_translate("SupprimerProduit", "SupprimerProduit"))
        self.pushButton.setText(_translate("SupprimerProduit", "Supprimer"))
        self.label_6.setText(_translate("SupprimerProduit", "Supprimer Produit"))
        self.label.setText(_translate("SupprimerProduit", "ID/PRODUIT"))


        # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa")

        # Ajout des éléments dans la combobox à partir de la base de données
        cursor = self.conn.cursor()
        cursor.execute("SELECT idp FROM produits")
        resultats = cursor.fetchall()
        for resultat in resultats:
                self.comboBox.addItem(str(resultat[0]))
        self.conn.close()

        self.pushButton.clicked.connect(self.supprimer)
        self.pushButton.clicked.connect(lambda:SupprimerProduit.close())
        ##########
    def supprimer(self):   
        id = self.comboBox.currentText()
        Produits().supprimer(id)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_SupprimerProduit()
     SupprimerProduit= QtWidgets.QMainWindow()
     ui.setupUi(SupprimerProduit)
     SupprimerProduit.show()
     sys.exit(app.exec_())
