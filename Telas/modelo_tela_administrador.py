import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView,QMainWindow, QButtonGroup, QStackedWidget
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

from tela_pesquisador_minhas_acoes import tela_minhas_acoes

class ModeloTelaAdministrador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar ação")
        self.setFixedSize(1920, 1080)
        
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
        self.btn_calendario = btn_layout (os.path.join(BASE, "Imagens/Calendario-Icone.png"), "Calendário")
        self.btn_acoes = btn_layout (os.path.join(BASE, "Imagens/Ações-Icone.png"), "Ações")
        self.btn_empregados = btn_layout (os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Empregados")
        self.btn_validadores = btn_layout (os.path.join(BASE, "Imagens/Validadores-Icone.png"), "Validadores")

        logo_label = QLabel ()
        logo = QPixmap (LOGO)
        logo_certa = logo.scaled (220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap (logo_certa)
        logo_label.setAlignment (Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_calendario)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_acoes)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_empregados)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_validadores)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_calendario)
        self.grupo_botoes.addButton(self.btn_acoes)
        self.grupo_botoes.addButton(self.btn_empregados)
        self.grupo_botoes.addButton(self.btn_validadores)
        
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

        funcao_empregado = QLabel("Administrador", cabecalho)
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

        self.paginaprincipal = QStackedWidget(self)
        self.paginaprincipal.setGeometry(280, 70, 1600, 1010)
        self.paginaprincipal.setStyleSheet("""
            QFrame{
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px
            }
        """)

        pagina_home = QFrame()
        pagina_calendario = QFrame()
        pagina_acoes = QFrame()
        pagina_empregados = QFrame()
        pagina_validadores = QFrame()

        self.paginaprincipal.addWidget(pagina_home)
        self.paginaprincipal.addWidget(pagina_calendario)
        self.paginaprincipal.addWidget(pagina_acoes)
        self.paginaprincipal.addWidget(pagina_empregados)
        self.paginaprincipal.addWidget(pagina_validadores)

        self.btn_home.clicked.connect(
            lambda: self.paginaprincipal.setCurrentIndex(0)
        )

        self.btn_calendario.clicked.connect(
            lambda: self.paginaprincipal.setCurrentIndex(1)
        )

        self.btn_acoes.clicked.connect(
            lambda: self.paginaprincipal.setCurrentIndex(2)
        )

        self.btn_empregados.clicked.connect(
            lambda: self.paginaprincipal.setCurrentIndex(3)
        )

        self.btn_validadores.clicked.connect(
            lambda: self.paginaprincipal.setCurrentIndex(4)
        )

        self.paginaprincipal.setCurrentIndex(0)

        # titulo = QLabel("Título", paginaprincipal)
        # titulo.setAlignment(Qt.AlignCenter)
        # titulo.setGeometry(820, 80, 150, 50)
        # titulo.setStyleSheet("""
        #     QLabel{
        #         font-size: 36px;
        #     }
        # """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaAdministrador()
    window.show()
    sys.exit(app.exec())