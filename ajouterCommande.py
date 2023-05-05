from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import datetime
from les_classes.class_Details_Commande import *
class Ui_AjouterCommande(object):
    def setupUi(self, AjouterCommande):
        AjouterCommande.setObjectName("AjouterCommande")
        AjouterCommande.resize(628, 921)
        AjouterCommande.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AjouterCommande.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(AjouterCommande)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(50, 10, 531, 811))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(79, 630, 371, 31))
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
        self.pushButton.setGeometry(QtCore.QRect(160, 710, 191, 41))
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
        self.label_6.setGeometry(QtCore.QRect(120, 20, 291, 51))
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
        self.pushButton_2.clicked.connect(lambda:AjouterCommande.close())
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(79, 570, 371, 31))
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
        self.lineEdit_6.setGeometry(QtCore.QRect(79, 510, 371, 31))
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
        self.dateEdit.setGeometry(QtCore.QRect(79, 210, 371, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, 190, 141, 16))
        self.label.setStyleSheet("color: rgb(148, 148, 148);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(79, 270, 371, 31))
        self.comboBox.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(79, 250, 41, 20))
        self.label_2.setStyleSheet("color: rgb(148, 148, 148);")
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setGeometry(QtCore.QRect(79, 330, 371, 31))
        self.comboBox_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(79, 310, 51, 20))
        self.label_3.setStyleSheet("color: rgb(148, 148, 148);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(79, 390, 371, 31))
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
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(79, 450, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        AjouterCommande.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AjouterCommande)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 26))
        self.menubar.setObjectName("menubar")
        AjouterCommande.setMenuBar(self.menubar)

        self.retranslateUi(AjouterCommande)
        QtCore.QMetaObject.connectSlotsByName(AjouterCommande)
        #######
        #Ajouter commande:
        self.pushButton.clicked.connect(self.Ajouter)
        self.pushButton.clicked.connect(lambda:AjouterCommande.close())
    #remplire le combobox client et produit:
     # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa")

        # Ajout des éléments des clients dans la combobox à partir de la base de données
        cursor = self.conn.cursor()
        cursor.execute("SELECT nom FROM client")
        resultats = cursor.fetchall()
        for resultat in resultats:
                self.comboBox.addItem(str(resultat[0]))
        # Ajout des éléments des produits dans la combobox à partir de la base de données
        cursor = self.conn.cursor()
        cursor.execute("SELECT nom FROM produits")
        resultats = cursor.fetchall()
        for resultat in resultats:
                self.comboBox_2.addItem(str(resultat[0]))
           
        #desactive les edit text:
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        # Connexion du signal de changement de sélection de la liste déroulante à la méthode de mise à jour des informations du produits
        self.comboBox_2.currentIndexChanged.connect(self.updateProduitInfo)
        # Connexion du signal de changement de lineEdit de quantite à la méthode de mise à jour des informations du produits
        self.lineEdit_7.textChanged.connect(self.updateProduitQuantite)
        # Connexion du signal de changement de lineEdit de la remise à la méthode de mise à jour des informations du produits
        self.lineEdit_8.textChanged.connect(self.updateProduitRemise)
        # Connexion du signal de changement de lineEdit de la TVA à la méthode de mise à jour des informations du produits
        self.lineEdit_6.textChanged.connect(self.updateProduitTVA)
######
    def updateProduitInfo(self):

        # Récupérer l'identifiant du produit sélectionné
        prodNom = self.comboBox_2.currentText()

        # Se connecter à la base de données MySQL
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pfa'
        )

        # Exécuter une requête pour récupérer les informations du produits
        cursor = db.cursor()
        cursor.execute('SELECT prix_unitaire FROM produits WHERE nom  = %s', (prodNom,))
        prod = cursor.fetchone()

        # Mettre à jour les champs d'édition de texte avec les informations du produits
        self.lineEdit_5.setText(str(prod[0]))
        self.lineEdit_3.setText(str(prod[0]))
     
        # Fermer la connexion à la base de données
        db.close()
 ################
# Methode pour le changement de quantite:
    def updateProduitQuantite(self):
        try:
                q = self.lineEdit_7.text()
                if q:
                        q = float(q)
                else:
                        q = 1.0
                        prixProd=self.updateProduitInfo()
                        return
                
                
                ht = float(self.lineEdit_5.text())
                ttc = float(self.lineEdit_3.text())
                self.lineEdit_5.setText(str(q*ht))
                self.lineEdit_3.setText(str(q*ttc))
        except Exception as e:
                M = QtWidgets.QMessageBox.warning(AjouterCommande, "Erreur", str(e))
                self.lineEdit_7.setText(str(0))
        

