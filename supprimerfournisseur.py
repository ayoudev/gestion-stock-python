from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from les_classes.class_Fournissour import *

class Ui_SupprimerFournisseur(object):
    def setupUi(self, SupprimerFournisseur):
        SupprimerFournisseur.setObjectName("SupprimerFournisseur")
        SupprimerFournisseur.resize(800, 600)
        SupprimerFournisseur.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        SupprimerFournisseur.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(SupprimerFournisseur)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(150, 60, 551, 281))
        self.widget_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 191, 41))
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
        self.label_6.setGeometry(QtCore.QRect(100, 20, 351, 51))
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
        self.pushButton_2.clicked.connect(lambda:SupprimerFournisseur.close())
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(200, 130, 291, 35))
        self.comboBox.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 140, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SupprimerFournisseur.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SupprimerFournisseur)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SupprimerFournisseur.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SupprimerFournisseur)
        self.statusbar.setObjectName("statusbar")
        SupprimerFournisseur.setStatusBar(self.statusbar)

        self.retranslateUi(SupprimerFournisseur)
        QtCore.QMetaObject.connectSlotsByName(SupprimerFournisseur)
    ##########
        # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa")

        # Ajout des éléments dans la combobox à partir de la base de données
        cursor = self.conn.cursor()
        cursor.execute("SELECT CodePostalFornisseur  FROM fornisseur")
        resultats = cursor.fetchall()
        for resultat in resultats:
                self.comboBox.addItem(str(resultat[0]))
        self.conn.close()
   ########## 
        self.pushButton.clicked.connect(self.supprimer)
        self.pushButton.clicked.connect(lambda:SupprimerFournisseur.close())

    def supprimer(self):    
        print("hello")  
        id = self.comboBox.currentText()
        forn = Fournisseur()    
        f= forn.Supprimer(id)
##########  
    def retranslateUi(self, SupprimerFournisseur):
        _translate = QtCore.QCoreApplication.translate
        SupprimerFournisseur.setWindowTitle(_translate("SupprimerFournisseur", "SupprimerFournisseur"))
        self.pushButton.setText(_translate("SupprimerFournisseur", "Supprimer"))
        self.label_6.setText(_translate("SupprimerFournisseur", "Supprimer Fournisseur"))
        self.label.setText(_translate("SupprimerFournisseur", "CODE/FOURNISSEUR"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_SupprimerFournisseur()
     SupprimerFournisseur = QtWidgets.QMainWindow()
     ui.setupUi(SupprimerFournisseur)
     SupprimerFournisseur.show()
     sys.exit(app.exec_())