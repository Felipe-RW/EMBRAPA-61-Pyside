import sys
from PySide6.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QFrame,
    QCheckBox,
    QLineEdit,
    QStackedWidget,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

ESTILO_BOTAO_ABA_ATIVA = """

QPushButton{
color: white;
font-size: 16px;
font-family: verdana;
font-weight: bold;
background-color: #356394;
border-radius:20px;
}
"""

ESTILO_BOTAO_ABA_INATIVA = """
QPushButton{
color:black;
font-size:16px;
font-family: verdana;
font-weight: bold;
background-color: #DFDFDF;
border-radius:20px;
}
"""

ESTILO_LABEL_TITULO_SECAO = """
QLabel{
color:black;
font-size:20px;
font-family:verdana;
font-weight:bold;
}
"""

ESTILO_BOTAO_SELECIONAR = """
QPushButton{
color: white;
font-size:13px;
font-family:verdana;
font-weight:bold;
background-color: #356394;
border-radius:15px;
}
"""

ESTILO_BOTAO_TODOS = """
QPushButton{
color:black;
font-size: 13px;
font-family:verdana;
font-weight:bold;
background-color:white;
border-radius:15px;
}
"""

ESTILO_CAIXA_BUSCA = """
QLineEdit{
background-color:white;
border-radius:10px;
padding:3px 10px;
border:0.5px solid #686868;
}
"""

ESTILO_CHECKBOX = """
QCheckBox{
color:black;
font-size:16px;
font-family:verdana;
font-weight:lighter;
}
"""

ESTILO_BOTAO_GERAR_RELATORIO = """
QPushButton{
color:white;
font-size:16px;
font-family:verdana;
font-weight:bold;
background-color: #1B3A5C;
border-radius:20px;
}
QPushButton:hover{
background-color: #14293F;
}
"""

def criar_caixa_de_busca(pai):
    caixa_de_busca = QLineEdit(pai)
    caixa_de_busca.setPlaceholderText("Pesquise...")
    caixa_de_busca.setGeometry(61,125,400,32)
    caixa_de_busca.setStyleSheet(ESTILO_CAIXA_BUSCA)

    icone_lupa = QIcon.fromTheme("edit-find")
    if not icone_lupa.isNull():
        caixa_de_busca.addAction(icone_lupa,QLineEdit.ActionPosition.TrailingPosition)
    
    return caixa_de_busca


def atualizar_selecao_botoes(lista_botoes,indice_ativo,estilo_ativo,estilo_inativo):
    for i, botao in enumerate(lista_botoes):
        botao.setStyleSheet(estilo_ativo if i == indice_ativo else estilo_inativo)


def criar_pagina_tipos_de_acoes():
    pagina = QFrame()
    pagina.setStyleSheet("QWidget{background-color: #DFDFDF; border-radius:0px;}")

    acoes = QLabel("Ações",pagina)
    acoes.setGeometry(61,28,200,30)
    acoes.setStyleSheet(ESTILO_LABEL_TITULO_SECAO)

    botao_selecionar_acoes = QPushButton("Selecionar Ações", pagina)
    botao_selecionar_acoes.setGeometry(61,74,192,30)
    botao_selecionar_acoes.setStyleSheet(ESTILO_BOTAO_SELECIONAR)

    botao_todas_as_acoes = QPushButton("Todas as Ações",pagina)
    botao_todas_as_acoes.setGeometry(275,74,192,30)
    botao_todas_as_acoes.setStyleSheet(ESTILO_BOTAO_TODOS)

    botoes_tipos_de_acoes = [botao_selecionar_acoes,botao_todas_as_acoes]
    botao_selecionar_acoes.clicked.connect(lambda:atualizar_selecao_botoes(botoes_tipos_de_acoes,0,ESTILO_BOTAO_SELECIONAR,ESTILO_BOTAO_TODOS))
    botao_todas_as_acoes.clicked.connect(lambda:atualizar_selecao_botoes(botoes_tipos_de_acoes,1,ESTILO_BOTAO_SELECIONAR,ESTILO_BOTAO_TODOS))

    criar_caixa_de_busca(pagina)

    nomes_acoes = [
        "Coordenação de evento REGIONAL",
        "Artigos de Divulgação na mídia",
        "Produção de Vídeos Técnicos",
        "Elaboração do Plano em Marketing",
    ]

    for i, nome in enumerate(nomes_acoes):
        checkbox = QCheckBox(nome,pagina)
        checkbox.setGeometry(61,170 + i * 30,400,20)
        checkbox.setStyleSheet(ESTILO_CHECKBOX)

    dados = QLabel("Dados",pagina)
    dados.setGeometry(624,28,75,30)
    dados.setStyleSheet(ESTILO_LABEL_TITULO_SECAO)

    nomes_dados=["Setor","Status"]
    for i, nome in enumerate(nomes_dados):
        checkbox = QCheckBox(nome,pagina)
        checkbox.setGeometry(624,74 + i * 30,400,20)
        checkbox.setStyleSheet(ESTILO_CHECKBOX)

    return pagina


