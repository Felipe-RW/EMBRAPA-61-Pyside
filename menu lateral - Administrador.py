import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFrame, QLineEdit, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

BASE = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens/Embrapa-Logo.jpg")

class menu_administrador (QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)

        menu = QWidget()
        self.setCentralWidget(menu)

        main_layout = QHBoxLayout(menu)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.menu_lateral = QFrame()
        self.menu_lateral.setObjectName("Menu Lateral")
        self.menu_lateral.setFixedWidth(280)
        self.menu_lateral.setStyleSheet("background-color: #356394;")

        menu_lateral_layout = QVBoxLayout(self.menu_lateral)
        self.btn_home = QPushButton ("Início")
        self.btn_calendario = QPushButton ("Calendário")
        self.btn_acoes = QPushButton ("Ações")
        self.btn_empregados = QPushButton ("Empregados")
        self.btn_validadores = QPushButton ("Validadores")

        logo_label = QLabel (self)
        logo = QPixmap ("Imagens/Embrapa-Logo.jpg")
        logo_certa = logo.scaled (221, 86, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap (logo_certa)
        logo_label.setAlignment (Qt.AlignCenter)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.addWidget(self.btn_calendario)
        menu_lateral_layout.addWidget(self.btn_acoes)
        menu_lateral_layout.addWidget(self.btn_empregados)
        menu_lateral_layout.addWidget(self.btn_validadores)

        for btn in [self.btn_home, self.btn_calendario, self.btn_acoes, self.btn_empregados, self.btn_validadores]:
            btn.setStyleSheet("color: white; text-align: center; padding: 10px; border: none; font-weight: bold; font-family: 'Verdana'; font-size: 20px;")
        
        menu_lateral_layout.addStretch()

        main_layout.addWidget(self.menu_lateral)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = menu_administrador()
    janela.show()
    sys.exit(app.exec())