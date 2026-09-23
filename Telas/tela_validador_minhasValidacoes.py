import sys, os

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QMainWindow, QTableWidget,
    QGridLayout, QTableWidgetItem, QAbstractItemView, QSizePolicy, QHeaderView
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")
EXCEL = os.path.join(BASE, "Imagens", "icone_excel.png")
PESQUISA = os.path.join(BASE, "Imagens", "icone_pesquisa.svg")
APROVADO = os.path.join(BASE, "Imagens", "icone_aprovado.svg")
BUSCA = os.path.join(BASE, "Imagens", "icone_busca.svg")
REPROVADO = os.path.join(BASE, "Imagens", "icone_reprovado.svg")
SETA = os.path.join(BASE, "Imagens", "sinalSetaBaixo.png")


class Tabela(QWidget):
    """
    Cabeçalho (QGridLayout com labels) + QTableWidget com os dados,
    usados dentro do painel expansível de cada CardStatus.
    """

    def __init__(self, pesquisas, parent=None):
        super().__init__(parent)

        self.pesquisas = pesquisas

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(0 , 0 , 0 , 0)
        layout_principal.setSpacing(0)

        # --- Cabeçalho (labels em grid) ---
        self.cab_frame  = QFrame()
        self.cab_frame.setObjectName("cabFrame")
        self.cab_frame.setFixedHeight(50)
        self.cab_frame.setStyleSheet("""
                QFrame#cabFrame {
                background:#EAF1FA;
                border:none;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                }
        """)

        cabecalho = QHBoxLayout(self.cab_frame)
        cabecalho.setContentsMargins(25 , 0 , 25 , 0)
        cabecalho.setSpacing(0)
        titulos = [
            ("Pesquisador") , ("Título da Pesquisa") , ("Tipo") ,
            ("Data")
        ]
        for texto in titulos:
            label = QLabel(texto)
            # label.setFixedWidth(largura)
            label.setStyleSheet("""
                color: #00409A;
                font-size: 15px;
                font-weight:bold;
                background: transparent;
                border: none;
            """)
            cabecalho.addWidget(label, stretch=1)

        # cabecalho.addStretch()

        layout_principal.addWidget(self.cab_frame)

        # --- Tabela de dados ---
        self.tab = QTableWidget()
        self.tab.setColumnCount(4)
        self.tab.setRowCount(len(pesquisas))

        for linha, (pesquisador, titulo, tipo, data) in enumerate(pesquisas):
            self.tab.setItem(linha, 0, QTableWidgetItem(pesquisador))
            self.tab.setItem(linha, 1, QTableWidgetItem(titulo))
            self.tab.setItem(linha, 2, QTableWidgetItem(tipo))
            self.tab.setItem(linha, 3, QTableWidgetItem(data))
            # self.tab.setCellWidget(linha, 4, self.criar_botao())

        self.tab.horizontalHeader().setVisible(False)
        self.tab.verticalHeader().setVisible(False)
        self.tab.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tab.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tab.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tab.setShowGrid(False)

        self.tab.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tab.setStyleSheet("""
            QTableWidget {
                border:none;
                border-top: 2px solid gray;
                border-left: 2px solid gray;
                border-right: 2px solid gray;
                border-bottom 2px solid gray;
                alternate-background-color:#EAF1FA;
                font-size:16px;
                font-weight:normal;
                gridline-color:;
            }
        """)
        self.tab.setAlternatingRowColors(True)

        self.tab.resizeRowsToContents()

        altura_linhas = sum(
            self.tab.rowHeight(i) for i in range (self.tab.rowCount())
        )

        self.tab.setFixedHeight(altura_linhas + 2)
        self.tab.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout_principal.addWidget(self.tab)
        
        # self.tab.setColumnWidth(0, 260)
        # self.tab.setColumnWidth(1, 260)
        # self.tab.setColumnWidth(2, 260)
        # self.tab.setColumnWidth(3, 200)
        # self.tab.setColumnWidth(4, 120)


    # def criar_botao(self):
    #     btn = QPushButton("Ver")
    #     btn.setStyleSheet("""
    #         QPushButton {
    #             background:#356394;
    #             color:white;
    #             border:none;
    #             border-radius:6px;
    #             font-size:14px;
    #             padding:4px 10px;
    #         }
    #         QPushButton:hover { background:#2a4f79; }
    #     """)
    #     return btn


