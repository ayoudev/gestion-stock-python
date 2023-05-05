
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from les_classes.class_Categories import *
class Ui_ModifierCategorie(object):
    def setupUi(self, ModifierCategorie):
        ModifierCategorie.setObjectName("ModifierCategorie")
        ModifierCategorie.resize(800, 472)
        ModifierCategorie.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ModifierCategorie.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(ModifierCategorie)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(140, 20, 541, 341))
        self.widget_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.widget_2.setObjectName("widget_2")
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
        self.pushButton.setGeometry(QtCore.QRect(180, 270, 191, 41))
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
        self.label_6.setGeometry(QtCore.QRect(210, 40, 151, 51))
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
        self.pushButton_2.clicked.connect(lambda:ModifierCategorie.close())
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
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 113, 22))
        self.lineEdit.setStyleSheet("color: rgb(148, 148, 148);")
        self.lineEdit.setObjectName("lineEdit")
        ModifierCategorie.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifierCategorie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ModifierCategorie.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifierCategorie)
        self.statusbar.setObjectName("statusbar")
        ModifierCategorie.setStatusBar(self.statusbar)

        self.retranslateUi(ModifierCategorie)
        QtCore.QMetaObject.connectSlotsByName(ModifierCategorie)
         ##########
        #desactive les edit text:
        self.lineEdit_3.setReadOnly(True)
        
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

######################
        ###
        self.pushButton.clicked.connect(self.modifier)
        self.pushButton.clicked.connect(lambda:ModifierCategorie.close())
        ####
        # Connexion du signal de changement de sélection de la liste déroulante à la méthode de mise à jour des informations du categorie
        self.comboBox.currentIndexChanged.connect(self.updateClientInfo)
    def updateClientInfo(self, index):
        #Active les edit text:
        self.lineEdit_3.setReadOnly(False)

        # Récupérer l'identifiant du categories sélectionné
        catId = self.comboBox.currentText()

        # Se connecter à la base de données MySQL
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pfa'
        )

        # Exécuter une requête pour récupérer les informations du categories
        cursor = db.cursor()
        cursor.execute('SELECT * FROM categories WHERE id_categorie  = %s', (catId,))
        cat = cursor.fetchone()

        # Mettre à jour les champs d'édition de texte avec les informations du categories
        self.lineEdit_3.setText(cat[1])
     
        # Fermer la connexion à la base de données
        db.close()

        
        #############
    def modifier(self):
       
        print("hello")
        edt2 = self.lineEdit_3.text()
        
        id = self.comboBox.currentText()
        categ = Categories(id, edt2)
        v = categ.modifier()


########################        

    def retranslateUi(self, ModifierCategorie):
        _translate = QtCore.QCoreApplication.translate
        ModifierCategorie.setWindowTitle(_translate("ModifierCategorie", "ModifierCategorie"))
        self.lineEdit_3.setPlaceholderText(_translate("ModifierCategorie", "NOM CATEGORIE"))
        self.pushButton.setText(_translate("ModifierCategorie", "Modifier"))
        self.label_6.setText(_translate("ModifierCategorie", "Modifier"))
        self.lineEdit.setText(_translate("ModifierCategorie", "ID/CATEGORIE"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_ModifierCategorie()
     ModifierCategorie = QtWidgets.QMainWindow()
     ui.setupUi(ModifierCategorie)
     ModifierCategorie.show()
     sys.exit(app.exec_())
