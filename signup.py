from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Signup)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 60, 591, 341))
        self.widget.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.widget.setObjectName("widget")
        Signup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Signup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Signup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Signup)
        self.statusbar.setObjectName("statusbar")
        Signup.setStatusBar(self.statusbar)

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Signup"))
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui=Ui_Signup()
     Signup = QtWidgets.QMainWindow()
     ui.setupUi(Signup)
     Signup.show()
     sys.exit(app.exec_())
