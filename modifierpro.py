# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import mysql.connector
import datetime
from les_classes.class_produit import *


class Ui_ModifierProduit(object):
    def setupUi(self, ModifierProduit):
        ModifierProduit.setObjectName("ModifierProduit")
        ModifierProduit.resize(920, 842)
        ModifierProduit.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ModifierProduit.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(ModifierProduit)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(90, 20, 751, 631))
        self.widget_2.setStyleSheet("#widget_2{\n"
"background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;}")
        self.widget_2.setObjectName("widget_2")
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
        self.label_6.setGeometry(QtCore.QRect(310, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 0, 50, 28))
        self.pushButton_2.setStyleSheet("\n"
"background-color: transparent;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-fermer-la-fenêtre-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:ModifierProduit.close())
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
        self.comboBox.setGeometry(QtCore.QRect(79, 510, 371, 31))
        self.comboBox.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 240, 93, 31))
        self.pushButton_3.setStyleSheet("background-color:  #CFE9C2;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(90, 690, 191, 91))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setGeometry(QtCore.QRect(79, 110, 371, 31))
        self.comboBox_2.setAccessibleDescription("")
        self.comboBox_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(79, 90, 71, 16))
        self.label_5.setStyleSheet("color: rgb(148, 148, 148);")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(492, 180, 231, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid  rgb(245, 245, 245);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        ModifierProduit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifierProduit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        ModifierProduit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifierProduit)
        self.statusbar.setObjectName("statusbar")
        ModifierProduit.setStatusBar(self.statusbar)

        self.retranslateUi(ModifierProduit)
        QtCore.QMetaObject.connectSlotsByName(ModifierProduit)

    def retranslateUi(self, ModifierProduit):
        _translate = QtCore.QCoreApplication.translate
        ModifierProduit.setWindowTitle(_translate("ModifierProduit", "ModifierProduit"))
        self.lineEdit_3.setPlaceholderText(_translate("ModifierProduit", "NOM/PRODUIT"))
        self.pushButton.setText(_translate("ModifierProduit", "Modifier"))
        self.label_6.setText(_translate("ModifierProduit", "Modifier"))
        self.lineEdit_4.setPlaceholderText(_translate("ModifierProduit", "DESCRIPTION"))
        self.lineEdit_5.setPlaceholderText(_translate("ModifierProduit", "PRIX UNITAIRE"))
        self.lineEdit_6.setPlaceholderText(_translate("ModifierProduit", "QUANTITE EN STOCK"))
        self.lineEdit_7.setPlaceholderText(_translate("ModifierProduit", "SEUIL ALERTE STOCK"))
        self.label.setText(_translate("ModifierProduit", "DATE DERNIERE ENTREE"))
        self.label_2.setText(_translate("ModifierProduit", "DATE DERNIERE SORTIE"))
        self.pushButton_3.setText(_translate("ModifierProduit", "Ajouter Image"))
        self.label_5.setText(_translate("ModifierProduit", "ID/PRODUIT"))


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


        # Ajout des éléments dans la combobox à partir de la base de données
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='pfa')
        c = cnx.cursor()
        c.execute("SELECT idp FROM produits")
        resultats = c.fetchall()
        for resultat in resultats:
                self.comboBox_2.addItem(str(resultat[0]))
        cnx.close()
        ##########


        self.pushButton_3.clicked.connect(self.open_dialog_box)
        self.pushButton.clicked.connect(self.modifier)
        self.pushButton.clicked.connect(lambda:ModifierProduit.close())

    def modifier(self):
        com1 = self.comboBox_2.currentText()
        com2 = self.comboBox.currentText()
        Edt3 = self.lineEdit_3.text()
        Edt4 = self.lineEdit_4.text()
        Edt5 = self.lineEdit_5.text()
        Edt6 = self.lineEdit_6.text()
        Edt7 = self.lineEdit_7.text()
        Edt8 = self.lineEdit.text()
        qdate1 = self.dateEdit.date()  # récupérer la date sous forme d'objet QDate
        qdate2 = self.dateEdit_2.date()
        date1 = datetime.date(qdate1.year(), qdate1.month(), qdate1.day()) 
        date2 = datetime.date(qdate2.year(), qdate2.month(), qdate2.day()) 
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='pfa')
        cursor = cnx.cursor()
        modification_produit = ("UPDATE produits "
                                "SET nom = %s, description = %s, prix_unitaire = %s, quantite_en_stock = %s, seuil_alerte_stock = %s, date_derniere_entree_stock = %s, date_derniere_sortie_stock = %s, image = %s, id_categorie = %s "
                                "WHERE idp = %s")
        donnees_produit = (Edt3, Edt4, Edt5, Edt6, Edt7, date1, date2, Edt8, com2,com1)
        cursor.execute(modification_produit, donnees_produit)
        cnx.commit()
        print(cursor.rowcount, "enregistrement mis à jour avec succès.")
        cursor.close()
        cnx.close()
    def open_dialog_box(self):
        filname = QFileDialog.getOpenFileName()
        self.path=filname[0]
        self.lineEdit.setText(self.path)

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_ModifierProduit()
     ModifierProduit= QtWidgets.QMainWindow()
     ui.setupUi(ModifierProduit)
     ModifierProduit.show()
     sys.exit(app.exec_())
