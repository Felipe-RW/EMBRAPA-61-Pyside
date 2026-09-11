import sys, os
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup,
    QGraphicsDropShadowEffect
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")


class ModeloTelaComite(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de colaboradores")
        self.setFixedSize(1920, 1080)

        self.setStyleSheet("""
            QWidget {
                font-family: 'Verdana';
                font-weight: regular;
                background-color: #356394;
            }
        """)

        # ==========================================================
        # MENU LATERAL
        # ==========================================================

        menu_lateral = QWidget(self)
        menu_lateral.setGeometry(0, 0, 280, 1080)

        menu_lateral.setStyleSheet("""
            QWidget {
                background-color: #356394;
            }
        """)

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)

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

        # ==========================================================
        # CABEÇALHO
        # ==========================================================

        cabecalho = QWidget(self)
        cabecalho.setGeometry(280, 0, 1640, 70)

        cabecalho.setStyleSheet("""
            QWidget {
                background-color: #356394;
            }
        """)

        nome_empregado = QLabel(
            "Fulano da Silva Rodrigues",
            cabecalho
        )

        nome_empregado.setGeometry(
            35,
            22,
            400,
            30
        )

        nome_empregado.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #ffffff;
            }
        """)

        separador = QLabel("|", cabecalho)

        separador.setGeometry(
            420,
            22,
            5,
            30
        )

        separador.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #ffffff;
            }
        """)

        funcao_empregado = QLabel(
            "Comitê",
            cabecalho
        )

        funcao_empregado.setGeometry(
            470,
            22,
            200,
            30
        )

        funcao_empregado.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 24px;
            }
        """)

        nome_tela = QLabel(
            "Funcionários",
            cabecalho
        )

        nome_tela.setGeometry(
            1000,
            22,
            300,
            30
        )

        nome_tela.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter;
            }
        """)

        botao_logout = QPushButton(
            "Logout",
            cabecalho
        )

        botao_logout.setGeometry(
            1450,
            15,
            150,
            40
        )

        botao_logout.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }
        """)

        # ==========================================================
        # PÁGINA BRANCA
        # ==========================================================

        paginaprincipal = QFrame(self)

        paginaprincipal.setGeometry(
            280,
            70,
            1600,
            1010
        )

        paginaprincipal.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
            }
        """)

        # ==========================================================
        # TÍTULO
        # ==========================================================

        titulo = QLabel(
            "Lista de colaboradores",
            paginaprincipal
        )

        titulo.setGeometry(
            550,
            48,
            500,
            55
        )

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            QLabel {
                color: #000000;
                font-family: 'Inter';
                font-size: 36px;
                font-weight: 800;
                background-color: transparent;
            }
        """)

        # ==========================================================
        # NOME DO COLABORADOR
        # ==========================================================

        nome_colaborador = QLabel(
            "Fulano Da Silva",
            paginaprincipal
        )

        nome_colaborador.setGeometry(
            118,
            161,
            217,
            30
        )

        nome_colaborador.setAlignment(
            Qt.AlignLeft | Qt.AlignVCenter
        )

        nome_colaborador.setStyleSheet("""
            QLabel {
                color: #000000;
                font-family: 'Verdana';
                font-size: 25px;
                font-weight: bold;
                background-color: transparent;
            }
        """)

       # ==========================================================
        # CAMPO DE PESQUISA
        # ==========================================================

        container_busca = QWidget(paginaprincipal)
        container_busca.setGeometry(1134, 145, 358, 50)
        container_busca.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border: 1px solid #999999;
                border-radius: 7px;
            }
        """)

        layout_busca_interno = QHBoxLayout(container_busca)
        layout_busca_interno.setContentsMargins(10, 0, 10, 0)
        layout_busca_interno.setSpacing(0)

        campo_busca = QLineEdit()
        campo_busca.setPlaceholderText("Ação")
        campo_busca.setStyleSheet("""
            QLineEdit {
                background-color: transparent;
                color: #000000;
                font-family: 'Verdana';
                font-size: 20px;
                font-weight: normal;
                border: none;
            }
        """)

        icone_label = QLabel()
        caminho_icone_pesquisa = os.path.join(BASE, "Imagens", "icone_pesquisa.svg")
        
        
        pixmap_icone = QPixmap(caminho_icone_pesquisa).scaled(
            30, 30, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        icone_label.setPixmap(pixmap_icone)
        icone_label.setStyleSheet("background: transparent; border: none;")

        layout_busca_interno.addWidget(campo_busca)
        layout_busca_interno.addWidget(icone_label)
        # ==========================================================
        # TABELA
        # ==========================================================

        tabela = QWidget(
            paginaprincipal
        )

        tabela.setGeometry(
            275,
            251,
            1055,
            366
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
        # ==========================================================
        # SOMBRA DA TABELA
        # ==========================================================


        sombra_tabela = QGraphicsDropShadowEffect(self)
        sombra_tabela.setBlurRadius(60)
        sombra_tabela.setXOffset(0)
        sombra_tabela.setYOffset(4)
        sombra_tabela.setColor(QColor(0, 0, 0, 50))
        
        tabela.setGraphicsEffect(sombra_tabela)

        # ==========================================================
        # CABEÇALHO DA TABELA
        # ==========================================================

        cabecalho_tabela = QWidget()

        cabecalho_tabela.setFixedSize(
            1055,
            71
        )

        cabecalho_tabela.setStyleSheet("""
            QWidget {
                background-color: #356394;
                border-top-left-radius: 14px;
                border-top-right-radius: 14px;
            }
        """)

        cabecalho_layout = QHBoxLayout(
            cabecalho_tabela
        )

        cabecalho_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        cabecalho_layout.setSpacing(0)

        titulo_acao = QLabel(
            "Tipo da Ação"
        )

        titulo_tipo = QLabel(
            "Tipo"
        )

        titulo_data = QLabel(
            "Data"
        )

        titulo_acao.setFixedWidth(320)
        titulo_tipo.setFixedWidth(300)
        titulo_data.setFixedWidth(365)

        for coluna in [
            titulo_acao,
            titulo_tipo,
            titulo_data
        ]:
            coluna.setAlignment(Qt.AlignCenter)

            coluna.setStyleSheet("""
                QLabel {
                    color: #ffffff;
                    font-family: 'Verdana';
                    font-size: 24px;
                    font-weight: bold;
                    background-color: transparent;
                }
            """)

        cabecalho_layout.addWidget(
            titulo_acao
        )

        cabecalho_layout.addWidget(
            titulo_tipo
        )

        cabecalho_layout.addWidget(
            titulo_data
        )

        cabecalho_layout.addStretch()

        tabela_layout.addWidget(
            cabecalho_tabela
        )

        # ==========================================================
        # DADOS
        # ==========================================================

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
                1055,
                59
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
                        border-bottom-left-radius: 14px;
                        border-bottom-right-radius: 14px;
                    }}
                """)
            else:
                linha.setStyleSheet(f"""
                    QWidget {{
                        background-color: {fundo};
                    }}
                """)

            linha_layout = QHBoxLayout(
                linha
            )

            linha_layout.setContentsMargins(
                0,
                0,
                0,
                0
            )

            linha_layout.setSpacing(0)

            # ======================================================
            # PESQUISA
            # ======================================================

            acao = QLabel(
                dados_linha[0]
            )

            acao.setFixedWidth(320)

            acao.setAlignment(
                Qt.AlignCenter
            )

            acao.setStyleSheet("""
                QLabel {
                    color: #000000;
                    font-family: 'Verdana';
                    font-size: 22px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            # ======================================================
            # TIPO
            # ======================================================

            tipo = QWidget()

            tipo.setFixedWidth(300)

            tipo_layout = QHBoxLayout(
                tipo
            )

            tipo_layout.setContentsMargins(
                0,
                0,
                0,
                0
            )

            tipo_layout.setSpacing(12)

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
                    font-family: 'Verdana';
                    font-size: 18px;
                    font-weight: bold;
                    background-color: transparent;
                }
            """)

            artigo = QLabel(
                dados_linha[2]
            )

            artigo.setFixedWidth(220)

            artigo.setAlignment(
                Qt.AlignLeft | Qt.AlignVCenter
            )

            artigo.setStyleSheet("""
                QLabel {
                    color: #000000;
                    font-family: 'Verdana';
                    font-size: 22px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            tipo_layout.addWidget(setor)
            tipo_layout.addWidget(artigo)

            # ======================================================
            # DATA
            # ======================================================

            data = QLabel(
                dados_linha[3]
            )

            data.setFixedWidth(365)

            data.setAlignment(
                Qt.AlignCenter
            )

            data.setStyleSheet("""
                QLabel {
                    color: #000000;
                    font-family: 'Verdana';
                    font-size: 22px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            # ======================================================
            # SETA
            # ======================================================

            seta = QLabel("⌄")

            seta.setFixedWidth(70)

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

            tabela_layout.addWidget(
                linha
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ModeloTelaComite()

    window.show()

    sys.exit(app.exec())