from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QFrame,QComboBox,QGridLayout,QTableWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys
from style import QSS

DROPDOWN = "Imagens/Vector_dropdown.png"

class popup_editar_ano(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(750,500)
        self.setWindowTitle("Editar ano")


        self.layout_vertical = QVBoxLayout()
        

        self.setLayout(self.layout_vertical)

        background_gaveta = QFrame()

        background_gaveta.setStyleSheet(QSS)

        background_gaveta.setObjectName("background_gaveta")

        self.layout_vertical.addWidget(background_gaveta)
        
        self.layout_gaveta = QHBoxLayout()  

        self.layout_gaveta_interna = QHBoxLayout()

        background_gaveta_branco = QComboBox()


        background_gaveta_branco.setLayout(self.layout_gaveta_interna)
 

        background_gaveta_branco.setStyleSheet(QSS)
        background_gaveta_branco.setObjectName("fundo_branco")
        self.layout_gaveta.addWidget(background_gaveta_branco)

        background_gaveta.setLayout(self.layout_gaveta)

        acoe = acoes()

        self.layout_vertical.addWidget(acoe)

        acoes_add = QLabel("Ações adicionadas o ano")

        self.layout_vertical.addWidget(acoes_add)
        
        self.layout_vertical.addStretch(1)
        


class acoes(QFrame):
    def __init__(self):
        super().__init__()
        self.layout_vertical = QVBoxLayout()
        self.setStyleSheet(QSS)
        self.setObjectName("aiai")
        self.layout_txt_acoes = QHBoxLayout()
        self.layout_acoes = QHBoxLayout()
        self.layout_vertical_organizador = QVBoxLayout()
        gaveta_acoes = QComboBox()
        gaveta_acoes.setObjectName("acoes")
        limite = QLineEdit()
        limite.setObjectName("input")
        peso = QLineEdit()
        peso.setObjectName("input")
        self.layout_acoes.addWidget(gaveta_acoes)
        self.layout_acoes.addWidget(limite)
        self.layout_acoes.addWidget(peso)
        txt_acoes = QLabel("Ações*")
        txt_limite = QLabel("Limite*")
        txt_peso = QLabel("Peso*")
        txt_acoes.setStyleSheet(QSS)
        txt_acoes.setObjectName("txt")
        self.layout_txt_acoes.addStretch(1)
        self.layout_txt_acoes.addWidget(txt_acoes)
        self.layout_txt_acoes.addWidget(txt_limite)
        self.layout_txt_acoes.addWidget(txt_peso)
        self.layout_vertical_organizador.addLayout(self.layout_txt_acoes)
        self.layout_vertical_organizador.addLayout(self.layout_acoes)
        self.setLayout(self.layout_vertical_organizador)
        self.layout_txt_acoes.addStretch(1)
        txt_acoes.setContentsMargins(0,0,180,0)
        txt_limite.setContentsMargins(0,0,180,0)
        txt_peso.setContentsMargins(0,0,0,0)


class tabela(QGridLayout):
    def __init__(self):
        super().__init__()

        

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = popup_editar_ano()
    janela.show()
    sys.exit(app.exec())