def criar_pagina_empregados():
    pagina = QFrame()
    pagina.setStyleSheet("QWidget {background-color: #DFDFDF; border-radius:0px;}")

    empregados = QLabel("Empregados",pagina)
    empregados.setGeometry(61,28,200,30)
    empregados.setStyleSheet(ESTILO_LABEL_TITULO_SECAO)

    botao_selecionar_empregados = QPushButton("Selecionar Empregados",pagina)
    botao_selecionar_empregados.setGeometry(61,74,192,30)
    botao_selecionar_empregados.setStyleSheet(ESTILO_BOTAO_SELECIONAR)

    criar_caixa_de_busca(pagina)

    nomes_empregados = {
        "Fulano da Silva",
        "Fulano Lima",
        "Fulano Rodrigues",
        "Fulano Carvalho",
    }
    for i,nome in enumerate(nomes_empregados):
        checkbox = QCheckBox(nome,pagina)
        checkbox.setGeometry(61,170+i*30,400,20)
        checkbox.setStyleSheet(ESTILO_CHECKBOX)

    dados = QLabel("Dados",pagina)
    dados.setGeometry(624,28,75,30)
    dados.setStyleSheet(ESTILO_LABEL_TITULO_SECAO)

    nomes_dados = ["Email","Área de Atuação","Status"]
    for i, nome in enumerate(nomes_dados):
        checkbox = QCheckBox(nome,pagina)
        checkbox.setGeometry(624,74 + i*30,400,20)
        checkbox.setStyleSheet(ESTILO_CHECKBOX)

    return pagina


def criar_pagina_anos():
    pagina = QFrame()
    pagina.setStyleSheet("QWidget {background-color: #DFDFDF; border-radius:0px;}")

    anos = QLabel("Anos",pagina)
    anos.setGeometry(61,28,200,30)
    anos.setStyleSheet(ESTILO_LABEL_TITULO_SECAO)

    botao_selecionar_anos = QPushButton("Selecionar Anos",pagina)
    botao_selecionar_anos.setGeometry(61,74,192,30)
    botao_selecionar_anos.setStyleSheet(ESTILO_BOTAO_SELECIONAR)

    botao_todos_os_anos = QPushButton("Todos os Anos",pagina)
    botao_todos_os_anos.setGeometry(275,74,192,30)
    botao_todos_os_anos.setStyleSheet(ESTILO_BOTAO_TODOS)

    botoes_anos = [botao_selecionar_anos,botao_todos_os_anos]
    botao_selecionar_anos.clicked.connect(lambda:atualizar_selecao_botoes(botoes_anos,0,ESTILO_BOTAO_SELECIONAR,ESTILO_BOTAO_TODOS))
    botao_todos_os_anos.clicked.connect(lambda:atualizar_selecao_botoes(botoes_anos,1,ESTILO_BOTAO_SELECIONAR,ESTILO_BOTAO_TODOS))

    criar_caixa_de_busca(pagina)

    nomes_anos = ["2026","2025","2024","2023"]
    for i, nome in enumerate(nomes_anos):
        checkbox = QCheckBox(nome,pagina)
        checkbox.setGeometry(61,170+i*30,400,20)
        checkbox.setStyleSheet(ESTILO_CHECKBOX)

    dados = QLabel("Dados",pagina)
    dados.setGeometry(624,28,75,30)
    dados.setStyleSheet(ESTILO_LABEL_TITULO_SECAO)

    nomes_dados = [
        "Status",
        "Número de Ações Enviadas",
        "Número de Ações Avaliadas",
        "Tipos de Ações",
    ]

    for i,nome in enumerate(nomes_dados):
        checkbox = QCheckBox(nome,pagina)
        checkbox.setGeometry(624,74 + i*30,400,20)
        checkbox.setStyleSheet(ESTILO_CHECKBOX)

    return pagina

