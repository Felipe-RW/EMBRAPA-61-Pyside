import sys, os

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QMainWindow, QButtonGroup
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from Utilitarios.btn_layout import btn_layout

LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")
EXCEL = os.path.join(BASE, "Imagens", "icone_excel.png")
PESQUISA = os.path.join(BASE, "Imagens", "icone_pesquisa.png")
APROVADO = os.path.join(BASE, "Imagens", "icone_aprovado.svg")
BUSCA = os.path.join(BASE, "Imagens", "icone_busca.svg")
REPROVADO = os.path.join(BASE, "Imagens", "icone_reprovado.svg")
SETA = os.path.join(BASE, "Imagens", "sinalSetaBaixo.png")


class ModeloTelaValidador(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Validações")
        self.setFixedSize(1920, 1080)

        self.setStyleSheet("""
            QWidget {
                font-family: Verdana;
                font-weight: bold;
                background-color: #356394;
            }
        """)

        self.criar_menu()
        self.criar_cabecalho()
        self.criar_pagina()

    def criar_menu(self):
        menu = QWidget(self)
        menu.setGeometry(0, 0, 280, 1080)

        layout = QVBoxLayout(menu)
        layout.setContentsMargins(30, 0, 0, 0)
        layout.setSpacing(5)

        logo = QLabel()
        logo.setPixmap(QPixmap(LOGO).scaled(
            220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
        layout.addWidget(logo)

        self.btn_home = btn_layout(
            os.path.join(BASE, "Imagens", "Painel-Principal-Icone.png"),
            "Painel Principal"
        )

        self.btn_acoes = btn_layout(
            os.path.join(BASE, "Imagens", "Validações-Icone.png"),
            "Validações"
        )

        layout.addWidget(self.btn_home)
        layout.addWidget(self.btn_acoes)
        layout.addStretch()

        grupo = QButtonGroup(self)
        grupo.setExclusive(True)
        grupo.addButton(self.btn_home)
        grupo.addButton(self.btn_acoes)

    def criar_cabecalho(self):
        cab = QWidget(self)
        cab.setGeometry(280, 0, 1640, 70)

        self.criar_texto(
            "Fulano da Silva Rodrigues", 35, 400, 24, cab
        )

        self.criar_texto("|", 420, 5, 24, cab)

        self.criar_texto(
            "Validador", 470, 200, 24, cab
        )

        titulo = self.criar_texto(
            "Validações", 1000, 300, 20, cab
        )

        titulo.setStyleSheet("""
            color:white;
            background:transparent;
            font-size:20px;
            font-weight:normal;
        """)

        logout = QPushButton("Logout", cab)
        logout.setGeometry(1450, 15, 150, 40)

        logout.setStyleSheet("""
            QPushButton {
                background:white;
                color:#08175C;
                font-size:18px;
                border:none;
                border-radius:20px;
            }

            QPushButton:hover {
                background:#eeeeee;
            }
        """)

    def criar_texto(self, texto, x, largura, tamanho, pai):
        label = QLabel(texto, pai)

        label.setGeometry(x, 22, largura, 30)

        label.setStyleSheet(
            f"color:white;"
            f"background:transparent;"
            f"font-size:{tamanho}px;"
        )

        return label

    def criar_pagina(self):
        self.paginaprincipal = QFrame(self)

        self.paginaprincipal.setGeometry(
            280, 70, 1600, 1010
        )

        self.paginaprincipal.setStyleSheet("""
            QFrame {
                background:white;
                border-top-left-radius:20px;
                border-top-right-radius:20px;
            }
        """)

        self.criar_titulo()
        self.criar_excel()
        self.criar_pesquisa()
        self.criar_cards()

    def criar_titulo(self):
        titulo = QLabel(
            "Validações",
            self.paginaprincipal
        )

        titulo.setGeometry(
            650, 15, 300, 55
        )

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            QLabel {
                background:transparent;
                color:#000;
                font-size:36px;
                font-weight:bold;
            }
        """)

    def criar_excel(self):
        excel = QPushButton(
            "Baixar em Excel",
            self.paginaprincipal
        )

        excel.setGeometry(
            65, 108, 225, 50
        )

        excel.setIcon(QIcon(EXCEL))
        excel.setIconSize(QSize(28, 28))

        excel.setStyleSheet("""
            QPushButton {
                background:white;
                color:#16458A;
                border:2px solid #c7c7c7;
                border-radius:10px;
                font-size:18px;
                text-align:left;
                padding-left:20px;
            }

            QPushButton:hover {
                background:#f5f5f5;
            }
        """)

    def criar_pesquisa(self):
        pesquisa = QLineEdit(
            self.paginaprincipal
        )

        pesquisa.setGeometry(
            1080, 108, 360, 50
        )

        pesquisa.setPlaceholderText(
            "Pesquise..."
        )

        pesquisa.setStyleSheet("""
            QLineEdit {
                background:white;
                color:#000;
                border:1px solid #888;
                border-radius:10px;
                padding-left:12px;
                padding-right:45px;
                font-size:18px;
                font-weight:normal;
            }

            QLineEdit:focus {
                border:2px solid #356394;
            }
        """)

        busca = QLabel(
            self.paginaprincipal
        )

        busca.setGeometry(
            1395, 118, 30, 30
        )

        busca.setPixmap(
            QPixmap(PESQUISA)
        )

        busca.setScaledContents(True)

    def criar_cards(self):
        self.criar_card(
            175,
            "Pesquisas em Análise",
            5,
            "#FFF2C7",
            "#F0B900",
            BUSCA
        )

        self.criar_card(
            320,
            "Pesquisas Aprovadas",
            5,
            "#D5F8DB",
            "#00A52A",
            APROVADO
        )

        self.criar_card(
            465,
            "Pesquisas Negadas",
            5,
            "#FFD1D1",
            "#D60000",
            REPROVADO
        )

    def criar_card(
        self,
        y,
        texto,
        numero,
        fundo,
        cor,
        icone
    ):
        card = QFrame(
            self.paginaprincipal
        )

        card.setGeometry(
            65, y, 1375, 118
        )

        card.setStyleSheet("""
            QFrame {
                background:white;
                border:2px solid #d0d0d0;
                border-radius:10px;
            }
        """)

        circulo = QLabel(card)

        circulo.setGeometry(
            18, 13, 84, 84
        )

        circulo.setStyleSheet(
            f"background:{fundo};"
            "border:none;"
            "border-radius:42px;"
        )

        simbolo = QLabel(circulo)

        simbolo.setGeometry(
            18, 18, 48, 48
        )

        simbolo.setPixmap(
            QIcon(icone).pixmap(
                QSize(48, 48)
            )
        )

        simbolo.setScaledContents(True)

        grupo = QWidget(card)

        grupo.setGeometry(
            130, 29, 900, 55
        )

        grupo.setStyleSheet(
            "background:transparent;"
        )

        linha = QHBoxLayout(grupo)

        linha.setContentsMargins(
            0, 0, 0, 0
        )

        linha.setSpacing(8)

        fonte = QFont(
            "Verdana",
            32
        )

        fonte.setBold(True)

        nome = QLabel(texto)

        nome.setFont(fonte)

        nome.setStyleSheet("""
            QLabel {
                background:transparent;
                color:#000;
                border:none;
                font-size:32px;
                font-weight:bold;
            }
        """)

        quantidade = QLabel(
            str(numero)
        )

        quantidade.setFixedSize(
            40, 35
        )

        quantidade.setAlignment(
            Qt.AlignCenter
        )

        quantidade.setStyleSheet(
            f"background:{fundo};"
            f"color:{cor};"
            "border:none;"
            "border-radius:15px;"
            "font-size:18px;"
            "font-weight:bold;"
        )

        linha.addWidget(nome)
        linha.addWidget(quantidade)
        linha.addStretch()

        seta = QLabel(card)

        seta.setGeometry(
            1300, 35, 35, 35
        )

        seta.setPixmap(
            QPixmap(SETA)
        )

        seta.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ModeloTelaValidador()

    window.show()

    sys.exit(app.exec())