from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget,QLabel,QMessageBox

from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
import sys
from ajouterCli import Ui_AjouterCli
from ajouterCategorie import Ui_AjouterCategorie
from ajouterCommande import Ui_AjouterCommande
from ajouterfournisseur import Ui_AjouterFournisseur
from ajouterpro import Ui_AjouterProduit
from modifierCategorie import Ui_ModifierCategorie
from modifierclient import Ui_ModifierClient
from modifiercommande import Ui_ModifierCommande
from modifierfournisseur import Ui_ModifierFournisseur
from modifierpro import Ui_ModifierProduit
from supprimercategorie import Ui_SupprimerCategorie
from supprimerclient import Ui_SupprimerClient
from supprimercommande import Ui_SupprimerCommande
from supprimerfournisseur import Ui_SupprimerFournisseur
from supprimerpro import Ui_SupprimerProduit
from les_classes.class_Client import *
from les_classes.class_produit import *
from PyQt5.QtGui import QPixmap, QIcon

class Ui_Principe(object):
    def setupUi(self, Principe):
        Principe.setObjectName("Principe")
        Principe.resize(1228, 660)
        Principe.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Principe.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Principe.setStyleSheet("*{\n"
"border:none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"padding:0;\n"
"margin:0;\n"
"color:1b1b27;\n"
"}\n"
"#centralwidget{\n"
"background-color:rgba(255, 255, 255, .15);\n"
"}\n"
"QPushButton{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(Principe)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"text-align:left;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1231, 661))
        self.widget.setStyleSheet("*{background-color: #1b1b27;}\n"
"QPushButton{\n"
"text-align:left;\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(self.widget)
        self.header.setStyleSheet("\n"
"background-color: #1b1b27;\n"
"")
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-menu-arrondi-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setShortcut("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icons8-utilisateur.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setShortcut("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(243, 243, 243);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/icons8-search-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/icons8-log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: transparent;")
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/icons8-fermer-la-fenêtre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_10.raise_()
        self.pushButton_2.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.pushButton.raise_()
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.main = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet("#widget_3{\n"
"background-color: #CFE9C2;\n"
"}\n"
"*{background-color: #1b1b27;}\n"
"#client:hover{\n"
"background-color: #CFE9C2;\n"
"border-left:5px solid #F3F3F3;\n"
"}\n"
"#categorie:hover{\n"
"background-color: #CFE9C2;\n"
"border-left:5px solid #F3F3F3;\n"
"}\n"
"#commande:hover{\n"
"background-color: #CFE9C2;\n"
"border-left:5px solid #F3F3F3;\n"
"}\n"
"#four:hover{\n"
"background-color: #CFE9C2;\n"
"border-left:5px solid #F3F3F3;\n"
"}\n"
"#produit:hover{\n"
"background-color: #CFE9C2;\n"
"border-left:5px solid #F3F3F3;\n"
"}\n"
"#analyse:hover{\n"
"background-color: #CFE9C2;\n"
"border-left:5px solid #F3F3F3;\n"
"}")
        self.main.setObjectName("main")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.main)
        self.widget_2.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setStyleSheet("font-weight:bold;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.widget_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.client = QtWidgets.QPushButton(self.frame_4)
        self.client.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.client.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/client.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.client.setIcon(icon5)
        self.client.setIconSize(QtCore.QSize(32, 32))
        self.client.setObjectName("client")
        self.verticalLayout_5.addWidget(self.client)
        self.four = QtWidgets.QPushButton(self.frame_4)
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/icons8-fournisseur.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.four.setIcon(icon6)
        self.four.setIconSize(QtCore.QSize(32, 32))
        self.four.setObjectName("four")
        self.verticalLayout_5.addWidget(self.four)
        self.produit = QtWidgets.QPushButton(self.frame_4)
        self.produit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/icons8-produit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.produit.setIcon(icon7)
        self.produit.setIconSize(QtCore.QSize(32, 32))
        self.produit.setObjectName("produit")
        self.verticalLayout_5.addWidget(self.produit)
        self.commande = QtWidgets.QPushButton(self.frame_4)
        self.commande.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/icons8-commande.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commande.setIcon(icon8)
        self.commande.setIconSize(QtCore.QSize(32, 32))
        self.commande.setObjectName("commande")
        self.verticalLayout_5.addWidget(self.commande)
        self.categorie = QtWidgets.QPushButton(self.frame_4)
        self.categorie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.categorie.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/icons8-classer-par-catégories.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.categorie.setIcon(icon9)
        self.categorie.setIconSize(QtCore.QSize(32, 32))
        self.categorie.setObjectName("categorie")
        self.verticalLayout_5.addWidget(self.categorie)
        self.verticalLayout_4.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.frame_5 = QtWidgets.QFrame(self.widget_5)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.analyse = QtWidgets.QPushButton(self.frame_5)
        self.analyse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/icons8-analyse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analyse.setIcon(icon10)
        self.analyse.setIconSize(QtCore.QSize(32, 32))
        self.analyse.setObjectName("analyse")
        self.verticalLayout_6.addWidget(self.analyse)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.main)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setStyleSheet("background-color: #1b1b27;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.client_2 = QtWidgets.QWidget()
        self.client_2.setObjectName("client_2")
        self.tableWidget = QtWidgets.QTableWidget(self.client_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 881, 441))
        self.tableWidget.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton_6 = QtWidgets.QPushButton(self.client_2)
        self.pushButton_6.setGeometry(QtCore.QRect(750, 500, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("font-weight:bold;\n"
"background-color: #CFE9C2;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"color:#1b1b27;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_8 = QtWidgets.QFrame(self.client_2)
        self.frame_8.setGeometry(QtCore.QRect(870, 30, 71, 162))
        self.frame_8.setStyleSheet("border-radius:20px;\n"
"background-color: #1b1b27;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/icons8-plus-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.showAjouterCli)
        self.verticalLayout_7.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/icons8-supprimer-la-propriété-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon12)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.showSupprimerClient)
        self.verticalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/icons8-modifier-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon13)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.showModifierClient)
        self.verticalLayout_7.addWidget(self.pushButton_8)
        self.stackedWidget.addWidget(self.client_2)
        self.categorie_2 = QtWidgets.QWidget()
        self.categorie_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.categorie_2.setObjectName("categorie_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.categorie_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(320, 30, 281, 441))
        self.tableWidget_2.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.frame_9 = QtWidgets.QFrame(self.categorie_2)
        self.frame_9.setGeometry(QtCore.QRect(570, 10, 71, 162))
        self.frame_9.setStyleSheet("border-radius:20px;\n"
"background-color: #1b1b27;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setText("")
        self.pushButton_11.setIcon(icon11)
        self.pushButton_11.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.showAjouterCategorie)
        self.verticalLayout_8.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon12)
        self.pushButton_12.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.showSupprimerCategorie)
        self.verticalLayout_8.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon13)
        self.pushButton_13.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.showModifierCategorie)
        self.verticalLayout_8.addWidget(self.pushButton_13)
        self.pushButton_25 = QtWidgets.QPushButton(self.categorie_2)
        self.pushButton_25.setGeometry(QtCore.QRect(730, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet("font-weight:bold;\n"
"background-color: #CFE9C2;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"color:#1b1b27;")
        self.pushButton_25.setObjectName("pushButton_25")
        self.stackedWidget.addWidget(self.categorie_2)
        self.commande_2 = QtWidgets.QWidget()
        self.commande_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commande_2.setObjectName("commande_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.commande_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 20, 881, 441))
        self.tableWidget_3.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(9)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        self.frame_10 = QtWidgets.QFrame(self.commande_2)
        self.frame_10.setGeometry(QtCore.QRect(870, 10, 71, 162))
        self.frame_10.setStyleSheet("border-radius:20px;\n"
"background-color: #1b1b27;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon11)
        self.pushButton_14.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.showAjouterCommande)
        self.verticalLayout_9.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(icon12)
        self.pushButton_15.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.showSupprimerCommande)
        self.verticalLayout_9.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setText("")
        self.pushButton_16.setIcon(icon13)
        self.pushButton_16.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.showModifierCommande)
        self.verticalLayout_9.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.commande_2)
        self.pushButton_17.setGeometry(QtCore.QRect(750, 480, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet("font-weight:bold;\n"
"background-color: #CFE9C2;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"color:#1b1b27;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.stackedWidget.addWidget(self.commande_2)
        self.four_2 = QtWidgets.QWidget()
        self.four_2.setObjectName("four_2")
        self.frame_11 = QtWidgets.QFrame(self.four_2)
        self.frame_11.setGeometry(QtCore.QRect(810, 10, 71, 162))
        self.frame_11.setStyleSheet("border-radius:20px;\n"
"background-color: #1b1b27;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon11)
        self.pushButton_18.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.showAjouterFournisseur)
        self.verticalLayout_10.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon12)
        self.pushButton_19.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.showSupprimerFournisseur)
        self.verticalLayout_10.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon13)
        self.pushButton_20.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.showModifierFournisseur)
        self.verticalLayout_10.addWidget(self.pushButton_20)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.four_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(60, 20, 781, 441))
        self.tableWidget_4.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        self.pushButton_21 = QtWidgets.QPushButton(self.four_2)
        self.pushButton_21.setGeometry(QtCore.QRect(700, 480, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("font-weight:bold;\n"
"background-color: #CFE9C2;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"color:#1b1b27;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.tableWidget_4.raise_()
        self.frame_11.raise_()
        self.pushButton_21.raise_()
        self.stackedWidget.addWidget(self.four_2)
        self.produit_2 = QtWidgets.QWidget()
        self.produit_2.setObjectName("produit_2")
        self.frame_12 = QtWidgets.QFrame(self.produit_2)
        self.frame_12.setGeometry(QtCore.QRect(880, 20, 71, 162))
        self.frame_12.setStyleSheet("border-radius:20px;\n"
"background-color: #1b1b27;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon11)
        self.pushButton_22.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(self.showAjouterProduit)
        self.verticalLayout_11.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setText("")
        self.pushButton_23.setIcon(icon12)
        self.pushButton_23.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.showSupprimerProduit)
        self.verticalLayout_11.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setText("")
        self.pushButton_24.setIcon(icon13)
        self.pushButton_24.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.clicked.connect(self.showModifierProduit)
        self.verticalLayout_11.addWidget(self.pushButton_24)
        self.pushButton_26 = QtWidgets.QPushButton(self.produit_2)
        self.pushButton_26.setGeometry(QtCore.QRect(750, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setStyleSheet("font-weight:bold;\n"
"background-color: #CFE9C2;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"color:#1b1b27;")
        self.pushButton_26.setObjectName("pushButton_26")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.produit_2)
        self.tableWidget_5.setGeometry(QtCore.QRect(20, 40, 871, 441))
        self.tableWidget_5.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(10)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, item)
        self.tableWidget_5.raise_()
        self.pushButton_26.raise_()
        self.frame_12.raise_()
        self.stackedWidget.addWidget(self.produit_2)
        self.analyse_2 = QtWidgets.QWidget()
        self.analyse_2.setObjectName("analyse_2")
        self.widget_6 = QtWidgets.QWidget(self.analyse_2)
        self.widget_6.setGeometry(QtCore.QRect(50, 30, 191, 121))
        self.widget_6.setStyleSheet("border-radius:20px;\n"
"background-color:#CFE9C2;")
        self.widget_6.setObjectName("widget_6")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.label_2.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.label_3.setStyleSheet("font: 75 12pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setGeometry(QtCore.QRect(130, 20, 51, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icons/client.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.widget_7 = QtWidgets.QWidget(self.analyse_2)
        self.widget_7.setGeometry(QtCore.QRect(400, 30, 191, 121))
        self.widget_7.setStyleSheet("border-radius:20px;\n"
"background-color:#CFE9C2;")
        self.widget_7.setObjectName("widget_7")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_5.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.label_6.setStyleSheet("font: 75 12pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setGeometry(QtCore.QRect(130, 20, 51, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icons/icons8-fournisseur.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.widget_8 = QtWidgets.QWidget(self.analyse_2)
        self.widget_8.setGeometry(QtCore.QRect(750, 30, 191, 121))
        self.widget_8.setStyleSheet("border-radius:20px;\n"
"background-color: #CFE9C2;")
        self.widget_8.setObjectName("widget_8")
        self.label_8 = QtWidgets.QLabel(self.widget_8)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_8.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_8)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.label_9.setStyleSheet("font: 75 12pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_8)
        self.label_10.setGeometry(QtCore.QRect(130, 20, 51, 61))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("icons/icons8-produit.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.widget_9 = QtWidgets.QWidget(self.analyse_2)
        self.widget_9.setGeometry(QtCore.QRect(230, 280, 191, 121))
        self.widget_9.setStyleSheet("border-radius:20px;\n"
"background-color:#CFE9C2;")
        self.widget_9.setObjectName("widget_9")
        self.label_11 = QtWidgets.QLabel(self.widget_9)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_11.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_9)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.label_12.setStyleSheet("font: 75 12pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_9)
        self.label_13.setGeometry(QtCore.QRect(130, 20, 51, 61))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("icons/icons8-commande.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.widget_10 = QtWidgets.QWidget(self.analyse_2)
        self.widget_10.setGeometry(QtCore.QRect(590, 280, 191, 121))
        self.widget_10.setStyleSheet("border-radius:20px;\n"
"background-color:#CFE9C2;")
        self.widget_10.setObjectName("widget_10")
        self.label_20 = QtWidgets.QLabel(self.widget_10)
        self.label_20.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_20.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_10)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.label_21.setStyleSheet("font: 75 12pt \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.widget_10)
        self.label_22.setGeometry(QtCore.QRect(130, 20, 51, 61))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("icons/icons8-classer-par-catégories.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.analyse_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.main)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.widget_4)
        self.tableWidget_6.setGeometry(QtCore.QRect(70, 80, 371, 441))
        self.tableWidget_6.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(10)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, item)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 191, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 20, 41, 31))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setGeometry(QtCore.QRect(280, 30, 91, 22))
        self.comboBox.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.main)
        Principe.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principe)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Principe)

    def retranslateUi(self, Principe):
        _translate = QtCore.QCoreApplication.translate
        Principe.setWindowTitle(_translate("Principe", "Principe"))
        self.client.setText(_translate("Principe", "Client"))
        self.four.setText(_translate("Principe", "Fournisseur"))
        self.produit.setText(_translate("Principe", "Produit"))
        self.commande.setText(_translate("Principe", "Commande"))
        self.categorie.setText(_translate("Principe", "Categorie"))
        self.analyse.setText(_translate("Principe", "Analyse"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Principe", "ID/Client"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Principe", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Principe", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Principe", "Telephone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Principe", "Mail"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Principe", "Adresse"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Principe", "Date Naissance"))
        self.pushButton_6.setText(_translate("Principe", "Actualiser"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Principe", "ID/Categorie"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Principe", "Nom Categorie"))
        self.pushButton_25.setText(_translate("Principe", "Actualiser"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Principe", "ID/Commade"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Principe", "Date Commande"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Principe", "Nom Client"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Principe", "Produit"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Principe", "Quantité Produit"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("Principe", "Remise"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("Principe", "TVA"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("Principe", "Total HT"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("Principe", "Total TTC"))
        self.pushButton_17.setText(_translate("Principe", "Actualiser"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Principe", "Code/Fournisseur"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Principe", "NomFournisseur"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Principe", "VilleFournisseur"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Principe", "TelFournisseur"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("Principe", "EmailFournisseur"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("Principe", "AdresseFournisseur"))
        self.pushButton_21.setText(_translate("Principe", "Actualiser"))
        self.pushButton_26.setText(_translate("Principe", "Actualiser"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Principe", "ID/Produit"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Principe", "Nom"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("Principe", "Description"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("Principe", "Prix_unitaire"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("Principe", "Quantite"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("Principe", "Seuil_alerte_stock"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("Principe", "date_derniere_entree"))
        item = self.tableWidget_5.horizontalHeaderItem(7)
        item.setText(_translate("Principe", "date_derniere_sortie"))
        item = self.tableWidget_5.horizontalHeaderItem(8)
        item.setText(_translate("Principe", "Image"))
        item = self.tableWidget_5.horizontalHeaderItem(9)
        item.setText(_translate("Principe", "Categorie"))
        self.label_2.setText(_translate("Principe", "Client"))
        self.label_5.setText(_translate("Principe", "Fournisseur"))
        self.label_8.setText(_translate("Principe", "Produit"))
        self.label_11.setText(_translate("Principe", "Commande"))
        self.label_20.setText(_translate("Principe", "Categorie"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("Principe", "ID/Produit"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("Principe", "Nom"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("Principe", "Description"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("Principe", "Prix_unitaire"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("Principe", "Quantite"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("Principe", "Seuil_alerte_stock"))
        item = self.tableWidget_6.horizontalHeaderItem(6)
        item.setText(_translate("Principe", "date_derniere_entree"))
        item = self.tableWidget_6.horizontalHeaderItem(7)
        item.setText(_translate("Principe", "date_derniere_sortie"))
        item = self.tableWidget_6.horizontalHeaderItem(8)
        item.setText(_translate("Principe", "Image"))
        item = self.tableWidget_6.horizontalHeaderItem(9)
        item.setText(_translate("Principe", "Categorie"))
        self.pushButton_2.clicked.connect(lambda:Principe.close())
        self.pushButton_10.clicked.connect(lambda:Principe.close())
    

        
        self.produit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.produit_2))
        ##################
#############
        self.client.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.client_2))
        
        ##############
###############
        self.categorie.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.categorie_2))
        ##################
###########
        self.commande.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.commande_2))
        ############
############
        self.four.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.four_2))
        ##############
#############
        self.analyse.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.analyse_2))
        ##############
        self.pushButton.clicked.connect(self.mover_menu)
        ##################
##############
#recuperer le nom de l'utilisateure
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pfa"
                )
        cursor = conn.cursor()
        cursor.execute("SELECT nom_utilisateur FROM compte WHERE user_connecter = %s", ("oui",))
        result = cursor.fetchone()
        if result is not None:
                nom = result[0]
                self.label.setText(nom)
                cursor.execute("UPDATE compte SET user_connecter = %s WHERE nom_utilisateur = %s", 
                    ("non", nom))
                conn.commit()
                print(cursor.rowcount, "enregistrement ajouté avec succès.")
        else:
                print("Aucun résultat n'a été renvoyé par la requête SQL.")


#Analyse
       
#Analyse Client:        
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM client" 
        cursor.execute(sql)
        result = cursor.fetchone()
        self.label_3.setText(str(result[0]))
#Analyse Fornisseur: 
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM fornisseur" 
        cursor.execute(sql)
        result = cursor.fetchone()
        self.label_6.setText(str(result[0]))  
#Analyse Produits: 
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM produits" 
        cursor.execute(sql)
        result = cursor.fetchone()
        self.label_9.setText(str(result[0])) 
#Analyse Commands: 
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM details_commande" 
        cursor.execute(sql)
        result = cursor.fetchone()
        self.label_12.setText(str(result[0]))  
#Analyse Categories: 
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM categories" 
        cursor.execute(sql)
        result = cursor.fetchone()
        self.label_21.setText(str(result[0]))      


    # Ajout des données clients dans la table widget 
        self.AfficherClient()
        self.pushButton_6.clicked.connect(self.AfficherClient)
    def AfficherClient(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pfa"
                )
        cursor = conn.cursor()
        sql = "SELECT * FROM client" 
        cursor.execute(sql)
        result = cursor.fetchall()

        # Définir le nombre de lignes du tableau
        self.tableWidget.setRowCount(len(result))

        # Insérer les données dans chaque cellule
        for row_num, row_data in enumerate(result):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget.setItem(row_num, col_num, item)       
        ######

         # Ajout des données fornisseur dans la table widget 
        self.Afficherforni()
        self.pushButton_21.clicked.connect(self.Afficherforni)
    def Afficherforni(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pfa"
                )
        cursor = conn.cursor()
        sql = "SELECT * FROM fornisseur" 
        cursor.execute(sql)
        result = cursor.fetchall()

        # Définir le nombre de lignes du tableau
        self.tableWidget_4.setRowCount(len(result))

        # Insérer les données dans chaque cellule
        for row_num, row_data in enumerate(result):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_4.setItem(row_num, col_num, item)       
        ######

         # Ajout des données categories dans la table widget 
        self.AfficherCat()
        self.pushButton_25.clicked.connect(self.AfficherCat)
    def AfficherCat(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pfa"
                )
        cursor = conn.cursor()
        sql = "SELECT * FROM categories" 
        cursor.execute(sql)
        result = cursor.fetchall()

        # Définir le nombre de lignes du tableau
        self.tableWidget_2.setRowCount(len(result))

        # Insérer les données dans chaque cellule
        for row_num, row_data in enumerate(result):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_2.setItem(row_num, col_num, item)       
        ######
        # Ajout des données Commande dans la table widget 
        self.AfficherCmd()
        self.pushButton_17.clicked.connect(self.AfficherCmd)
    def AfficherCmd(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pfa"
                )
        cursor = conn.cursor()
        sql = "SELECT * FROM details_commande" 
        cursor.execute(sql)
        result = cursor.fetchall()

        # Définir le nombre de lignes du tableau
        self.tableWidget_3.setRowCount(len(result))

        # Insérer les données dans chaque cellule
        for row_num, row_data in enumerate(result):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_3.setItem(row_num, col_num, item)       
        ######




        #AFFICHER LES PRODUITS---------
        self.AfficherProduit()
        self.produit.clicked.connect(self.AfficherProduit) 
        self.pushButton_26.clicked.connect(self.AfficherProduit)
    def AfficherProduit(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pfa"
                )
        cursor = conn.cursor()
        sql = "SELECT * FROM produits" 
        cursor.execute(sql)
        result = cursor.fetchall()

        # Définir le nombre de lignes du tableau
        self.tableWidget_5.setRowCount(len(result))

        # Insérer les données dans chaque cellule
        
        
        self.tableWidget_5.clearContents()
        self.tableWidget_5.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_5.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 8:
                    pixmap=QPixmap(item)
                    icon = QIcon(pixmap)
                    TableItem = QTableWidgetItem()
                    TableItem.setIcon(icon)
                    self.tableWidget_5.setItem(row_number, column_number,TableItem)
                else:
                    qtablewidgetitem = QTableWidgetItem()
                    self.tableWidget_5.setItem(row_number, column_number, qtablewidgetitem)
                    qtablewidgetitem.setText(str(item))
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(80)
        #########-----------
        #REMPLIR COMBO et recherche
        number = self.comboBox.count()
        print(number)
        if(number == 0):
                self.comboBox.addItem("choisir")
                self.comboBox.addItem("nom")
                self.comboBox.addItem("prix_unitaire")
                self.comboBox.addItem("quantite")
                self.comboBox.addItem("date_entree")
                self.comboBox.addItem("categorie")
        self.lineEdit.setReadOnly(True)
        self.comboBox.currentIndexChanged.connect(self.active)
        self.pushButton_9.clicked.connect(self.rechercher_par_critere)
    def active(self):
                #Active les edit text:
                self.lineEdit.setReadOnly(False)
        

        

    


    def rechercher_par_critere(self):
            print("test")
            com = self.comboBox.currentText()
            text = self.lineEdit.text()
            print(com)
            print(text)
            cnx = mysql.connector.connect(user='root', password='', host='localhost',database='PFA')
            cursor = cnx.cursor()
            if com == 'nom':
                print("ja")
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE nom=%s")
                valeur_recherche = (text,)
            elif com == 'prix_unitaire':
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE prix_unitaire <= %s")
                valeur_recherche = (text,)
            elif com == 'quantite':
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE quantite_en_stock <= %s")
                valeur_recherche = (text,)
            elif com == 'date_entree':
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE date_derniere_entree_stock <= %s")
                valeur_recherche = (text,)
                #chercher avec categorie
            elif com == 'categorie':
                requete_produits = ("SELECT * FROM produits JOIN Categories "
                                    "WHERE produits.id_categorie = Categories.id_categorie AND nom_Cat=%s")
                valeur_recherche = (text,)
            else:
                return None
            cursor.execute(requete_produits, valeur_recherche)
            resultats = cursor.fetchall()
            if len(resultats) != 0:
                self.tableWidget_6.setRowCount(len(resultats))
                self.tableWidget_6.clearContents()
                self.tableWidget_6.setRowCount(0)
                for row_number, row_data in enumerate(resultats):
                    self.tableWidget_6.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        item = str(column_data)
                        if column_number == 8:
                            pixmap=QPixmap(item)
                            icon = QIcon(pixmap)
                            TableItem = QTableWidgetItem()
                            TableItem.setIcon(icon)
                            self.tableWidget_6.setItem(row_number, column_number,TableItem)
                        else:
                            qtablewidgetitem = QTableWidgetItem()
                            self.tableWidget_6.setItem(row_number, column_number, qtablewidgetitem)
                            qtablewidgetitem.setText(str(item))
                    self.tableWidget_6.verticalHeader().setDefaultSectionSize(80)  
                cnx.close()
            else:
                 # Création de la boîte de dialogue d'erreur
                 msg_box = QMessageBox()
                 msg_box.setIcon(QMessageBox.Critical)
                 msg_box.setText("Une erreur ce produits n'existe pas.")
                 msg_box.setWindowTitle("Erreur")

                 # Affichage de la boîte de dialogue
                 msg_box.exec()
                 self.tableWidget_6.clearContents()
        ######

        #Ajouter
    def showAjouterProduit(self):
        self.AjouterProduit = QtWidgets.QMainWindow()
        self.ui=Ui_AjouterProduit()
        self.ui.setupUi(self.AjouterProduit) 
        self.AjouterProduit.show()
    def showAjouterFournisseur(self):
        self.AjouterFournisseur = QtWidgets.QMainWindow()
        self.ui=Ui_AjouterFournisseur()
        self.ui.setupUi(self.AjouterFournisseur) 
        self.AjouterFournisseur.show()
    def showAjouterCommande(self):
        self.AjouterCommande = QtWidgets.QMainWindow()
        self.ui=Ui_AjouterCommande()
        self.ui.setupUi(self.AjouterCommande) 
        self.AjouterCommande.show()
    def showAjouterCategorie(self):
        self.AjouterCategorie = QtWidgets.QMainWindow()
        self.ui=Ui_AjouterCategorie()
        self.ui.setupUi(self.AjouterCategorie) 
        self.AjouterCategorie.show()
    def showAjouterCli(self):
        self.AjouterCli = QtWidgets.QMainWindow()
        self.ui=Ui_AjouterCli()
        self.ui.setupUi(self.AjouterCli) 
        self.AjouterCli.show()
        #Modifier
    def showModifierProduit(self):
        self.ModifierProduit = QtWidgets.QMainWindow()
        self.ui=Ui_ModifierProduit()
        self.ui.setupUi(self.ModifierProduit) 
        self.ModifierProduit.show()
    def showModifierCategorie(self):
        self.ModifierCategorie = QtWidgets.QMainWindow()
        self.ui=Ui_ModifierCategorie()
        self.ui.setupUi(self.ModifierCategorie) 
        self.ModifierCategorie.show()
    def showModifierClient(self):
        self.ModifierClient = QtWidgets.QMainWindow()
        self.ui=Ui_ModifierClient()
        self.ui.setupUi(self.ModifierClient) 
        self.ModifierClient.show()
    def showModifierCommande(self):
        self.ModifierCommande = QtWidgets.QMainWindow()
        self.ui=Ui_ModifierCommande()
        self.ui.setupUi(self.ModifierCommande) 
        self.ModifierCommande.show()
    def showModifierFournisseur(self):
        self.ModifierFournisseur = QtWidgets.QMainWindow()
        self.ui=Ui_ModifierFournisseur()
        self.ui.setupUi(self.ModifierFournisseur) 
        self.ModifierFournisseur.show()
        #Supprimer
    def showSupprimerProduit(self):
        self.SupprimerProduit = QtWidgets.QMainWindow()
        self.ui=Ui_SupprimerProduit()
        self.ui.setupUi(self.SupprimerProduit) 
        self.SupprimerProduit.show()
    def showSupprimerCategorie(self):
        self.SupprimerCategorie = QtWidgets.QMainWindow()
        self.ui=Ui_SupprimerCategorie()
        self.ui.setupUi(self.SupprimerCategorie) 
        self.SupprimerCategorie.show()
    def showSupprimerClient(self):
        self.SupprimerClient = QtWidgets.QMainWindow()
        self.ui=Ui_SupprimerClient()
        self.ui.setupUi(self.SupprimerClient) 
        self.SupprimerClient.show()
    def showSupprimerCommande(self):
        self.SupprimerCommande = QtWidgets.QMainWindow()
        self.ui=Ui_SupprimerCommande()
        self.ui.setupUi(self.SupprimerCommande) 
        self.SupprimerCommande.show()
    def showSupprimerFournisseur(self):
        self.SupprimerFournisseur = QtWidgets.QMainWindow()
        self.ui=Ui_SupprimerFournisseur()
        self.ui.setupUi(self.SupprimerFournisseur) 
        self.SupprimerFournisseur.show()




    def mover_menu(self):
            if True:			
                width = self.widget_4.width()
                normal = 500
                if width==500:
                        extender = 0
                else:
                        extender = normal
            self.animacion = QPropertyAnimation(self.widget_4, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_Principe()
     Principe = QtWidgets.QMainWindow()
     ui.setupUi(Principe)
     Principe.show()
     sys.exit(app.exec_())

