from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont

# Le nom d'utilisateur connecté
username = "JohnDoe"

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        # Crée un label pour afficher le nom de l'utilisateur
        self.username_label = QLabel(self)
        self.username_label.setFont(QFont('Arial', 16))
        self.username_label.move(50, 50)
        self.username_label.setText(f"Bonjour {username}!")

if __name__ == '__main__':
    app = QApplication([])
    home_page = HomePage()
    home_page.show()
    app.exec_()
