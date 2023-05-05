from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import datetime
from les_classes.class_Details_Commande import *

class Ui_ModifierCommande(object):
    def setupUi(self, ModifierCommande):
        ModifierCommande.setObjectName("ModifierCommande")
        ModifierCommande.resize(588, 829)
        ModifierCommande.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ModifierCommande.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(ModifierCommande)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(30, 10, 541, 751))
        self.widget_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(8079, 630, 371, 31))
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
        self.pushButton.setGeometry(QtCore.QRect(170, 690, 191, 41))
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
        self.label_6.setGeometry(QtCore.QRect(210, 20, 141, 51))
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
        self.pushButton_2.clicked.connect(lambda:ModifierCommande.close())
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
        self.dateEdit = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit.setGeometry(QtCore.QRect(79, 210, 371, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, 200, 141, 16))
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
        self.label_2.setGeometry(QtCore.QRect(80, 260, 41, 20))
        self.label_2.setStyleSheet("color: rgb(148, 148, 148);")
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setGeometry(QtCore.QRect(79, 150, 371, 31))
        self.comboBox_2.setAccessibleDescription("")
        self.comboBox_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(79, 130, 113, 22))
        self.lineEdit.setStyleSheet("color: rgb(148, 148, 148);")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_5.setGeometry(QtCore.QRect(79, 330, 371, 31))
        self.comboBox_5.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.comboBox_5.setCurrentText("")
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(79, 310, 51, 20))
        self.label_8.setStyleSheet("color: rgb(148, 148, 148);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(79, 390, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(79, 510, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(79, 450, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(79, 630, 371, 31))
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
        ModifierCommande.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifierCommande)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 26))
        self.menubar.setObjectName("menubar")
        ModifierCommande.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifierCommande)
        self.statusbar.setObjectName("statusbar")
        ModifierCommande.setStatusBar(self.statusbar)
        self.retranslateUi(ModifierCommande)
        QtCore.QMetaObject.connectSlotsByName(ModifierCommande)

         #######
            ##########
        #desactive les edit text:
        self.dateEdit.setReadOnly(True)
        self.comboBox.setDisabled(True)
        self.comboBox_5.setDisabled(True)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        
        
       

       # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa")

        # Ajout des éléments dans la combobox à partir de la base de données
        cursor = self.conn.cursor()
        cursor.execute("SELECT IDcommande FROM details_commande")
        resultats = cursor.fetchall()
        for resultat in resultats:
                self.comboBox_2.addItem(str(resultat[0]))
        self.conn.close()
   ##########
        #modiffier commande:
        ##self.pushButton.clicked.connect(self.Modiffier)
        self.pushButton.clicked.connect(lambda:ModifierCommande.close())
        # Connexion du signal de changement de sélection de la liste déroulante à la méthode de mise à jour des informations du client
        self.comboBox_2.currentIndexChanged.connect(self.updateProdcombo)
    def updateProdcombo(self, index):
        #Active les edit text:
        self.dateEdit.setReadOnly(False)
        self.comboBox.setDisabled(False)
        self.comboBox_5.setDisabled(False)
        self.lineEdit_11.setReadOnly(False)
        self.lineEdit_12.setReadOnly(False)
        self.lineEdit_13.setReadOnly(False)
        # Récupérer l'identifiant du cmd sélectionné
        commId = self.comboBox_2.currentText()

        # Se connecter à la base de données MySQL
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pfa'
        )

        # Exécuter une requête pour récupérer les informations du cmd
        cursor = db.cursor()
        cursor.execute('SELECT * FROM details_commande WHERE IDcommande  = %s', (commId,))
        cmd = cursor.fetchone()

        # Mettre à jour les champs d'édition de texte avec les informations du cmd
        if cmd[1] is not None:
                date_str = cmd[1].strftime("%d/%m/%Y")
                self.dateEdit.setDate(QtCore.QDate.fromString(date_str, "dd/MM/yyyy"))
        else:
                self.dateEdit.setDate(QtCore.QDate())  # Si la date est None, afficher la date d'aujourd'hui ou une date par défaut.
        self.comboBox.setCurrentText(cmd[2])
        self.comboBox_5.setCurrentText(cmd[3])
        self.lineEdit_11.setText(str(cmd[4]))
        self.lineEdit_12.setText(str(cmd[5]))
        self.lineEdit_13.setText(str(cmd[6]))
        self.lineEdit_5.setText(str(cmd[7]))
        self.lineEdit_6.setText(str(cmd[8]))
        
        



        # Fermer la connexion à la base de données
        db.close()

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
                self.comboBox_5.addItem(str(resultat[0]))
           
        
        
        # Connexion du signal de changement de sélection de la liste déroulante à la méthode de mise à jour des informations du produits
        self.comboBox_5.currentIndexChanged.connect(self.updateProduitInfo)
        # Connexion du signal de changement de lineEdit de quantite à la méthode de mise à jour des informations du produits
        self.lineEdit_11.textChanged.connect(self.updateProduitQuantite)
        # Connexion du signal de changement de lineEdit de la remise à la méthode de mise à jour des informations du produits
        self.lineEdit_12.textChanged.connect(self.updateProduitRemise)
        # Connexion du signal de changement de lineEdit de la TVA à la méthode de mise à jour des informations du produits
        self.lineEdit_13.textChanged.connect(self.updateProduitTVA)