class JanelaRelatorio(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Popup Relatório Administrador Tipos de Ações")
        self.setFixedSize(1202,639)
        self.setStyleSheet(
            """
            QWidget{
            background-color:white;
            border-radius:20px;
            }
            """
        )

        titulo = QLabel("Relatório",self)
        titulo.setGeometry(350,37,500,40)
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
        QLabel{
        color:black;
        font-size:32px;
        font-family:verdana;
        font-weight: bold;
        background-color: transparent;
        }
        """
        )

        self.botao_relatorio_tipos_de_acoes = QPushButton("Relatório de Tipos de Ações",self)
        self.botao_relatorio_tipos_de_acoes.setGeometry(54,150,303,40)

        self.botao_relatorio_empregados = QPushButton("Relatório de Empregados",self)
        self.botao_relatorio_empregados.setGeometry(375,150,303,40)

        self.botao_relatorio_anos = QPushButton("Relatório de Anos",self)
        self.botao_relatorio_anos.setGeometry(696,150,303,40)

        self.botoes_abas = [
            self.botao_relatorio_tipos_de_acoes,
            self.botao_relatorio_empregados,
            self.botao_relatorio_anos,
        ]

        self.paginas = QStackedWidget(self)
        self.paginas.setGeometry(54,215,1094,354)

        self.paginas.addWidget(criar_pagina_tipos_de_acoes())
        self.paginas.addWidget(criar_pagina_empregados())
        self.paginas.addWidget(criar_pagina_anos())

        self.botao_relatorio_tipos_de_acoes.clicked.connect(lambda:self.selecionar_aba(0))
        self.botao_relatorio_empregados.clicked.connect(lambda:self.selecionar_aba(1))
        self.botao_relatorio_anos.clicked.connect(lambda:self.selecionar_aba(2))

        self.botao_gerar_relatorio = QPushButton("Gerar Relatório", self)
        self.botao_gerar_relatorio.setGeometry(923,585,225,40)
        self.botao_gerar_relatorio.setStyleSheet(ESTILO_BOTAO_GERAR_RELATORIO)
        self.botao_gerar_relatorio.clicked.connect(self.gerar_relatorio)

        self.selecionar_aba(0)

    def selecionar_aba(self,indice):
        self.paginas.setCurrentIndex(indice)
        for i,botao in enumerate(self.botoes_abas):
            botao.setStyleSheet(
                ESTILO_BOTAO_ABA_ATIVA if i == indice else ESTILO_BOTAO_ABA_INATIVA
            )

    def gerar_relatorio(self):
        indice_aba = self.paginas.currentIndex()
        nomes_abas = ["Tipos de Ações", "Empregados", "Anos"]
        print(f"Gerando relatório de:{nomes_abas[indice_aba]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaRelatorio()
    janela.show()
    sys.exit(app.exec())