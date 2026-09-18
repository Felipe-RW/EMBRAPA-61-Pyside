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

class ModeloTelaAdministrador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar ação")
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

        funcao_empregado = QLabel("Pesquisador", cabecalho)
        funcao_empregado.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        funcao_empregado.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 24px;
            }

        """)

        nome_tela = QLabel("Nome da Tela", cabecalho)
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

        frame_principal = QFrame(self)
        frame_principal.setFixedWidth(1600)
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


        # As seguintes linhas de código são apenas para exemplo, seu código vai ser colocado seguindo esse exemplo:
        # titulo = QLabel("Título", frame_principal)
        # titulo.setAlignment(Qt.AlignCenter)
        # titulo.setGeometry(760, 40, 150, 50)
        # titulo.setStyleSheet("""
        #     QLabel{
        #         font-size: 36px;

        #     }

        # """)

        layout_pagina.addWidget(cabecalho)
        layout_pagina.addWidget(frame_principal)

        layout_principal.addWidget(menu_lateral)
        layout_principal.addWidget(pagina_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaAdministrador()
    window.showMaximized()
    sys.exit(app.exec())