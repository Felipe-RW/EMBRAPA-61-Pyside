import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel

class tela_acoes (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle ("Tela de Ações")
        self.resize (800, 600)