######
    def updateProduitInfo(self):

        # Récupérer l'identifiant du produit sélectionné
        prodNom = self.comboBox_5.currentText()

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
        self.lineEdit_6.setText(str(prod[0]))
     
        # Fermer la connexion à la base de données
        db.close()
 ################
# Methode pour le changement de quantite:
    def updateProduitQuantite(self):
        try:
                q = self.lineEdit_11.text()
                if q:
                        q = float(q)
                else:
                        q = 1.0
                        prixProd=self.updateProduitInfo()
                        return
                
                
                ht = float(self.lineEdit_5.text())
                ttc = float(self.lineEdit_6.text())
                self.lineEdit_5.setText(str(q*ht))
                self.lineEdit_6.setText(str(q*ttc))
        except Exception as e:
                M = QtWidgets.QMessageBox.warning(ModifierCommande, "Erreur", str(e))
                self.lineEdit_11.setText(str(0))
        

#############
# Methode pour le changement de la remise:
    def updateProduitRemise(self):
        try:
                text = self.lineEdit_12.text()
                if text:
                        r = float(text)
                        if r > 100:
                                M = QtWidgets.QMessageBox.warning(ModifierCommande, "Erreur", "il ne faut pas dépasser 100!!")
                                self.lineEdit_12.setText("100")
                        else:   
                                            
                                ht = float(self.lineEdit_5.text())
                                ttc = float(self.lineEdit_6.text())
                                remise = (ht/100)*r
                                self.lineEdit_5.setText(str(ht-remise))
                                self.lineEdit_6.setText(str(ttc-remise))
                                              
                else:
                        #prixProd=self.updateProduitInfo() 
                        q=self.updateProduitQuantite()
                        pass
        except Exception as e:
                M = QtWidgets.QMessageBox.warning(ModifierCommande, "Erreur", str(e))
                self.lineEdit_12.setText(str(0))

# Methode pour le changement de la TVA:
    def updateProduitTVA(self):
        try:
                text = self.lineEdit_13.text()
                if text:
                        tva = float(text)
                        if tva > 100:
                                M = QtWidgets.QMessageBox.warning(ModifierCommande, "Erreur", "il ne faut pas dépasser 100!!")
                                self.lineEdit_13.setText("100")
                        else:
                                ttc = float(self.lineEdit_6.text())
                                LaTva=(ttc/100)*tva
                                self.lineEdit_6.setText(str(ttc+LaTva))
                                              
                else:
                        #prixProd=self.updateProduitInfo() 
                        #q=self.updateProduitQuantite()
                        r=self.updateProduitRemise()

                        pass
        except Exception as e:
                M = QtWidgets.QMessageBox.warning(ModifierCommande, "Erreur", str(e))
                self.lineEdit_13.setText(str(0))
    def Modiffier(self):
           print("hello")
           Edt1 = self.comboBox_2.currentText()
           qdate = self.dateEdit.date()  # récupérer la date sous forme d'objet QDate
           date = datetime.date(qdate.year(), qdate.month(), qdate.day())  # convertir en datetime.date
           Edt2 = self.comboBox.currentText()
           Edt3 = self.comboBox_5.currentText()
           Edt4 = self.lineEdit_11.text()
           Edt5 = self.lineEdit_12.text()
           Edt6 = self.lineEdit_13.text()
           Edt7 = self.lineEdit_5.text()
           Edt8 = self.lineEdit_6.text()
           
           cmd = Details_Commande(Edt1, date, Edt2, Edt3, Edt4, Edt5, Edt6, Edt7, Edt8)
           ajou = cmd.Ajouter()

    def retranslateUi(self, ModifierCommande):
        _translate = QtCore.QCoreApplication.translate
        ModifierCommande.setWindowTitle(_translate("ModifierCommande", "ModifierCommande"))
        self.lineEdit_3.setPlaceholderText(_translate("ModifierCommande", "TOTAL TTC"))
        self.pushButton.setText(_translate("ModifierCommande", "Modifier"))
        self.label_6.setText(_translate("ModifierCommande", "Modifier"))
        self.lineEdit_5.setPlaceholderText(_translate("ModifierCommande", "TOTAL HT"))
        self.label.setText(_translate("ModifierCommande", "DATE COMMANDE"))
        self.label_2.setText(_translate("ModifierCommande", "CLIENT"))
        self.lineEdit.setText(_translate("ModifierCommande", "ID/COMMANDE"))
        self.label_8.setText(_translate("ModifierCommande", "PRODUIT"))
        self.lineEdit_11.setPlaceholderText(_translate("ModifierCommande", "QUANTITE PRODUIT"))
        self.lineEdit_13.setPlaceholderText(_translate("ModifierCommande", "TVA %"))
        self.lineEdit_12.setPlaceholderText(_translate("ModifierCommande", "REMISE %"))
        self.lineEdit_6.setPlaceholderText(_translate("ModifierCommande", "TOTAL TTC"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_ModifierCommande()
     ModifierCommande = QtWidgets.QMainWindow()
     ui.setupUi(ModifierCommande)
     ModifierCommande.show()
     sys.exit(app.exec_())