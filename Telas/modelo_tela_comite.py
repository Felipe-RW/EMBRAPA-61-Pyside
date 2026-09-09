import sys, os

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup,
    QScrollArea, QSizePolicy
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")


class ModeloTelaAdministrador(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de colaboradores")
        self.setMinimumSize(1920, 1080)

        self.setStyleSheet("""
            QWidget {
                font-family: 'Verdana';
                font-weight: bold;
                background-color: #356394;
                border: none;
            }
        """)

        self.area_scroll = QScrollArea()
        self.area_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.area_scroll.setWidgetResizable(True)

        conteudo_pagina = QWidget()
        self.area_scroll.setWidget(conteudo_pagina)

        layout_principal = QHBoxLayout(conteudo_pagina)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        self.setCentralWidget(self.area_scroll)

        # MENU LATERAL

        menu_lateral = QWidget(self)
        menu_lateral.setFixedWidth(280)

        menu_lateral.setStyleSheet("""
            QWidget {
                background-color: #356394;
            }
        """)

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)
        menu_lateral_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.btn_home = btn_layout(
            os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"),
            "Painel Principal"
        )

        self.btn_empregados = btn_layout(
            os.path.join(BASE, "Imagens/Empregados-Icone.png"),
            "Pesquisadores"
        )

        logo_label = QLabel()

        logo = QPixmap(LOGO)
        logo_certa = logo.scaled(
            220,
            190,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        logo_label.setPixmap(logo_certa)
        logo_label.setAlignment(Qt.AlignLeft)

        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)

        menu_lateral_layout.setSpacing(5)

        menu_lateral_layout.addWidget(self.btn_empregados)

        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_empregados)

        menu_lateral_layout.addStretch()

        # PÁGINA PRINCIPAL

        pagina_principal = QWidget()

        layout_pagina = QVBoxLayout(pagina_principal)
        layout_pagina.setContentsMargins(0, 0, 0, 0)
        layout_pagina.setSpacing(0)

        # CABEÇALHO

        cabecalho = QWidget(self)
        cabecalho.setFixedSize(1640, 70)

        cabecalho.setStyleSheet("""
            QWidget {
                background-color: #356394;
            }
        """)

        cabecalho_layout = QHBoxLayout(cabecalho)
        cabecalho_layout.setContentsMargins(40, 0, 40, 0)

        nome_empregado = QLabel(
            "Fulano da Silva Rodrigues",
            cabecalho
        )

        nome_empregado.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum
        )

        nome_empregado.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #ffffff;
            }
        """)

        separador = QLabel("|", cabecalho)

        separador.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum
        )

        separador.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #ffffff;
            }
        """)

        funcao_empregado = QLabel("Comitê", cabecalho)

        funcao_empregado.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum
        )

        funcao_empregado.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 24px;
            }
        """)

        nome_tela = QLabel("Funcionários", cabecalho)

        nome_tela.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum
        )

        nome_tela.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter;
            }
        """)

        botao_logout = QPushButton("Logout", cabecalho)
        botao_logout.setFixedSize(150, 40)
        botao_logout.setCursor(Qt.PointingHandCursor)

        botao_logout.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #8E8E93;
                color: #FFFFFF;
            }
        """)

        cabecalho_layout.addWidget(nome_empregado)
        cabecalho_layout.addSpacing(30)
        cabecalho_layout.addWidget(separador)
        cabecalho_layout.addSpacing(30)
        cabecalho_layout.addWidget(funcao_empregado)
        cabecalho_layout.addStretch()
        cabecalho_layout.addWidget(nome_tela)
        cabecalho_layout.addStretch()
        cabecalho_layout.addWidget(botao_logout)

        # PÁGINA BRANCA

        frame_principal = QFrame(self)

        frame_principal.setFixedWidth(1600)
        frame_principal.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Expanding
        )

        frame_principal.setContentsMargins(0, 0, 0, 0)

        frame_principal.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
            }
        """)

        frame_principal_layout = QVBoxLayout(frame_principal)
        frame_principal_layout.setContentsMargins(0, 0, 0, 0)
        frame_principal_layout.setSpacing(0)

        # ==========================================================
        # CONTEÚDO DA TELA
        # ==========================================================

        # TÍTULO

        titulo = QLabel(
            "Lista de colaboradores",
            frame_principal
        )

        titulo.setGeometry(
            0,
            30,
            1600,
            45
        )

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            QLabel {
                color: #000000;
                font-family: Verdana;
                font-size: 28px;
                font-weight: bold;
                background-color: transparent;
            }
        """)

        # NOME DO COLABORADOR

        nome_colaborador = QLabel(
            "Fulano Da Silva",
            frame_principal
        )

        nome_colaborador.setGeometry(
            81,
            106,
            300,
            35
        )

        nome_colaborador.setStyleSheet("""
            QLabel {
                color: #000000;
                font-family: Verdana;
                font-size: 18px;
                font-weight: bold;
                background-color: transparent;
            }
        """)

        # CAMPO DE PESQUISA

        campo_busca = QLineEdit(frame_principal)

        campo_busca.setGeometry(
            780,
            101,
            248,
            36
        )

        campo_busca.setPlaceholderText("Ação")

        campo_busca.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                font-family: Verdana;
                font-size: 14px;
                font-weight: normal;
                border: 1px solid #999999;
                border-radius: 7px;
                padding-left: 10px;
            }
        """)

        # ==========================================================
        # TABELA
        # ==========================================================

        tabela = QWidget(frame_principal)

        tabela.setGeometry(
            190,
            170,
            728,
            255
        )

        tabela.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
        """)

        tabela_layout = QVBoxLayout(tabela)

        tabela_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        tabela_layout.setSpacing(0)

        # CABEÇALHO

        cabecalho_tabela = QWidget()

        cabecalho_tabela.setFixedSize(
            728,
            48
        )

        cabecalho_tabela.setStyleSheet("""
            QWidget {
                background-color: #356394;
                border-top-left-radius: 12px;
                border-top-right-radius: 12px;
            }
        """)

        cabecalho_layout = QHBoxLayout(cabecalho_tabela)

        cabecalho_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        cabecalho_layout.setSpacing(0)

        titulo_acao = QLabel("Tipo da Ação")
        titulo_tipo = QLabel("Tipo")
        titulo_data = QLabel("Data")

        titulo_acao.setFixedWidth(240)
        titulo_tipo.setFixedWidth(270)
        titulo_data.setFixedWidth(160)

        for coluna in [
            titulo_acao,
            titulo_tipo,
            titulo_data
        ]:

            coluna.setAlignment(
                Qt.AlignCenter
            )

            coluna.setStyleSheet("""
                QLabel {
                    color: #ffffff;
                    font-family: Verdana;
                    font-size: 18px;
                    font-weight: bold;
                    background-color: transparent;
                }
            """)

        cabecalho_layout.addWidget(titulo_acao)
        cabecalho_layout.addWidget(titulo_tipo)
        cabecalho_layout.addWidget(titulo_data)

        tabela_layout.addWidget(
            cabecalho_tabela
        )

        # DADOS

        dados = [
            (
                "Pesquisa 1",
                "Setor",
                "Artigo Científico",
                "23/03/2026"
            ),
            (
                "Pesquisa 2",
                "Setor",
                "Artigo Científico",
                "29/04/2026"
            ),
            (
                "Pesquisa 3",
                "Setor",
                "Artigo Científico",
                "22/06/2026"
            ),
            (
                "Pesquisa 4",
                "Setor",
                "Artigo Científico",
                "23/07/2026"
            ),
            (
                "Pesquisa 5",
                "Setor",
                "Artigo Científico",
                "29/08/2026"
            )
        ]

        for i, dados_linha in enumerate(dados):

            linha = QWidget()

            linha.setFixedSize(
                728,
                41
            )

            fundo = (
                "#E6F0FC"
                if i % 2 == 0
                else "#FFFFFF"
            )

            if i == 4:

                linha.setStyleSheet(f"""
                    QWidget {{
                        background-color: {fundo};
                        border-bottom-left-radius: 12px;
                        border-bottom-right-radius: 12px;
                    }}
                """)

            else:

                linha.setStyleSheet(f"""
                    QWidget {{
                        background-color: {fundo};
                    }}
                """)

            linha_layout = QHBoxLayout(linha)

            linha_layout.setContentsMargins(
                0,
                0,
                0,
                0
            )

            linha_layout.setSpacing(0)

            # PESQUISA

            acao = QLabel(
                dados_linha[0]
            )

            acao.setFixedWidth(210)

            acao.setAlignment(
                Qt.AlignCenter
            )

            acao.setStyleSheet("""
                QLabel {
                    color: #000000;
                    font-family: Verdana;
                    font-size: 16px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            # TIPO

            tipo = QWidget()

            tipo.setFixedWidth(270)

            tipo_layout = QHBoxLayout(tipo)

            tipo_layout.setContentsMargins(
                0,
                0,
                0,
                0
            )

            tipo_layout.setSpacing(10)

            setor = QLabel(
                dados_linha[1]
            )

            setor.setFixedWidth(55)

            setor.setAlignment(
                Qt.AlignRight | Qt.AlignVCenter
            )

            setor.setStyleSheet("""
                QLabel {
                    color: #666666;
                    font-family: Verdana;
                    font-size: 15px;
                    font-weight: bold;
                    background-color: transparent;
                }
            """)

            artigo = QLabel(
                dados_linha[2]
            )

            artigo.setFixedWidth(195)

            artigo.setAlignment(
                Qt.AlignLeft | Qt.AlignVCenter
            )

            artigo.setStyleSheet("""
                QLabel {
                    color: #000000;
                    font-family: Verdana;
                    font-size: 16px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            tipo_layout.addWidget(setor)
            tipo_layout.addWidget(artigo)

            # DATA

            data = QLabel(
                dados_linha[3]
            )

            data.setFixedWidth(160)

            data.setAlignment(
                Qt.AlignCenter
            )

            data.setStyleSheet("""
                QLabel {
                    color: #000000;
                    font-family: Verdana;
                    font-size: 16px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            # SETA

            seta = QLabel("⌄")

            seta.setFixedWidth(58)

            seta.setAlignment(
                Qt.AlignCenter
            )

            seta.setStyleSheet("""
                QLabel {
                    color: #000000;
                    font-family: Arial;
                    font-size: 24px;
                    font-weight: bold;
                    background-color: transparent;
                }
            """)

            linha_layout.addWidget(acao)
            linha_layout.addWidget(tipo)
            linha_layout.addWidget(data)
            linha_layout.addWidget(seta)

            tabela_layout.addWidget(linha)

        # ==========================================================

        layout_pagina.addWidget(cabecalho)
        layout_pagina.addWidget(frame_principal)

        layout_principal.addWidget(menu_lateral)
        layout_principal.addWidget(pagina_principal)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ModeloTelaAdministrador()

    window.showMaximized()

    sys.exit(app.exec())