class CardStatus(QFrame):
    """
    Card de resumo (Análise / Aprovadas / Negadas) que expande,
    ao clicar na seta, revelando a lista de pesquisas daquele status.
    """

    def __init__(self, texto, fundo, cor, icone, pesquisas, parent=None):
        super().__init__(parent)

        self.expandido = False
        self.pesquisas = pesquisas

        self.setStyleSheet("QFrame { background:transparent; border:none; }")

        layout_geral = QVBoxLayout(self)
        layout_geral.setContentsMargins(0, 0, 0, 0)
        layout_geral.setSpacing(20)

        # --- Cabeçalho do card (igual ao visual original) ---
        self.topo = QFrame(self)
        self.topo.setFixedHeight(116)
        self.topo.setStyleSheet("""
            QFrame {
                background:white;
                border:2px solid #d0d0d0;
                border-radius:10px;
            }
        """)

        circulo = QLabel(self.topo)
        circulo.setGeometry(18, 13, 84, 84)
        circulo.setStyleSheet(
            f"background:{fundo}; border:none; border-radius:42px;"
        )

        simbolo = QLabel(circulo)
        simbolo.setGeometry(18, 18, 48, 48)
        simbolo.setPixmap(QIcon(icone).pixmap(QSize(48, 48)))
        simbolo.setScaledContents(True)

        grupo = QWidget(self.topo)
        grupo.setGeometry(130, 29, 900, 55)
        grupo.setStyleSheet("background:transparent;")

        linha = QHBoxLayout(grupo)
        linha.setContentsMargins(0, 0, 0, 0)
        linha.setSpacing(8)

        fonte = QFont("Verdana", 32)
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

        quantidade = QLabel(str(len(pesquisas)))
        quantidade.setFixedSize(40, 35)
        quantidade.setAlignment(Qt.AlignCenter)
        quantidade.setStyleSheet(
            f"background:{fundo}; color:{cor}; border:none;"
            "border-radius:15px; font-size:18px; font-weight:bold;"
        )

        linha.addWidget(nome)
        linha.addWidget(quantidade)
        linha.addStretch()

        self.seta_btn = QPushButton(self.topo)
        self.seta_btn.setGeometry(1300, 35, 35, 35)
        self.seta_btn.setIcon(QIcon(SETA))
        self.seta_btn.setIconSize(QSize(20, 20))
        self.seta_btn.setStyleSheet("border:none; background:transparent;")
        self.seta_btn.setCursor(Qt.PointingHandCursor)
        self.seta_btn.clicked.connect(self.alternar)

        layout_geral.addWidget(self.topo)

        # --- Painel expansível com a Tabela ---
        self.painel = QFrame(self)
        self.painel.setObjectName("painelFrame")
        self.painel.setVisible(False)
        self.painel.setStyleSheet("""
            QFrame#painelFrame {
                background:white;
                border:2px solid #d0d0d0;
                border-bottom: 2px solid gray;
                border-radius:10px;
            }
        """)

        painel_layout = QVBoxLayout(self.painel)
        painel_layout.setContentsMargins(0, 0, 0, 0)

        self.tabela = Tabela(pesquisas, self.painel)
        painel_layout.addWidget(self.tabela)

        layout_geral.addWidget(self.painel)

    def alternar(self):
        self.expandido = not self.expandido
        self.painel.setVisible(self.expandido)


class ModeloTelaValidador(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Validações")
        self.setFixedSize(1920, 1080)

        self.setStyleSheet("""
            QWidget {
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        self.criar_pagina()

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
                # border-bottom: 20px;
                # border-top: 20px;
                # border-top-left-radius:20px;
                # border-top-right-radius:20px;
            }
        """)

        self.criar_titulo()
        self.criar_excel()
        self.criar_pesquisa()
        self.criar_cards()

    def criar_titulo(self):
        titulo = QLabel("Validações", self.paginaprincipal)
        titulo.setGeometry(650, 15, 300, 55)
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
        excel = QPushButton("Baixar em Excel", self.paginaprincipal)
        excel.setGeometry(113, 108, 225, 50)
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
            QPushButton:hover { background:#f5f5f5; }
        """)

    def criar_pesquisa(self):
        pesquisa = QLineEdit(self.paginaprincipal)
        pesquisa.setGeometry(1127, 108, 360, 50)
        pesquisa.setPlaceholderText("Pesquise...")
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
            QLineEdit:focus { border:2px solid #356394; }
        """)

        busca = QLabel(self.paginaprincipal)
        busca.setGeometry(1442, 118, 30, 30)
        busca.setPixmap(QPixmap(PESQUISA))
        busca.setScaledContents(True)

    def criar_cards(self):
        container = QWidget(self.paginaprincipal)
        container.setGeometry(113, 180, 1374, 820)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(25)

        pesquisas_analise = [
            ("Mateus Freitas", "Gado", "Artigo Científico", "29/03/2026"),
            ("Felipe Wrubell", "Soja", "Artigo Científico", "22/04/2026"),
            ("Arthur Ferraz", "Pasto", "Artigo Científico", "20/05/2026"),
            ("Nathália Fialho", "Plantação", "Artigo Científico", "17/06/2026"),
            ("Enzo Lima", "Clima", "Artigo Científico", "23/07/2026"),
        ]

        pesquisas_aprovadas = [
            ("Carla Souza", "Milho", "Artigo Científico", "10/02/2026"),
            ("João Pedro", "Irrigação", "Artigo Científico", "15/03/2026"),
        ]

        pesquisas_negadas = [
            ("Bruna Lopes", "Pragas", "Artigo Científico", "05/01/2026"),
            ("Bruna Lopes", "Pragas", "Artigo Científico", "05/01/2026"),
            ("Bruna Lopes", "Pragas", "Artigo Científico", "05/01/2026"),
            ("Bruna Lopes", "Pragas", "Artigo Científico", "05/01/2026"),
        ]

        card_analise = CardStatus(
            "Pesquisas em Análise", "#FFF2C7", "#F0B900", BUSCA, pesquisas_analise
        )
        card_aprovadas = CardStatus(
            "Pesquisas Aprovadas", "#D5F8DB", "#00A52A", APROVADO, pesquisas_aprovadas
        )
        card_negadas = CardStatus(
            "Pesquisas Negadas", "#FFD1D1", "#D60000", REPROVADO, pesquisas_negadas
        )

        layout.addWidget(card_analise)
        layout.addWidget(card_aprovadas)
        layout.addWidget(card_negadas)
        layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaValidador()
    window.show()
    sys.exit(app.exec())