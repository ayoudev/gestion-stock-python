from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from les_classes.class_Categories import *
class Ui_AjouterCategorie(object):
    def setupUi(self, AjouterCategorie):
        AjouterCategorie.setObjectName("AjouterCategorie")
        AjouterCategorie.resize(800, 418)
        AjouterCategorie.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AjouterCategorie.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(AjouterCategorie)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(120, 10, 541, 341))
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
        self.label_6.setGeometry(QtCore.QRect(160, 20, 271, 51))
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
        self.pushButton_2.clicked.connect(lambda:AjouterCategorie.close())
        AjouterCategorie.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AjouterCategorie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        AjouterCategorie.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AjouterCategorie)
        self.statusbar.setObjectName("statusbar")
        AjouterCategorie.setStatusBar(self.statusbar)

        self.retranslateUi(AjouterCategorie)
        QtCore.QMetaObject.connectSlotsByName(AjouterCategorie)
        ####
        self.pushButton.clicked.connect(self.ajouter)
        self.pushButton.clicked.connect(lambda:AjouterCategorie.close())
        ####
        #############
    def ajouter(self):
        print("hello")
        Edt1 = self.lineEdit_2.text()
        Edt2 = self.lineEdit_3.text()
        
        ajouCat = Categories(Edt1, Edt2)
        ajou = ajouCat.ajouter()
        
        #############

    def retranslateUi(self, AjouterCategorie):
        _translate = QtCore.QCoreApplication.translate
        AjouterCategorie.setWindowTitle(_translate("AjouterCategorie", "AjouterCategorie"))
        self.lineEdit_2.setPlaceholderText(_translate("AjouterCategorie", "ID/CATEGORIE"))
        self.lineEdit_3.setPlaceholderText(_translate("AjouterCategorie", "NOM CATEGORIE"))
        self.pushButton.setText(_translate("AjouterCategorie", "Ajouter"))
        self.label_6.setText(_translate("AjouterCategorie", "Ajouter Categorie"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_AjouterCategorie()
     AjouterCategorie = QtWidgets.QMainWindow()
     ui.setupUi(AjouterCategorie)
     AjouterCategorie.show()
     sys.exit(app.exec_())
