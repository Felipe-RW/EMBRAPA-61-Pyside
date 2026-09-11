import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QFont, QIcon, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView,QMainWindow, QButtonGroup,
    QHeaderView, QTableWidget, QTableWidgetItem
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

class ModeloTelaPesquisador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar ação")
        self.setMinimumSize(1920, 1080)
        
        self.setStyleSheet("""
            QWidget {
                font-family: 'Verdana';
                font-weight: bold;
                background-color: #356394;
            }
        """)

        menu_lateral = QWidget(self)
        menu_lateral.setGeometry(0, 0, 280, 1080)
        menu_lateral.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)

        self.btn_home = btn_layout (os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_acoes = btn_layout (os.path.join(BASE, "Imagens/Ações-Icone.png"), "Minhas Ações")

        logo_label = QLabel ()
        logo = QPixmap (LOGO)
        logo_certa = logo.scaled (220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap (logo_certa)
        logo_label.setAlignment (Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_acoes)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_acoes)
        
        menu_lateral_layout.addStretch()

        cabecalho = QWidget(self)
        cabecalho.setGeometry(280, 0, 1640, 70)
        cabecalho.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        nome_empregado = QLabel("Fulano da Silva Rodrigues", cabecalho)
        nome_empregado.setGeometry(35, 22, 400, 30)
        nome_empregado.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }
        """)

        separador = QLabel("|", cabecalho)
        separador.setGeometry(420, 22, 5, 30)
        separador.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }

        """)

        funcao_empregado = QLabel("Pesquisador", cabecalho)
        funcao_empregado.setGeometry(470, 22, 200, 30)
        funcao_empregado.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 24px
            }

        """)

        nome_tela = QLabel("Nome da Tela", cabecalho)
        nome_tela.setGeometry(1000, 22, 300, 30)
        nome_tela.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter
            }

        """)

        botao_logout = QPushButton("Logout", cabecalho)
        botao_logout.setGeometry(1450, 15, 150, 40)
        botao_logout.setStyleSheet("""
            QPushButton{
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }
        """)



        paginaprincipal = QFrame(self)
        paginaprincipal.setGeometry(280, 70, 1600, 1010)
        paginaprincipal.setStyleSheet("""
            QFrame{
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px
            }
        """)

        janela = QWidget(paginaprincipal)
        janela.setObjectName("janela_de_acoes")
        janela.setGeometry(0, 0, 1640, 1010)
        janela.setStyleSheet("background-color: transparent;")

        layout_principal = QVBoxLayout(janela)
        layout_principal.setContentsMargins(30, 30, 30, 80)

        self.conteudo = QFrame()
        self.conteudo.setObjectName("conteudo")

        layout_conteudo = QVBoxLayout(self.conteudo)
        layout_conteudo.setContentsMargins(28, 24, 28, 22)
        layout_conteudo.setSpacing(0)

        layout_principal.addWidget(self.conteudo)

        barra_nav = QHBoxLayout()
        barra_nav.setContentsMargins(0, 0, 0, 20)

        titulo = QLabel("Minhas Ações")

        fonte_titulo = QFont("Verdana", 24)
        fonte_titulo.setBold(True)

        titulo.setFont(fonte_titulo)
        titulo.setStyleSheet("color: black;")
        titulo.setAlignment(Qt.AlignCenter)

        barra_nav.addStretch()
        barra_nav.addWidget(titulo)
        barra_nav.addStretch()

        botao_excel = QPushButton("  Baixar em Excel ")
        botao_excel.setFixedSize(230, 45)

        botao_excel_icone = QIcon ("Imagens/Excel-Icone.png")
        botao_excel.setIcon (botao_excel_icone)

        botao_excel.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #9AB7D9;
                border-radius: 9px;
                color: #174EA6;
                font-size: 18px;
                font-weight: bold;
                padding-left: 8px;
            }

            QPushButton:hover {
                background-color: #F1F6FC;
            }
        """)

        barra_nav.addWidget(botao_excel)
        barra_nav.addSpacing(12)

        ano = QComboBox()

        ano.addItems([
            "2026",
            "2025",
            "2024",
            "2023",
            "2022"
        ])

        ano.setCurrentText("2026")
        ano.setFixedSize(105, 45)

        ano.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #9AB7D9;
                border-radius: 9px;
                padding-left: 16px;
                color: #174EA6;
                font-size: 18px;
                font-weight: bold;
            }

            QComboBox::drop-down {
                border: none;
                width: 30px;
            }

            QComboBox QAbstractItemView {
                background-color: white;
                border: 1px solid #9AB7D9;
                selection-background-color: #EAF2FF;
                selection-color: #174EA6;
            }
        """)

        barra_nav.addWidget(ano)

        layout_conteudo.addLayout(barra_nav)

        barra_filtro = QHBoxLayout()
        barra_filtro.setContentsMargins(0, 0, 0, 20)

        self.botao_novo = QPushButton(" Nova Ação")
        self.botao_novo.setFixedSize(165, 42)

        self.botao_novo_icone = QIcon ("Imagens/icone_nova_acao.png")
        self.botao_novo.setIcon (self.botao_novo_icone)

        botao_excel = QPushButton("  Baixar em Excel ")
        botao_excel.setFixedSize(230, 45)
        
        botao_excel_icone = QIcon ("Imagens/Excel-Icone.png")
        botao_excel.setIcon (botao_excel_icone)

        self.botao_novo.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                border: none;
                border-radius: 9px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #099440;
            }
        """)

        barra_filtro.addWidget(self.botao_novo)
        barra_filtro.addStretch()

        pesquisa = QLineEdit()
        pesquisa.setPlaceholderText("Pesquisar...")
        pesquisa.setFixedSize(250, 42)

        pesquisa.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #9AB7D9;
                border-radius: 9px;
                padding-left: 14px;
                padding-right: 35px;
                color: #B3B3B3;
                font-size: 18px;
            }

            QLineEdit:focus {
                border: 1px solid #1677E8;
            }
        """)

        filtro = QComboBox()
        filtro.setPlaceholderText ("Filtrar")
        filtro.setCurrentIndex (-1)
        filtro.addItems([
            "Aprovado",
            "Recusado",
            "Análise",
        ])

        filtro.setFixedSize(125, 45)
        
        filtro.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #9AB7D9;
                border-radius: 9px;
                padding-left: 16px;
                color: #686868;
                font-family: Verdana;
                font-size: 18px;
            }
        
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
        
            QComboBox QAbstractItemView {
                background-color: white;
                border: 1px solid #9AB7D9;
                selection-background-color: #EAF2FF;
                selection-color: #174EA6;
            }
        """)

        barra_filtro.addWidget(pesquisa)
        barra_filtro.addSpacing(20)
        barra_filtro.addWidget(filtro)

        layout_conteudo.addLayout(barra_filtro)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)

        self.tabela.setHorizontalHeaderLabels([
            "Título",
            "Tipo",
            "Data",
            "Status",
            "Ação"
        ])

        acoes = [
            ["Desempenho de bovinos", "Artigo Científico", "29/05/2026", "Aprovado"],
            ["Produção sustentável", "Artigo Científico", "21/12/2024", "Análise"],
            ["Redução da degradação do solo", "Artigo Científico", "10/10/2010", "Recusado"],
            ["Produtividade de culturas agrícolas", "Artigo Científico", "15/08/2025", "Análise"],
            ["Uso da água na produtividade agrícola", "Artigo Científico", "21/04/2026", "Aprovado"],
            ["Estratégias de produção sustentável", "Artigo Científico", "22/05/2026", "Análise"],
            ["Influência da qualidade da pastagem", "Artigo Científico", "01/01/2026", "Aprovado"],
            ["Sistemas de irrigação e sua eficiência", "Artigo Científico", "01/02/2025", "Análise"],
            ["Sistemas de manejo do solo", "Artigo Científico", "29/06/2026", "Aprovado"],
        ]

        self.tabela.setRowCount(len(acoes))

        for linha, acoes_data in enumerate(acoes):

            for coluna in range(4):

                item = QTableWidgetItem(
                    acoes_data[coluna]
                )

                item.setFlags(
                    Qt.ItemIsEnabled |
                    Qt.ItemIsSelectable
                )

                if coluna in [1, 2, 3]:
                    item.setTextAlignment(
                        Qt.AlignCenter |
                        Qt.AlignVCenter
                    )
                else:
                    item.setTextAlignment(
                        Qt.AlignLeft |
                        Qt.AlignVCenter
                    )

                if coluna == 3:

                    fonte_status = QFont("Verdana", 18)
                    fonte_status.setBold(False)

                    item.setFont(fonte_status)

                    if acoes_data[coluna] == "Aprovado":
                        item.setForeground(
                            QColor("#058914")
                        )

                    elif acoes_data[coluna] == "Análise":
                        item.setForeground(
                            QColor("#FFCC00")
                        )

                    elif acoes_data[coluna] == "Recusado":
                        item.setForeground(
                            QColor("#FF0000")
                        )

                self.tabela.setItem(
                    linha,
                    coluna,
                    item
                )

            botao_editar = QPushButton("Editar")
            botao_editar.setFixedSize(100, 32)

            botao_editar.setStyleSheet("""
                QPushButton {
                    background-color: #2C66BF;
                    color: white;
                    border: 3px solid #134593;
                    border-radius: 10px;
                    font-size: 18px;
                }

                QPushButton:hover {
                    background-color: #0668C9;
                }
            """)

            botao_editar.clicked.connect(
                lambda checked=False, row=linha:
                self.editar_acao(row)
            )

            widget_container = QWidget()

            widget_container.setStyleSheet("background: transparent;")

            layout_container = QHBoxLayout(
                widget_container
            )

            layout_container.setContentsMargins(
                0, 0, 0, 0
            )

            layout_container.setAlignment(
                Qt.AlignCenter
            )

            layout_container.addWidget(
                botao_editar
            )

            self.tabela.setCellWidget(
                linha,
                4,
                widget_container
            )

        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid black;
                border-top-right-radius: 14px;
                border-top-left-radius: 14px;
                gridline-color: transparent;
                font-size: 18px;
                font-weight: normal;
                color: black;
                outline: none;
            }

            QTableWidget::item {
                padding-left: 10px;
                padding-right: 10px;
                border-bottom: 1px solid #D4E1EF;
            }

            QTableWidget::item:selected {
                background-color: #EDF5FF;
                color: #222222;
            }

            QHeaderView::section {
                background-color: #356394;
                color: white;
                border: none;
                border-right: 1px solid #356394;
                font-size: 14px;
                font-weight: bold;
                padding: 8px;
            }

            QHeaderView::section:last {
                border-top-right-radius: 13px;
            }

            QHeaderView::section:first {
                border-top-left-radius: 13px;
            }

            QScrollBar:vertical {
                width: 0px;
            }

            QScrollBar:horizontal {
                height: 0px;
            }
        """)

        for linha in range(
            self.tabela.rowCount()
        ):
            self.tabela.setRowHeight(
                linha,
                68
            )

        self.tabela.setFixedHeight(650)

        header = self.tabela.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.Stretch)

        header.setSectionResizeMode(1, QHeaderView.Fixed)

        header.setSectionResizeMode(2, QHeaderView.Fixed)

        header.setSectionResizeMode(3, QHeaderView.Fixed)

        header.setSectionResizeMode(4, QHeaderView.Fixed)

        self.tabela.setColumnWidth(1,220)

        self.tabela.setColumnWidth(2,200)

        self.tabela.setColumnWidth(3,160)

        self.tabela.setColumnWidth(4,140)

        self.tabela.verticalHeader().setVisible(False)

        self.tabela.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.tabela.setSelectionMode(
            QTableWidget.SingleSelection
        )

        layout_conteudo.addWidget(
            self.tabela
        )

        pesquisa.textChanged.connect(
            self.filtrar_tabela
        )

        self.botao_novo.clicked.connect(
            self.nova_acao
        )

        botao_excel.clicked.connect(
            self.baixar_excel
        )

    def filtrar_tabela(self, texto):

        texto = texto.lower()

        for linha in range(
            self.tabela.rowCount()
        ):

            titulo = self.tabela.item(
                linha,
                0
            ).text().lower()

            tipo = self.tabela.item(
                linha,
                1
            ).text().lower()

            status = self.tabela.item(
                linha,
                3
            ).text().lower()

            encontrado = (
                texto in titulo
                or texto in tipo
                or texto in status
            )

            self.tabela.setRowHidden(
                linha,
                not encontrado
            )

    def editar_acao(self, linha):

        titulo = self.tabela.item(
            linha,
            0
        ).text()

        print(
            f"Editando: {titulo}"
        )

    def nova_acao(self):

        print("Nova ação")

    def baixar_excel(self):

        print("Baixar em Excel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaPesquisador()
    window.show()
    sys.exit(app.exec())