#############
# Methode pour le changement de la remise:
    def updateProduitRemise(self):
        try:
                text = self.lineEdit_8.text()
                if text:
                        r = float(text)
                        if r > 100:
                                M = QtWidgets.QMessageBox.warning(AjouterCommande, "Erreur", "il ne faut pas dépasser 100!!")
                                self.lineEdit_8.setText("100")
                        else:   
                                            
                                ht = float(self.lineEdit_5.text())
                                ttc = float(self.lineEdit_3.text())
                                remise = (ht/100)*r
                                self.lineEdit_5.setText(str(ht-remise))
                                self.lineEdit_3.setText(str(ttc-remise))
                                              
                else:
                        #prixProd=self.updateProduitInfo() 
                        q=self.updateProduitQuantite()
                        pass
        except Exception as e:
                M = QtWidgets.QMessageBox.warning(AjouterCommande, "Erreur", str(e))
                self.lineEdit_8.setText(str(0))

# Methode pour le changement de la TVA:
    def updateProduitTVA(self):
        try:
                text = self.lineEdit_6.text()
                if text:
                        tva = float(text)
                        if tva > 100:
                                M = QtWidgets.QMessageBox.warning(AjouterCommande, "Erreur", "il ne faut pas dépasser 100!!")
                                self.lineEdit_6.setText("100")
                        else:
                                ttc = float(self.lineEdit_3.text())
                                LaTva=(ttc/100)*tva
                                self.lineEdit_3.setText(str(ttc+LaTva))
                                              
                else:
                        #prixProd=self.updateProduitInfo() 
                        #q=self.updateProduitQuantite()
                        r=self.updateProduitRemise()

                        pass
        except Exception as e:
                M = QtWidgets.QMessageBox.warning(AjouterCommande, "Erreur", str(e))
                self.lineEdit_6.setText(str(0))
    def Ajouter(self):
           print("hello")
           Edt1 = self.lineEdit_2.text()
           qdate = self.dateEdit.date()  # récupérer la date sous forme d'objet QDate
           date = datetime.date(qdate.year(), qdate.month(), qdate.day())  # convertir en datetime.date
           Edt2 = self.comboBox.currentText()
           Edt3 = self.comboBox_2.currentText()
           Edt4 = self.lineEdit_7.text()
           Edt5 = self.lineEdit_8.text()
           Edt6 = self.lineEdit_6.text()
           Edt7 = self.lineEdit_5.text()
           Edt8 = self.lineEdit_3.text()
           
           cmd = Details_Commande(Edt1, date, Edt2, Edt3, Edt4, Edt5, Edt6, Edt7, Edt8)
           ajou = cmd.Ajouter()

    def retranslateUi(self, AjouterCommande):
        _translate = QtCore.QCoreApplication.translate
        AjouterCommande.setWindowTitle(_translate("AjouterCommande", "AjouterCommande"))
        self.lineEdit_2.setPlaceholderText(_translate("AjouterCommande", "ID/COMMANDE"))
        self.lineEdit_3.setPlaceholderText(_translate("AjouterCommande", "TOTAL TTC"))
        self.pushButton.setText(_translate("AjouterCommande", "Ajouter"))
        self.label_6.setText(_translate("AjouterCommande", "Ajouter Commande"))
        self.lineEdit_5.setPlaceholderText(_translate("AjouterCommande", "TOTAL HT"))
        self.lineEdit_6.setPlaceholderText(_translate("AjouterCommande", "TVA %"))
        self.label.setText(_translate("AjouterCommande", "DATE COMMANDE"))
        self.label_2.setText(_translate("AjouterCommande", "CLIENT"))
        self.label_3.setText(_translate("AjouterCommande", "PRODUIT"))
        self.lineEdit_7.setPlaceholderText(_translate("AjouterCommande", "QUANTITE PRODUIT"))
        self.lineEdit_8.setPlaceholderText(_translate("AjouterCommande", "REMISE %"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_AjouterCommande()
     AjouterCommande= QtWidgets.QMainWindow()
     ui.setupUi(AjouterCommande)
     AjouterCommande.show()
     sys.exit(app.exec_())
