import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView,QMainWindow, QButtonGroup,
    QScrollArea, QSizePolicy
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

class ModeloTelaAdministradorCalendario(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1600)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setContentsMargins(0, 0, 40, 0)
        self.setStyleSheet("""
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
        """)

        painel_layout = QVBoxLayout(self)
        painel_layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel ("Testando", self)
        painel_layout.addWidget(label)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ModeloTelaAdministradorCalendario()
#     window.showMaximized()
#     sys.exit(app.exec())