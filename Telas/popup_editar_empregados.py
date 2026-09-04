from pathlib import Path
import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QCheckBox,
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")
caminho_check = Path(BASE) / "Imagens" / "check.png"

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

        self.btn_home = btn_layout(os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_calendario = btn_layout(os.path.join(BASE, "Imagens/Calendario-Icone.png"), "Calendário")
        self.btn_acoes = btn_layout(os.path.join(BASE, "Imagens/Ações-Icone.png"), "Ações")
        self.btn_empregados = btn_layout(os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Empregados")
        self.btn_validadores = btn_layout(os.path.join(BASE, "Imagens/Validadores-Icone.png"), "Validadores")

        logo_label = QLabel()
        logo = QPixmap(LOGO)
        logo_certa = logo.scaled(220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_certa)
        logo_label.setAlignment(Qt.AlignLeft)
        
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

        nome_tela = QLabel("Empregados", cabecalho)
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
                border-top-right-radius: 20px;
            }
        """)

        titulo = QLabel("Editar Empregado", paginaprincipal)
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setGeometry(550, 40, 400, 50)
        titulo.setStyleSheet("""
            QLabel{
                font-size: 36px;
            }
        """)

        card_popup = QFrame(paginaprincipal)
        card_popup.setGeometry(75, 150, 1436, 694)
        card_popup.setStyleSheet("""
            QFrame {
                background-color: #92C498;
                border-radius: 20px;
            }
            QLabel {
                background-color: transparent;
            }
        """)

        caminho_check = Path(__file__).resolve().parent.parent / "Imagens" / "check.png"

        self.texto_nome = QLabel(card_popup)
        self.texto_nome.setGeometry(20, 15, 300, 50)
        self.texto_nome.setText("Nome do Empregado:")
        self.texto_nome.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        self.campo_nome = QLineEdit(card_popup)
        self.campo_nome.setGeometry(20, 80, 1376, 92)
        self.campo_nome.setPlaceholderText("Digite o nome:")
        self.campo_nome.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #4A4A4A;
                border-radius: 20px;
                font-family: Verdana;
                font-weight: bold;
                font-size: 20px;
                padding-left: 15px;
            }
        """)

        self.texto_email = QLabel(card_popup)
        self.texto_email.setGeometry(20, 205, 300, 50)
        self.texto_email.setText("Email do Empregado:")
        self.texto_email.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        self.campo_email = QLineEdit(card_popup)
        self.campo_email.setGeometry(20, 265, 1376, 92)
        self.campo_email.setPlaceholderText("Digite o email:")
        self.campo_email.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #4A4A4A;
                border-radius: 20px;
                font-family: Verdana;
                font-weight: bold;
                font-size: 20px;
                padding-left: 15px;
            }
        """)

        self.texto_funcao = QLabel(card_popup)
        self.texto_funcao.setGeometry(20, 417, 210, 50)
        self.texto_funcao.setText("Tipo de função:")
        self.texto_funcao.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        self.checkbox_administrador = QCheckBox("Administrador", card_popup)
        self.checkbox_administrador.setGeometry(1190, 395, 200, 100)
        self.checkbox_administrador.setStyleSheet(f"""
            QCheckBox {{
                color: black;
                font-size: 20px;
                font-family: Verdana;
                font-weight: bold;
                background-color: transparent;
            }}
            QCheckBox::indicator {{
                width: 24px;
                height: 24px;
                background-color: white;
                border: 1px solid #333333;
                border-radius: 10px;
            }}
            QCheckBox::indicator:checked {{
                background-color: #7DA883;
                image: url("{caminho_check.as_posix()}");
            }}
        """)

        self.dropdown_validador = QComboBox(card_popup)
        self.dropdown_validador.addItems(["SPAT", "SPIT", "NCO"])
        self.dropdown_validador.setCurrentIndex(-1)
        self.dropdown_validador.setPlaceholderText("Avaliadores")
        self.dropdown_validador.setGeometry(570, 417, 220, 45)
        self.dropdown_validador.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 18px;
                font-family: Verdana;
                font-weight: bold;
                border-radius: 0px;
                border: 1px solid gray;
                background-color: white;
            }
            QComboBox QAbstractItemView {
                color: black;
                background-color: white;
                selection-background-color: #92C498;
                selection-color: black;
                border: 1px solid gray;
            }
        """)

        self.checkbox_comite = QCheckBox("Comitê", card_popup)
        self.checkbox_comite.setGeometry(910, 395, 200, 100)
        self.checkbox_comite.setStyleSheet(f"""
            QCheckBox {{
                color: black;
                font-size: 20px;
                font-family: Verdana;
                font-weight: bold;
                background-color: transparent;
            }}
            QCheckBox::indicator {{
                width: 24px;
                height: 24px;
                background-color: white;
                border: 1px solid #333333;
                border-radius: 10px;
            }}
            QCheckBox::indicator:checked {{
                background-color: #7DA883;
                image: url("{caminho_check.as_posix()}");
            }}
        """)

        self.checkbox_pesquisador = QCheckBox("Pesquisador", card_popup)
        self.checkbox_pesquisador.setGeometry(290, 395, 200, 100)
        self.checkbox_pesquisador.setStyleSheet(f"""
            QCheckBox {{
                color: black;
                font-size: 20px;
                font-family: Verdana;
                font-weight: bold;
                background-color: transparent;
            }}
            QCheckBox::indicator {{
                width: 24px;
                height: 24px;
                background-color: white;
                border: 1px solid #333333;
                border-radius: 10px;
            }}
            QCheckBox::indicator:checked {{
                background-color: #7DA883;
                image: url("{caminho_check.as_posix()}");
            }}
        """)

        self.botao_cancelar = QPushButton("Cancelar", card_popup)
        self.botao_cancelar.setGeometry(20, 545, 563, 67)
        self.botao_cancelar.setStyleSheet("""
            QPushButton {
                background-color: #134593;
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-family: Verdana;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0C2750;
            }
            QPushButton:pressed {
                background-color: #0C2750;
            }
        """)

        self.botao_editar = QPushButton("Editar", card_popup)
        self.botao_editar.setGeometry(830, 545, 563, 67)
        self.botao_editar.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-family: Verdana;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #04620F;
            }
            QPushButton:pressed {
                background-color: #04620F;
            }
        """)


if __name__ == "__main__": #Isso é só pra rodar o código
    app = QApplication(sys.argv)
    window = ModeloTelaAdministrador()
    window.show()
    sys.exit(app.exec())