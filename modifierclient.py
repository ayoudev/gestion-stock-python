from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from les_classes.class_Client import *

class Ui_ModifierClient(object):
    def setupUi(self, ModifierClient):
        ModifierClient.setObjectName("ModifierClient")
        ModifierClient.resize(653, 793)
        ModifierClient.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ModifierClient.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(ModifierClient)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(50, 60, 541, 631))
        self.widget_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(79, 210, 371, 31))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(79, 270, 371, 31))
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
        self.pushButton.setGeometry(QtCore.QRect(170, 580, 191, 41))
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
        self.label_6.setGeometry(QtCore.QRect(210, 20, 151, 51))
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
        self.pushButton_2.clicked.connect(lambda:ModifierClient.close())
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(79, 330, 371, 31))
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
        self.lineEdit_5.setGeometry(QtCore.QRect(79, 390, 371, 31))
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
        self.lineEdit_6.setGeometry(QtCore.QRect(79, 450, 371, 31))
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
        self.dateEdit.setGeometry(QtCore.QRect(80, 510, 371, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, 490, 141, 16))
        self.label.setStyleSheet("color: rgb(148, 148, 148);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(79, 150, 371, 31))
        self.comboBox.setAccessibleDescription("")
        self.comboBox.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(79, 130, 113, 22))
        self.lineEdit.setStyleSheet("color: rgb(148, 148, 148);")
        self.lineEdit.setObjectName("lineEdit")
        ModifierClient.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifierClient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 26))
        self.menubar.setObjectName("menubar")
        ModifierClient.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifierClient)
        self.statusbar.setObjectName("statusbar")
        ModifierClient.setStatusBar(self.statusbar)

   ##########
        #desactive les edit text:
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.dateEdit.setReadOnly(True)
       

       # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa")

        # Ajout des éléments dans la combobox à partir de la base de données
        cursor = self.conn.cursor()
        cursor.execute("SELECT idC FROM client")
        resultats = cursor.fetchall()
        for resultat in resultats:
                self.comboBox.addItem(str(resultat[0]))
        self.conn.close()
   ##########

        self.retranslateUi(ModifierClient)
        QtCore.QMetaObject.connectSlotsByName(ModifierClient)



######################
        ###
        self.pushButton.clicked.connect(self.modifier)
        self.pushButton.clicked.connect(lambda:ModifierClient.close())
        ####
        # Connexion du signal de changement de sélection de la liste déroulante à la méthode de mise à jour des informations du client
        self.comboBox.currentIndexChanged.connect(self.updateClientInfo)
    def updateClientInfo(self, index):
        #Active les edit text:
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_6.setReadOnly(False)
        self.dateEdit.setReadOnly(False)
        # Récupérer l'identifiant du client sélectionné
        clientId = self.comboBox.currentText()

        # Se connecter à la base de données MySQL
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pfa'
        )

        # Exécuter une requête pour récupérer les informations du client
        cursor = db.cursor()
        cursor.execute('SELECT * FROM client WHERE idC = %s', (clientId,))
        client = cursor.fetchone()

        # Mettre à jour les champs d'édition de texte avec les informations du client
        self.lineEdit_2.setText(client[2])
        self.lineEdit_3.setText(client[1])
        self.lineEdit_4.setText(client[3])
        self.lineEdit_5.setText(client[4])
        self.lineEdit_6.setText(client[5])
        if client[6] is not None:
                date_str = client[6].strftime("%d/%m/%Y")
                self.dateEdit.setDate(QtCore.QDate.fromString(date_str, "dd/MM/yyyy"))
        else:
                self.dateEdit.setDate(QtCore.QDate())  # Si la date est None, afficher la date d'aujourd'hui ou une date par défaut.



        # Fermer la connexion à la base de données
        db.close()

        
        #############
    def modifier(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa"
        )
        print("hello")
        edt1 = self.lineEdit_2.text()
        edt2 = self.lineEdit_3.text()
        edt3 = self.lineEdit_4.text()
        edt4 = self.lineEdit_5.text()
        edt5 = self.lineEdit_6.text()
        edt6 = self.dateEdit.date().toString("yyyy-MM-dd")
        id = self.comboBox.currentText()
        client = Client(edt1, edt2, edt3, edt4, edt5, edt6)
        cursor = conn.cursor()
        sql, val = client.Modifier(id)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "enregistrement mis à jour avec succès.")

########################        



    def retranslateUi(self, ModifierClient):
        _translate = QtCore.QCoreApplication.translate
        ModifierClient.setWindowTitle(_translate("ModifierClient", "ModifierClient"))
        self.lineEdit_2.setPlaceholderText(_translate("ModifierClient", "PRENOM/CLIENT"))
        self.lineEdit_3.setPlaceholderText(_translate("ModifierClient", "NOM CLIENT"))
        self.pushButton.setText(_translate("ModifierClient", "Modifier"))
        self.label_6.setText(_translate("ModifierClient", "Modifier"))
        self.lineEdit_4.setPlaceholderText(_translate("ModifierClient", "TELE"))
        self.lineEdit_5.setPlaceholderText(_translate("ModifierClient", "EMAIL"))
        self.lineEdit_6.setPlaceholderText(_translate("ModifierClient", "ADRESSE"))
        self.label.setText(_translate("ModifierClient", "DATE NAISSANCE"))
        self.lineEdit.setText(_translate("ModifierClient", "ID/CLIENT"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_ModifierClient()
     ModifierClient = QtWidgets.QMainWindow()
     ui.setupUi(ModifierClient)
     ModifierClient.show()
     sys.exit(app.exec_())