from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import sys
import datetime
import mysql.connector

from les_classes.class_produit import *

class Ui_AjouterProduit(object):
    def setupUi(self, AjouterProduit):
        AjouterProduit.setObjectName("AjouterProduit")
        AjouterProduit.resize(945, 871)
        AjouterProduit.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AjouterProduit.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(AjouterProduit)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(90, 10, 751, 631))
        self.widget_2.setStyleSheet("#widget_2{\n"
"background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(79, 110, 371, 31))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(79, 160, 371, 31))
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
        self.pushButton.setGeometry(QtCore.QRect(310, 560, 191, 41))
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
        self.label_6.setGeometry(QtCore.QRect(230, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 10, 50, 28))
        self.pushButton_2.setStyleSheet("background-color:transparent;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-fermer-la-fenêtre-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:AjouterProduit.close())
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(79, 210, 371, 31))
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
        self.lineEdit_5.setGeometry(QtCore.QRect(79, 260, 371, 31))
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
        self.lineEdit_6.setGeometry(QtCore.QRect(79, 310, 371, 31))
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
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(79, 360, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.dateEdit = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit.setGeometry(QtCore.QRect(79, 410, 371, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, 400, 141, 16))
        self.label.setStyleSheet("color: rgb(148, 148, 148);")
        self.label.setObjectName("label")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(79, 460, 371, 31))
        self.dateEdit_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(80, 450, 141, 16))
        self.label_2.setStyleSheet("color: rgb(148, 148, 148);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(80, 510, 371, 31))
        self.comboBox.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 280, 93, 31))
        self.pushButton_3.setStyleSheet("background-color:  #CFE9C2;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(490, 220, 211, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid  rgb(245, 245, 245);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        AjouterProduit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AjouterProduit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 26))
        self.menubar.setObjectName("menubar")
        AjouterProduit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AjouterProduit)
        self.statusbar.setObjectName("statusbar")
        AjouterProduit.setStatusBar(self.statusbar)

        self.retranslateUi(AjouterProduit)
        QtCore.QMetaObject.connectSlotsByName(AjouterProduit)

    def retranslateUi(self, AjouterProduit):
        _translate = QtCore.QCoreApplication.translate
        AjouterProduit.setWindowTitle(_translate("AjouterProduit", "AjouterProduit"))
        self.lineEdit_2.setPlaceholderText(_translate("AjouterProduit", "ID/PRODUIT"))
        self.lineEdit_3.setPlaceholderText(_translate("AjouterProduit", "NOM/PRODUIT"))
        self.pushButton.setText(_translate("AjouterProduit", "Ajouter"))
        self.label_6.setText(_translate("AjouterProduit", "Ajouter Produit"))
        self.lineEdit_4.setPlaceholderText(_translate("AjouterProduit", "DESCRIPTION"))
        self.lineEdit_5.setPlaceholderText(_translate("AjouterProduit", "PRIX UNITAIRE"))
        self.lineEdit_6.setPlaceholderText(_translate("AjouterProduit", "QUANTITE EN STOCK"))
        self.lineEdit_7.setPlaceholderText(_translate("AjouterProduit", "SEUIL ALERTE STOCK"))
        self.label.setText(_translate("AjouterProduit", "DATE DERNIERE ENTREE"))
        self.label_2.setText(_translate("AjouterProduit", "DATE DERNIERE SORTIE"))
        self.pushButton_3.setText(_translate("AjouterProduit", "Ajouter Image"))
        self.pushButton_3.clicked.connect(self.open_dialog_box)
        self.pushButton.clicked.connect(self.ajouter)
        self.pushButton.clicked.connect(lambda:AjouterProduit.close())



        # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa")

        # Ajout des éléments dans la combobox à partir de la base de données
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_categorie FROM categories")
        resultats = cursor.fetchall()
        for resultat in resultats:
                self.comboBox.addItem(str(resultat[0]))
        self.conn.close()
        ##########

 
    def open_dialog_box(self):
        filname = QFileDialog.getOpenFileName()
        self.path=filname[0]
        self.lineEdit.setText(self.path)
       
    

    def ajouter(self):
        Edt1 = self.lineEdit_2.text()
        Edt2 = self.lineEdit_3.text()
        Edt3 = self.lineEdit_4.text()
        Edt4 = self.lineEdit_5.text()
        Edt5 = self.lineEdit_6.text()
        Edt6 = self.lineEdit_7.text()
        Edt7 = self.lineEdit.text()
        com = self.comboBox.currentText()
        qdate1 = self.dateEdit.date()  # récupérer la date sous forme d'objet QDate
        qdate2 = self.dateEdit_2.date()
        date1 = datetime.date(qdate1.year(), qdate1.month(), qdate1.day()) 
        date2 = datetime.date(qdate2.year(), qdate2.month(), qdate2.day()) 
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='pfa')
        cursor = cnx.cursor()
        ajout_produit = ("INSERT INTO produits "
                         "(idp, nom, description, prix_unitaire, quantite_en_stock, seuil_alerte_stock, date_derniere_entree_stock, date_derniere_sortie_stock, image, id_categorie) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        donnees_produit = (Edt1, Edt2, Edt3, Edt4, Edt5, Edt6, date1, date2,Edt7, com)
        cursor.execute(ajout_produit, donnees_produit)
        cnx.commit()
        cursor.close()
        cnx.close()
         

    


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_AjouterProduit()
     AjouterProduit= QtWidgets.QMainWindow()
     ui.setupUi(AjouterProduit)
     AjouterProduit.show()
     sys.exit(app.exec_())
