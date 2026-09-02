from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QCheckBox,
    QLineEdit
)

from estilos import ESTILO


class PopupRelatorio(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("popup")
        self.setFixedSize(1504, 639)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(ESTILO)

        self.criar_titulo()
        self.criar_botao_fechar()
        self.criar_botao_relatorio()
        self.criar_area_cinza()
        self.criar_dados()
        self.criar_anos()
        self.criar_pesquisadores()
        self.criar_botao_gerar()


    def criar_titulo(self):

        self.titulo = QLabel("Relatório", self)
        self.titulo.setObjectName("titulo")
        self.titulo.setGeometry(670, 37, 164, 39)
        self.titulo.setAlignment(Qt.AlignCenter)


    def criar_botao_fechar(self):

        self.botao_fechar = QPushButton("X", self)
        self.botao_fechar.setObjectName("botaoFechar")
        self.botao_fechar.setGeometry(1420, 15, 60, 50)
        self.botao_fechar.clicked.connect(self.close)


    def criar_botao_relatorio(self):

        self.botao_relatorio = QPushButton("Relatório de Pesquisas", self)
        self.botao_relatorio.setObjectName("botaoRelatorio")
        self.botao_relatorio.setGeometry(54, 149, 303, 39)


    def criar_area_cinza(self):

        self.area = QWidget(self)
        self.area.setObjectName("areaCinza")
        self.area.setGeometry(54, 208, 1395, 354)


    def criar_dados(self):

        self.titulo_dados = QLabel("Dados do Relatório", self.area)
        self.titulo_dados.setObjectName("tituloSecao")
        self.titulo_dados.setGeometry(47, 31, 269, 23)

        self.criar_linha(275, 20, 1, 280)

        self.criar_checkbox("Categoria de Ação", 40, 70, 220)
        self.criar_checkbox("Data de Postagem", 40, 105, 220)
        self.criar_checkbox("Status", 40, 140, 220)
        self.criar_checkbox("Pesquisador", 40, 175, 220)
        self.criar_checkbox("Setor", 40, 210, 220)


    def criar_anos(self):

        self.titulo_anos = QLabel("Anos", self.area)
        self.titulo_anos.setObjectName("tituloSecao")
        self.titulo_anos.setGeometry(384, 31, 67, 23)

        self.botao_selecionar_anos = QPushButton("Selecionar anos", self.area)
        self.botao_selecionar_anos.setObjectName("botaoAzul")
        self.botao_selecionar_anos.setGeometry(305, 70, 150, 24)

        self.botao_todos_anos = QPushButton("Todos os anos", self.area)
        self.botao_todos_anos.setObjectName("botaoBranco")
        self.botao_todos_anos.setGeometry(510, 70, 150, 24)

        self.criar_checkbox("2022", 305, 115, 100)
        self.criar_checkbox("2023", 305, 155, 100)
        self.criar_checkbox("2024", 305, 195, 100)
        self.criar_checkbox("2025", 305, 235, 100)
        self.criar_checkbox("2026", 305, 275, 100)

        self.criar_linha(700, 28, 1, 260)


    def criar_pesquisadores(self):

        self.titulo_pesquisadores = QLabel("Pesquisadores", self.area)
        self.titulo_pesquisadores.setObjectName("tituloSecao")
        self.titulo_pesquisadores.setGeometry(725, 25, 230, 35)

        self.botao_selecionar_pesquisadores = QPushButton(
            "Selecionar pesquisadores", self.area
        )
        self.botao_selecionar_pesquisadores.setObjectName("botaoAzul")
        self.botao_selecionar_pesquisadores.setGeometry(725, 70, 165, 24)

        self.botao_todos_pesquisadores = QPushButton(
            "Todos os pesquisadores", self.area
        )
        self.botao_todos_pesquisadores.setObjectName("botaoBranco")
        self.botao_todos_pesquisadores.setGeometry(900, 70, 165, 24)

        self.campo_pesquisa = QLineEdit(self.area)
        self.campo_pesquisa.setPlaceholderText("Pesquise...")
        self.campo_pesquisa.setGeometry(750, 105, 300, 42)

        self.criar_checkbox("Fulano da Silva", 725, 155, 230)
        self.criar_checkbox("Ciclano da Silva", 725, 195, 230)
        self.criar_checkbox("Beltrano da Silva", 725, 235, 230)


    def criar_botao_gerar(self):

        self.botao_gerar = QPushButton("Gerar Relatório", self)
        self.botao_gerar.setObjectName("botaoGerar")
        self.botao_gerar.setGeometry(1180, 575, 269, 34)


    def criar_checkbox(self, texto, x, y, largura):

        checkbox = QCheckBox(texto, self.area)
        checkbox.setGeometry(x, y, largura, 30)

        return checkbox


    def criar_linha(self, x, y, largura, altura):

        linha = QWidget(self.area)
        linha.setGeometry(x, y, largura, altura)
        linha.setStyleSheet("background-color: #707070;")

        return linha



    def criar_linha(self, x, y, largura, altura):

        linha = QWidget(self.area)

        linha.setGeometry(x, y, largura, altura)

        linha.setStyleSheet("background-color: #707070;")

        return linha