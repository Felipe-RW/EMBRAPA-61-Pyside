import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QCheckBox, QStackedWidget,
    QFrame, QGraphicsDropShadowEffect, QMenu, QWidgetAction
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class RelatorioPopup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Relatório")
        self.resize(780, 520)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)

        self.iniciar_interface()

    def iniciar_interface(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(15, 15, 15, 15)

        container_popup = QFrame()
        container_popup.setObjectName("ContainerPopup")
        layout_container = QVBoxLayout(container_popup)
        layout_container.setContentsMargins(25, 20, 25, 20)

        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(20)
        sombra.setColor(QColor(0, 0, 0, 60))
        sombra.setOffset(0, 4)
        container_popup.setGraphicsEffect(sombra)

        layout_cabecalho = QHBoxLayout()
        layout_cabecalho.addStretch()
        
        titulo_relatorio = QLabel("Relatório")
        titulo_relatorio.setObjectName("TituloRelatorio")
        layout_cabecalho.addWidget(titulo_relatorio)
        
        layout_cabecalho.addStretch()
        
        fechar = QPushButton("X")
        fechar.setObjectName("BotaoFechar")
        fechar.setFixedSize(30, 30)
        fechar.clicked.connect(self.close)
        layout_cabecalho.addWidget(fechar)

        layout_container.addLayout(layout_cabecalho)

        layout_navegacao = QHBoxLayout()
        layout_navegacao.setSpacing(15)

        self.relatorio_de_tipos_de_acoes = QPushButton("Relatório de Tipos de Ações")
        self.relatorio_de_empregados = QPushButton("Relatório de Empregados")
        self.relatorio_de_anos = QPushButton("Relatório de Anos")

        for opcao_aba in (self.relatorio_de_tipos_de_acoes, self.relatorio_de_empregados, self.relatorio_de_anos):
            opcao_aba.setCheckable(True)
            opcao_aba.setObjectName("BotaoAba")
            layout_navegacao.addWidget(opcao_aba)

        self.relatorio_de_tipos_de_acoes.setChecked(True)
        layout_container.addLayout(layout_navegacao)

        self.conteudo_paginas = QStackedWidget()
        self.conteudo_paginas.setObjectName("AreaConteudo")

        self.conteudo_paginas.addWidget(self.criar_pagina_tipos_de_acoes())
        self.conteudo_paginas.addWidget(self.criar_pagina_empregados())
        self.conteudo_paginas.addWidget(self.criar_pagina_anos())

        layout_container.addWidget(self.conteudo_paginas)

        self.relatorio_de_tipos_de_acoes.clicked.connect(lambda: self.alternar_aba(0))
        self.relatorio_de_empregados.clicked.connect(lambda: self.alternar_aba(1))
        self.relatorio_de_anos.clicked.connect(lambda: self.alternar_aba(2))

        layout_rodape = QHBoxLayout()
        layout_rodape.addStretch()

        self.gerar_relatorio = QPushButton("Gerar Relatório")
        self.gerar_relatorio.setObjectName("BotaoGerarRelatorio")
        self.gerar_relatorio.setFixedSize(180, 36)
        
        self.configurar_menu_setores()
        self.gerar_relatorio.setMenu(self.menu_setores)

        layout_rodape.addWidget(self.gerar_relatorio)
        layout_container.addLayout(layout_rodape)

        layout_principal.addWidget(container_popup)

        self.aplicar_estilos()

    def configurar_menu_setores(self):
        self.menu_setores = QMenu(self)
        self.menu_setores.setObjectName("MenuSetores")

        frame_menu = QFrame()
        frame_menu.setObjectName("FrameMenu")
        layout_menu = QVBoxLayout(frame_menu)
        layout_menu.setContentsMargins(15, 12, 15, 12)
        layout_menu.setSpacing(12)

        for setor in ["CIPT", "SPAT", "NCO"]:
            botao_setor = QPushButton(setor)
            botao_setor.setObjectName("BotaoOpcaoMenu")
            botao_setor.clicked.connect(lambda s=setor: self.ao_selecionar_setor(s))
            layout_menu.addWidget(botao_setor)

        acao_widget = QWidgetAction(self.menu_setores)
        acao_widget.setDefaultWidget(frame_menu)
        self.menu_setores.addAction(acao_widget)

    def ao_selecionar_setor(self, nome_setor):
        self.menu_setores.close()

    def alternar_aba(self, indice):
        self.conteudo_paginas.setCurrentIndex(indice)
        self.relatorio_de_tipos_de_acoes.setChecked(indice == 0)
        self.relatorio_de_empregados.setChecked(indice == 1)
        self.relatorio_de_anos.setChecked(indice == 2)

    def alternar_modo_selecao(self, botao_selecionar, botao_todos, selecionar_ativo):
        botao_selecionar.setChecked(selecionar_ativo)
        botao_todos.setChecked(not selecionar_ativo)

    def criar_pagina_tipos_de_acoes(self):
        pagina = QWidget()
        layout = QHBoxLayout(pagina)
        
        coluna_esquerda = QVBoxLayout()
        coluna_esquerda.addWidget(QLabel("<b>Ações</b>"))
        
        layout_sub_filtros = QHBoxLayout()
        selecionar_acoes = QPushButton("Selecionar ações")
        selecionar_acoes.setCheckable(True)
        selecionar_acoes.setChecked(True)
        selecionar_acoes.setObjectName("BotaoSubFiltro")
        
        todas_as_acoes = QPushButton("Todos as ações")
        todas_as_acoes.setCheckable(True)
        todas_as_acoes.setObjectName("BotaoSubFiltro")

        selecionar_acoes.clicked.connect(lambda: self.alternar_modo_selecao(selecionar_acoes, todas_as_acoes, True))
        todas_as_acoes.clicked.connect(lambda: self.alternar_modo_selecao(selecionar_acoes, todas_as_acoes, False))

        layout_sub_filtros.addWidget(selecionar_acoes)
        layout_sub_filtros.addWidget(todas_as_acoes)
        layout_sub_filtros.addStretch()
        coluna_esquerda.addLayout(layout_sub_filtros)

        pesquise = QLineEdit()
        pesquise.setPlaceholderText("Pesquise...")
        coluna_esquerda.addWidget(pesquise)

        itens_acoes = [
            "Coordenação de evento REGIONAL",
            "Artigos de divulgação na mídia",
            "Produção de vídeos técnicos",
            "Elaboração do plano em marketing"
        ]
        for item in itens_acoes:
            coluna_esquerda.addWidget(QCheckBox(item))
        coluna_esquerda.addStretch()

        coluna_direita = QVBoxLayout()
        coluna_direita.addWidget(QLabel("<b>Dados</b>"))
        coluna_direita.addWidget(QCheckBox("Setor"))
        coluna_direita.addWidget(QCheckBox("Status"))
        coluna_direita.addStretch()

        layout.addLayout(coluna_esquerda)
        layout.addLayout(coluna_direita)
        return pagina

    def criar_pagina_empregados(self):
        pagina = QWidget()
        layout = QHBoxLayout(pagina)

        coluna_esquerda = QVBoxLayout()
        coluna_esquerda.addWidget(QLabel("<b>Funcionários</b>"))

        layout_sub_filtros = QHBoxLayout()
        selecionar_empregados = QPushButton("Selecionar Empregados")
        selecionar_empregados.setCheckable(True)
        selecionar_empregados.setChecked(True)
        selecionar_empregados.setObjectName("BotaoSubFiltro")

        todos_os_empregados = QPushButton("Todos os Empregados")
        todos_os_empregados.setCheckable(True)
        todos_os_empregados.setObjectName("BotaoSubFiltro")

        selecionar_empregados.clicked.connect(lambda: self.alternar_modo_selecao(selecionar_empregados, todos_os_empregados, True))
        todos_os_empregados.clicked.connect(lambda: self.alternar_modo_selecao(selecionar_empregados, todos_os_empregados, False))

        layout_sub_filtros.addWidget(selecionar_empregados)
        layout_sub_filtros.addWidget(todos_os_empregados)
        layout_sub_filtros.addStretch()
        coluna_esquerda.addLayout(layout_sub_filtros)

        pesquise = QLineEdit()
        pesquise.setPlaceholderText("Pesquise...")
        coluna_esquerda.addWidget(pesquise)

        for item in ["Fulano Da Silva", "Fulano Ferreira", "Fulano Araujo", "Fulano Oliveira"]:
            coluna_esquerda.addWidget(QCheckBox(item))
        coluna_esquerda.addStretch()

        coluna_direita = QVBoxLayout()
        coluna_direita.addWidget(QLabel("<b>Dados</b>"))
        coluna_direita.addWidget(QCheckBox("Email"))
        coluna_direita.addWidget(QCheckBox("Área de Atuação"))
        coluna_direita.addWidget(QCheckBox("Status"))
        coluna_direita.addStretch()

        layout.addLayout(coluna_esquerda)
        layout.addLayout(coluna_direita)
        return pagina

    def criar_pagina_anos(self):
        pagina = QWidget()
        layout = QHBoxLayout(pagina)

        coluna_esquerda = QVBoxLayout()
        coluna_esquerda.addWidget(QLabel("<b>Anos</b>"))

        layout_sub_filtros = QHBoxLayout()
        selecionar_anos = QPushButton("Selecionar Anos")
        selecionar_anos.setCheckable(True)
        selecionar_anos.setChecked(True)
        selecionar_anos.setObjectName("BotaoSubFiltro")

        todos_os_anos = QPushButton("Todos os Anos")
        todos_os_anos.setCheckable(True)
        todos_os_anos.setObjectName("BotaoSubFiltro")

        selecionar_anos.clicked.connect(lambda: self.alternar_modo_selecao(selecionar_anos, todos_os_anos, True))
        todos_os_anos.clicked.connect(lambda: self.alternar_modo_selecao(selecionar_anos, todos_os_anos, False))

        layout_sub_filtros.addWidget(selecionar_anos)
        layout_sub_filtros.addWidget(todos_os_anos)
        layout_sub_filtros.addStretch()
        coluna_esquerda.addLayout(layout_sub_filtros)

        pesquise = QLineEdit()
        pesquise.setPlaceholderText("Pesquise...")
        coluna_esquerda.addWidget(pesquise)

        for ano in ["2026", "2025", "2024", "2023"]:
            coluna_esquerda.addWidget(QCheckBox(ano))
        coluna_esquerda.addStretch()

        coluna_direita = QVBoxLayout()
        coluna_direita.addWidget(QLabel("<b>Dados</b>"))
        coluna_direita.addWidget(QCheckBox("Status"))
        coluna_direita.addWidget(QCheckBox("Número de Ações Enviadas"))
        coluna_direita.addWidget(QCheckBox("Número de Ações Avaliadas"))
        coluna_direita.addWidget(QCheckBox("Tipos de Ações"))
        coluna_direita.addStretch()

        layout.addLayout(coluna_esquerda)
        layout.addLayout(coluna_direita)
        return pagina

    def aplicar_estilos(self):
        self.setStyleSheet("""
            #ContainerPopup {
                background-color: #F8F9FA;
                border-radius: 20px;
            }
            #TituloRelatorio {
                font-size: 20px;
                font-weight: bold;
                color: #333333;
            }
            #BotaoFechar {
                background: transparent;
                border: none;
                font-size: 18px;
                font-weight: bold;
                color: #333333;
            }
            #BotaoFechar:hover {
                color: #FF0000;
            }

            #BotaoAba {
                background-color: #E2E4E8;
                color: #555555;
                border: none;
                border-radius: 15px;
                padding: 8px 16px;
                font-weight: bold;
                font-size: 12px;
            }
            #BotaoAba:checked {
                background-color: #4C72B0;
                color: #FFFFFF;
            }

            #BotaoSubFiltro {
                background-color: #FFFFFF;
                color: #333333;
                border: none;
                border-radius: 12px;
                padding: 4px 12px;
                font-weight: bold;
                font-size: 11px;
            }
            #BotaoSubFiltro:checked {
                background-color: #4C72B0;
                color: #FFFFFF;
            }

            #AreaConteudo {
                background-color: #DDE1E5;
                border-radius: 12px;
                padding: 15px;
            }

            QCheckBox {
                font-size: 13px;
                color: #333333;
                spacing: 8px;
            }
            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #CCCCCC;
                border-radius: 12px;
                padding: 6px 12px;
            }

            #BotaoGerarRelatorio {
                background-color: #3B488C;
                color: white;
                border: none;
                border-radius: 18px;
                font-weight: bold;
                font-size: 13px;
            }
            #BotaoGerarRelatorio:hover, #BotaoGerarRelatorio:on {
                background-color: #288034;
            }
            #BotaoGerarRelatorio::menu-indicator {
                image: none;
                width: 0px;
            }

            QMenu#MenuSetores {
                background: transparent;
                border: none;
            }
            #FrameMenu {
                background-color: #E9ECEF;
                border-radius: 10px;
                border: 1px solid #CED4DA;
            }
            #BotaoOpcaoMenu {
                background: transparent;
                border: none;
                color: #333333;
                font-weight: bold;
                font-size: 13px;
                text-align: center;
                padding: 4px;
            }
            #BotaoOpcaoMenu:hover {
                color: #1E7E34;
            }
        """)

if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    janela = RelatorioPopup()
    janela.show()
    sys.exit(aplicacao.exec())