import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView,QMainWindow, QButtonGroup,
    QScrollArea, QSizePolicy
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

class TelaListaColaboradores(QMainWindow):
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
        
        menu_lateral = QWidget(self)
        menu_lateral.setFixedWidth(280)
        menu_lateral.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)
        menu_lateral_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.btn_home = btn_layout (os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_empregados = btn_layout (os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Pesquisadores")

        logo_label = QLabel ()
        logo = QPixmap (LOGO)
        logo_certa = logo.scaled (220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap (logo_certa)
        logo_label.setAlignment (Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_empregados)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_empregados)
        
        menu_lateral_layout.addStretch()
        

        pagina_principal = QWidget()
        layout_pagina = QVBoxLayout(pagina_principal)
        layout_pagina.setContentsMargins(0, 0, 0, 0)
        layout_pagina.setSpacing(0)
    

        cabecalho = QWidget(self)
        cabecalho.setFixedSize(1640, 70)
        cabecalho.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        cabecalho_layout = QHBoxLayout(cabecalho)
        cabecalho_layout.setContentsMargins(40, 0, 40, 0)
        

        nome_empregado = QLabel("Fulano da Silva Rodrigues", cabecalho)
        nome_empregado.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        nome_empregado.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }
        """)

        separador = QLabel("|", cabecalho)
        separador.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        separador.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }

        """)

        funcao_empregado = QLabel("Comitê", cabecalho)
        funcao_empregado.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        funcao_empregado.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 24px;
            }

        """)

        nome_tela = QLabel("Funcionários", cabecalho)
        nome_tela.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        nome_tela.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter
            }

        """)

        botao_logout = QPushButton("Logout", cabecalho)
        botao_logout.setFixedSize(150, 40)
        botao_logout.setCursor(Qt.PointingHandCursor)
        botao_logout.setStyleSheet("""
            QPushButton{
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }

            QPushButton:hover{
                background-color: #8E8E93;
                color: #FFFFFF;
                cursor: pointer;
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

        # A página branca (frame_principal) segue a resolução do Figma: 1609x1010
        LARGURA_FRAME = 1609

        frame_principal = QFrame(self)
        frame_principal.setFixedWidth(LARGURA_FRAME)
        frame_principal.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        frame_principal.setContentsMargins(0, 0, 0, 0)
        frame_principal.setStyleSheet("""
            QFrame{
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
            }

        """)


        frame_principal_layout = QVBoxLayout(frame_principal)
        frame_principal_layout.setAlignment(Qt.AlignTop)

        # ===================== CONTEÚDO DA PÁGINA =====================
        # Coordenadas calculadas a partir do Figma (frame de 1609x1010),
        # usando setGeometry para reproduzir o design com precisão.

        titulo = QLabel("Lista de colaboradores", frame_principal)
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setGeometry(0, 45, LARGURA_FRAME, 50)
        titulo.setStyleSheet("""
            QLabel{
                font-size: 28px;
                color: #08175C;
                background-color: transparent;
            }
        """)

        MARGEM_LATERAL = 116

        nome_colaborador = QLabel("Fulano Da Silva", frame_principal)
        nome_colaborador.setGeometry(MARGEM_LATERAL, 156, 320, 34)
        nome_colaborador.setStyleSheet("""
            QLabel{
                font-size: 18px;
                color: #08175C;
                background-color: transparent;
            }
        """)

        LARGURA_BUSCA = 358
        ALTURA_BUSCA = 39

        campo_busca = QLineEdit(frame_principal)
        campo_busca.setPlaceholderText("Ação")
        campo_busca.setGeometry(
            LARGURA_FRAME - MARGEM_LATERAL - LARGURA_BUSCA, 153,
            LARGURA_BUSCA, ALTURA_BUSCA
        )
        campo_busca.setStyleSheet("""
            QLineEdit{
                font-weight: normal;
                font-size: 14px;
                color: #08175C;
                background-color: #ffffff;
                border: 1px solid #C7C7CC;
                border-radius: 8px;
                padding-left: 12px;
                padding-right: 12px;
            }
        """)
        # Adicione aqui o seu próprio ícone de pesquisa (ex.: um QAction no
        # QLineEdit ou um QLabel posicionado sobre o campo).

        # ---- Tabela ----

        MARGEM_ESQUERDA_TABELA = 277
        TOPO_TABELA = 256
        LARGURA_TABELA = 1060
        ALTURA_LINHA = 60

        COL_ACAO = 375
        COL_TIPO = 306
        COL_DATA = 285
        COL_SETA = LARGURA_TABELA - COL_ACAO - COL_TIPO - COL_DATA

        # Substitua esta lista pelos dados reais vindos do seu banco/backend.
        dados_colaboradores = [
            {"acao": "Pesquisa 1", "setor": "Setor", "tipo": "Artigo Científico", "data": "23/03/2026"},
            {"acao": "Pesquisa 2", "setor": "Setor", "tipo": "Artigo Científico", "data": "29/04/2026"},
            {"acao": "Pesquisa 3", "setor": "Setor", "tipo": "Artigo Científico", "data": "22/06/2026"},
            {"acao": "Pesquisa 4", "setor": "Setor", "tipo": "Artigo Científico", "data": "23/07/2026"},
            {"acao": "Pesquisa 5", "setor": "Setor", "tipo": "Artigo Científico", "data": "29/08/2026"},
        ]

        altura_tabela = ALTURA_LINHA * (len(dados_colaboradores) + 1)

        tabela = QWidget(frame_principal)
        tabela.setGeometry(MARGEM_ESQUERDA_TABELA, TOPO_TABELA, LARGURA_TABELA, altura_tabela)
        tabela_layout = QVBoxLayout(tabela)
        tabela_layout.setContentsMargins(0, 0, 0, 0)
        tabela_layout.setSpacing(0)

        cabecalho_tabela = QWidget(tabela)
        cabecalho_tabela.setFixedHeight(ALTURA_LINHA)
        cabecalho_tabela.setStyleSheet("""
            QWidget{
                background-color: #356394;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
        """)
        cabecalho_tabela_layout = QHBoxLayout(cabecalho_tabela)
        cabecalho_tabela_layout.setContentsMargins(0, 0, 0, 0)
        cabecalho_tabela_layout.setSpacing(0)

        col_tipo_acao = QLabel("Tipo da Ação")
        col_tipo = QLabel("Tipo")
        col_data = QLabel("Data")
        col_tipo_acao.setFixedWidth(COL_ACAO)
        col_tipo.setFixedWidth(COL_TIPO)
        col_data.setFixedWidth(COL_DATA)
        for col in (col_tipo_acao, col_tipo, col_data):
            col.setAlignment(Qt.AlignCenter)
            col.setStyleSheet("""
                QLabel{
                    color: #ffffff;
                    font-size: 20px;
                    background-color: transparent;
                }
            """)

        cabecalho_tabela_layout.addWidget(col_tipo_acao)
        cabecalho_tabela_layout.addWidget(col_tipo)
        cabecalho_tabela_layout.addWidget(col_data)
        cabecalho_tabela_layout.addStretch()

        tabela_layout.addWidget(cabecalho_tabela)

        for indice, item in enumerate(dados_colaboradores):
            cor_fundo = "#ffffff" if indice % 2 == 0 else "#EAF2FB"
            ultima_linha = indice == len(dados_colaboradores) - 1

            linha = QWidget(tabela)
            linha.setFixedHeight(ALTURA_LINHA)
            estilo_borda = (
                "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;"
                if ultima_linha else ""
            )
            linha.setStyleSheet(f"""
                QWidget{{
                    background-color: {cor_fundo};
                    {estilo_borda}
                }}
            """)

            linha_layout = QHBoxLayout(linha)
            linha_layout.setContentsMargins(0, 0, 0, 0)
            linha_layout.setSpacing(0)

            label_acao = QLabel(item["acao"])
            label_acao.setFixedWidth(COL_ACAO)
            label_acao.setAlignment(Qt.AlignCenter)
            label_acao.setStyleSheet("""
                QLabel{
                    color: #08175C;
                    font-size: 17px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            container_tipo = QWidget()
            container_tipo.setFixedWidth(COL_TIPO)
            container_tipo.setStyleSheet("QWidget{background-color: transparent;}")
            container_tipo_layout = QHBoxLayout(container_tipo)
            container_tipo_layout.setContentsMargins(0, 0, 0, 0)
            container_tipo_layout.setAlignment(Qt.AlignCenter)

            label_setor = QLabel(item["setor"])
            label_setor.setStyleSheet("""
                QLabel{
                    color: #8E8E93;
                    font-size: 17px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            label_tipo = QLabel(item["tipo"])
            label_tipo.setStyleSheet("""
                QLabel{
                    color: #08175C;
                    font-size: 17px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            container_tipo_layout.addWidget(label_setor)
            container_tipo_layout.addSpacing(14)
            container_tipo_layout.addWidget(label_tipo)

            label_data = QLabel(item["data"])
            label_data.setFixedWidth(COL_DATA)
            label_data.setAlignment(Qt.AlignCenter)
            label_data.setStyleSheet("""
                QLabel{
                    color: #08175C;
                    font-size: 17px;
                    font-weight: normal;
                    background-color: transparent;
                }
            """)

            container_seta = QWidget()
            container_seta.setFixedWidth(COL_SETA)
            container_seta.setStyleSheet("QWidget{background-color: transparent;}")
            container_seta_layout = QHBoxLayout(container_seta)
            container_seta_layout.setContentsMargins(0, 0, 20, 0)
            container_seta_layout.setAlignment(Qt.AlignCenter)

            botao_expandir = QPushButton("⌄")
            botao_expandir.setFixedSize(36, 36)
            botao_expandir.setCursor(Qt.PointingHandCursor)
            botao_expandir.setStyleSheet("""
                QPushButton{
                    color: #08175C;
                    font-size: 20px;
                    background-color: transparent;
                    border: none;
                }
            """)
            # Conecte aqui a ação de expandir a linha, por exemplo:
            # botao_expandir.clicked.connect(lambda _, i=indice: self.expandir_linha(i))
            container_seta_layout.addWidget(botao_expandir)

            linha_layout.addWidget(label_acao)
            linha_layout.addWidget(container_tipo)
            linha_layout.addWidget(label_data)
            linha_layout.addWidget(container_seta)

            tabela_layout.addWidget(linha)

        # ===================== FIM DO CONTEÚDO =====================

        layout_pagina.addWidget(cabecalho)
        layout_pagina.addWidget(frame_principal)

        layout_principal.addWidget(menu_lateral)
        layout_principal.addWidget(pagina_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaListaColaboradores()
    window.showMaximized()
    sys.exit(app.exec())