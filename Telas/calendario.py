import sys

from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter, QPen, QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFrame, QSizePolicy
)

BOTAO_EDITAR = "#2f5fa8"
BOTAO_MUDANCA = "#8EA5C2" #Essa cor muda o botão quando o mouse passa por cima.
BORDA = "#cfd8e8" 
TEXTO = "#1f2430"
INTERRUPTORES_DESLIGADOS = "#c9cfd8" 

icone_calendario = "Imagens/calendario.png"

#sem funcionalidade
class Interruptor(QFrame):
    def __init__(self, pai=None):
        super().__init__(pai)
        self.setFixedSize(34, 18)
        self.setStyleSheet(f"""
            background-color: {INTERRUPTORES_DESLIGADOS};
            border-radius: 9px;
        """)

        bolinha = QLabel(self)
        bolinha.setFixedSize(14, 14)
        bolinha.setStyleSheet("background-color: white; border-radius: 7px;")
        bolinha.move(self.width() - 14 - 2, 2)


#classe do card de cada ano
class CartaoAno(QFrame):
    def __init__(self, ano, pai=None):
        super().__init__(pai)
        self.setObjectName("cartao")
        self.setFixedWidth(220)
        self.setStyleSheet(f"""
            #cartao {{
                background: white;
                border: 1px solid {BORDA};
                border-radius: 12px;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(0)

        linha_superior = QHBoxLayout()
        fracao = QLabel("0/0")
        fracao.setStyleSheet(f"font-style: italic; font-size: 14px; color: {TEXTO};")
        linha_superior.addWidget(fracao)
        linha_superior.addStretch()
        linha_superior.addWidget(Interruptor())
        layout.addLayout(linha_superior)

        layout.addSpacing(6)

        linha_icone = QHBoxLayout()
        linha_icone.addStretch()

        rotulo_icone = QLabel()
        imagem_icone = QPixmap(icone_calendario)
        rotulo_icone.setPixmap(
        imagem_icone.scaled(56, 56, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        linha_icone.addWidget(rotulo_icone)

        linha_icone.addStretch()
        layout.addLayout(linha_icone)

        layout.addSpacing(10)

        rotulo_ano = QLabel(str(ano))
        rotulo_ano.setAlignment(Qt.AlignCenter)
        fonte_ano = QFont()
        fonte_ano.setPointSize(14)
        fonte_ano.setBold(True)
        rotulo_ano.setFont(fonte_ano)
        rotulo_ano.setStyleSheet(f"color: {TEXTO};")
        layout.addWidget(rotulo_ano)

        layout.addSpacing(16)

        botao_editar = QPushButton("Editar")
        botao_editar.setCursor(Qt.PointingHandCursor)
        botao_editar.setStyleSheet(f"""
            QPushButton {{
                background: {BOTAO_EDITAR};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 0;
                font-size: 13px;
            }}
            QPushButton:hover {{
                background: {BOTAO_MUDANCA};
            }}
        """)
        layout.addWidget(botao_editar)


#classe da tela principal com o cabecalho com título e o grid de cards dos anos
class TelaCalendario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendário")
        self.setStyleSheet("background: white;")

        layout_externo = QVBoxLayout(self)
        layout_externo.setContentsMargins(40, 32, 40, 32) #Define as margens internas
        layout_externo.setSpacing(28)

        fonte_titulo = QFont()
        fonte_titulo.setPointSize(17)
        fonte_titulo.setBold(True)

        titulo = QLabel("Calendário")
        titulo.setFont(fonte_titulo)
        titulo.setAlignment(Qt.AlignCenter)

        botao_criar = QPushButton("+  Criar ano")
        botao_criar.setCursor(Qt.PointingHandCursor)
        botao_criar.setStyleSheet(f"""
            QPushButton {{
                background: {BOTAO_EDITAR};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
            }}
            QPushButton:hover {{
                background: {BOTAO_MUDANCA};
            }}
        """)

        grade_cabecalho = QGridLayout()
        grade_cabecalho.addWidget(QLabel(""), 0, 0)
        grade_cabecalho.addWidget(titulo, 0, 1)
        grade_cabecalho.addWidget(botao_criar, 0, 2, alignment=Qt.AlignRight)
        grade_cabecalho.setColumnStretch(0, 1)
        grade_cabecalho.setColumnStretch(1, 1)
        grade_cabecalho.setColumnStretch(2, 1)
        layout_externo.addLayout(grade_cabecalho)

        anos = [2025, 2026, 2027, 2028, 2029, 2030]
        grade = QGridLayout()
        grade.setHorizontalSpacing(24)
        grade.setVerticalSpacing(24)

        colunas = 4
        for indice, ano in enumerate(anos): #o for é um laço, ele serve pra posicionar de forma automatica os anos na tela
            linha = indice // colunas #esse % e // serve pra organizar os itens em linha e coluna de uma forma automatica
            coluna = indice % colunas
            grade.addWidget(CartaoAno(ano), linha, coluna, alignment=Qt.AlignTop)

        container_grade = QHBoxLayout()
        container_grade.addLayout(grade)
        container_grade.addStretch()
        layout_externo.addLayout(container_grade)

        layout_externo.addStretch()


if __name__ == "__main__":
    aplicativo = QApplication(sys.argv)
    janela = TelaCalendario()
    janela.resize(1040, 620)
    janela.show()
    sys.exit(aplicativo.exec())
