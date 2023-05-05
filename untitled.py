from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from principe import *
from les_classes.class_Compte import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 635)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 981, 581))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 331, 541))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image/Checking boxes (1).gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget_3.setGeometry(QtCore.QRect(340, 30, 631, 541))
        self.stackedWidget_3.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.login = QtWidgets.QWidget()
        self.login.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.login.setObjectName("login")
        self.pushButton_2 = QtWidgets.QPushButton(self.login)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 0, 50, 28))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-fermer-la-fenêtre-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:MainWindow.close())
        self.label_6 = QtWidgets.QLabel(self.login)
        self.label_6.setGeometry(QtCore.QRect(230, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.login)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 150, 411, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.login)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 250, 411, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.login)
        self.pushButton.setGeometry(QtCore.QRect(240, 350, 191, 41))
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
        self.label_4 = QtWidgets.QLabel(self.login)
        self.label_4.setGeometry(QtCore.QRect(200, 410, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 0.464);")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.login)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 440, 71, 20))
        self.pushButton_3.setStyleSheet("color:rgba(11, 131, 120, 219);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.login)
        self.label_7.setGeometry(QtCore.QRect(240, 440, 111, 20))
        self.label_7.setStyleSheet("color:rgba(0, 0, 0, 0.464);")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.login)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 31, 21))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/icons8-utilisateur-48.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.login)
        self.label_5.setGeometry(QtCore.QRect(70, 260, 31, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icons/icons8-mode-portrait-verrouillé-24.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.stackedWidget_3.addWidget(self.login)
        self.signup = QtWidgets.QWidget()
        self.signup.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-bottom-right-radius: 80px;")
        self.signup.setObjectName("signup")
        self.pushButton_5 = QtWidgets.QPushButton(self.signup)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 10, 31, 28))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda:MainWindow.close())
        self.label_12 = QtWidgets.QLabel(self.signup)
        self.label_12.setGeometry(QtCore.QRect(260, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.signup)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 160, 431, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(self.signup)
        self.label_10.setGeometry(QtCore.QRect(60, 160, 41, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("icons/icons8-utilisateur-48.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.signup)
        self.label_11.setGeometry(QtCore.QRect(70, 260, 31, 31))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("icons/icons8-mode-portrait-verrouillé-24.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.signup)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 260, 431, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.signup)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 360, 431, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border:none;\n"
"border-bottom:1.5px solid #CFE9C2;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_13 = QtWidgets.QLabel(self.signup)
        self.label_13.setGeometry(QtCore.QRect(70, 360, 31, 31))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("icons/icons8-mode-portrait-verrouillé-24.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.pushButton_4 = QtWidgets.QPushButton(self.signup)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 450, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"    background-color: qlineargradient(spread:pad, x1:2, y1:1, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1   #CFE9C2);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:2, y1:1, x2:1, y2:0, stop:0 #CFE9C2, stop:1 rgba(11, 131, 120, 219));\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0   #CFE9C2, stop:1 rgba(11, 131, 120, 219));\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.signup)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 449, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("\n"
"color: rgb(7, 7, 7);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icons8-utilisateur-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget_3.addWidget(self.signup)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(lambda:self.loginfunction())
        self.pushButton_4.clicked.connect(lambda:self.signupcompte())
        self.pushButton_3.clicked.connect(lambda:self.stackedWidget_3.setCurrentIndex(1))
        self.pushButton_6.clicked.connect(lambda:self.stackedWidget_3.setCurrentIndex(0))
        
        
    def loginfunction(self):
         user = self.lineEdit_2.text()
         password = self.lineEdit_3.text()
         if len(user) == 0 or len(password) == 0:
              self.error.setText("Please fill in ALL the fields!")
         else:
              conn = mysql.connector.connect(host='localhost',
                                       database='pfa',
                                       user='root',
                                       password='')
              cur = conn.cursor()
              sql = "SELECT mdp FROM compte WHERE nom_utilisateur = %s"
              values = (user,)
              cur.execute(sql, values)
              result = cur.fetchone()
              if result is not None:
                   hashed_password = result[0].encode()
                   if bcrypt.checkpw(base64.b64encode(hashlib.sha256(password.encode()).digest()), hashed_password):
                       #######
                        cursor = conn.cursor()
                        cursor.execute("UPDATE compte SET user_connecter = %s WHERE nom_utilisateur = %s", 
                                        ("oui", user))
                        conn.commit()
                        print(cursor.rowcount, "enregistrement ajouté avec succès.")
                       #######
                        MainWindow.close()
                        Principe = QtWidgets.QMainWindow()
                        ui=Ui_Principe()
                        ui.setupUi(Principe)
                        Principe.show() 
                   else:
                       QtWidgets.QMessageBox.warning(MainWindow,"Compte existe", "Incorrect username or password")
              else:
                   QtWidgets.QMessageBox.warning(MainWindow,"Compte existe", "Incorrect username or password")
              cur.close()
              conn.close()
    def signupcompte(self):
        
        user_name=self.lineEdit_4.text()
        mdp1=self.lineEdit_5.text()
        mdp2=self.lineEdit_6.text()
        if user_name=="" and mdp1=="" and mdp2=="":
                M=QtWidgets.QMessageBox.warning(MainWindow,"Les champs est vide ", "Merci de remplir les champs!!")
                return
        if mdp1==mdp2:  
                compte = Compte(user_name,mdp1)
                c_a=compte.ajouter()
                if c_a==0:
                     M=QtWidgets.QMessageBox.warning(MainWindow,"Compte existe", "Ce compte est deja existe, Merci de change le nom !!")
                else:
                     M=QtWidgets.QMessageBox.warning(MainWindow,"Compte existe", "Les infos sont enregistree")               
        else:
                M=QtWidgets.QMessageBox.warning(MainWindow,"erreur", "le mots de pass invalide")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_5.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Se Connecter"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Utilisateur"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.pushButton.setText(_translate("MainWindow", "Se connecter"))
        self.label_4.setText(_translate("MainWindow", "Veuillez saisir votre identifiant et mot de passe"))
        self.pushButton_3.setText(_translate("MainWindow", "Cliquez ici"))
        self.label_7.setText(_translate("MainWindow", "Creer votre compte"))
        self.label_12.setText(_translate("MainWindow", "S\'inscrire"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Utilisateur"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Confirmer Mot de passe"))
        self.pushButton_4.setText(_translate("MainWindow", "S\'inscrire"))
        self.pushButton_6.setText(_translate("MainWindow", "Retour"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_MainWindow()
     MainWindow = QtWidgets.QMainWindow()
     ui.setupUi(MainWindow)
     MainWindow.show()
     sys.exit(app.exec_())
