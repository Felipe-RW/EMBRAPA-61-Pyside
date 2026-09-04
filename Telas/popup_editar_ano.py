from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QFrame,QComboBox
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

        # ano = QLabel("2027")

        # icon = QLabel()
        # pixmap = QPixmap(DROPDOWN)
        # icon.setPixmap(pixmap)
        # icon.setStyleSheet(QSS)
        # icon.setObjectName("dropdown")
        # icon.setScaledContents(True)
        

        # self.layout_gaveta_interna.addWidget(ano,alignment=Qt.AlignmentFlag.AlignLeft)
        # self.layout_gaveta_interna.addWidget(icon,alignment=Qt.AlignmentFlag.AlignRight)

        background_gaveta_branco.setLayout(self.layout_gaveta_interna)



        background_gaveta_branco.setStyleSheet(QSS)
        background_gaveta_branco.setObjectName("fundo_branco")
        self.layout_gaveta.addWidget(background_gaveta_branco)

        background_gaveta.setLayout(self.layout_gaveta)

        acoe = acoes()

        self.layout_vertical.addWidget(acoe)
        
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
        limite = QLineEdit()
        peso = QLineEdit()
        self.layout_acoes.addWidget(gaveta_acoes)
        self.layout_acoes.addWidget(limite)
        self.layout_acoes.addWidget(peso)
        txt_acoes = QLabel("Ações*")
        txt_limite = QLabel("Limite*")
        txt_peso = QLabel("Peso*")
        self.layout_txt_acoes.addWidget(txt_acoes)
        self.layout_txt_acoes.addWidget(txt_limite)
        self.layout_txt_acoes.addWidget(txt_peso)
        self.layout_vertical_organizador.addLayout(self.layout_txt_acoes)
        self.layout_vertical_organizador.addLayout(self.layout_acoes)
        self.setLayout(self.layout_vertical_organizador)
       

        txt_acoes_adicionadas = QLabel("Ações adicionadas para o ano")

        self.layout_vertical.addWidget(txt_acoes_adicionadas)


        self.layout_vertical.addStretch(1)

        

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = popup_editar_ano()
    janela.show()
    sys.exit(app.exec())