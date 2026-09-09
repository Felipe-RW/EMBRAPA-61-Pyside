import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QColor, QBrush
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup, QCheckBox, QTableWidgetItem,QTableWidget
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

        nome_tela = QLabel("Validadores", cabecalho)
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

        self.paginaprincipal = QFrame(self)
        self.paginaprincipal.setGeometry(280, 70, 1600, 1010)
        self.paginaprincipal.setStyleSheet("""
            QFrame{
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px
            }
        """)

        titulo = QLabel("Validadores", self.paginaprincipal)
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setGeometry(675, 40, 250, 50)
        titulo.setStyleSheet("""
            QLabel{
                font-size: 36px;
                color: #000000;
            }
        """)

        self.conteudo_pagina()

    def conteudo_pagina(self):

        fundo = QFrame(self.paginaprincipal)
        fundo.setFrameShape(QFrame.Shape.NoFrame)
        fundo.setGeometry(50, 120, 1500, 840) 
        fundo.setStyleSheet("QFrame { background-color: transparent; }")

        layout_interno = QVBoxLayout(fundo)
        layout_interno.setContentsMargins(0, 0, 0, 0)
        layout_interno.setAlignment(Qt.AlignmentFlag.AlignTop)


        sublayou_interno_superior= QHBoxLayout()
        sublayou_interno_superior.setContentsMargins(0, 0, 0, 0)
        sublayou_interno_superior.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        novo_setor= QPushButton("Novo setor")
        novo_setor.setFixedSize(186,52)
        novo_setor.setStyleSheet("""
            QPushButton{
                background-color: #058914;
                border-radius: 5px;
                border: none;
                color: #ffffff;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #04620F;
                cursor: pointer;
            }
            QPushButton:pressed {
                background-color: #04620F;
            }
        """)
        sublayou_interno_superior.addWidget(novo_setor)

        sublayou_interno_superior.addStretch()
        
        barra_pesquisa= QLineEdit()
        barra_pesquisa.setPlaceholderText("Pesquise...")
        barra_pesquisa.setFixedSize(358,50)
        barra_pesquisa.setStyleSheet("""
            QLineEdit{
                background-color: #ffffff;
                border-radius: 5px;
                border: 1px solid;
                border-color: #686868;
                color: #B3B3B3;
                font-size: 20 px;
                font-weight: italic;
            }
        """)
        sublayou_interno_superior.addWidget(barra_pesquisa)



        
        sublayou_interno_inferior= QVBoxLayout()
        sublayou_interno_inferior.setContentsMargins(0, 0, 0, 0)

        quant_linhas= 5




        lista_setores = ["SPT", "SPIT", "NCO"]
        quant_linhas = len(lista_setores)

        tabela_setores = QTableWidget(fundo)
        tabela_setores.setFixedSize(1500, 500) 
        tabela_setores.setContentsMargins(0,0,0,0)
        tabela_setores.setColumnCount(2)     
        tabela_setores.setRowCount(quant_linhas)        

        tabela_setores.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        tabela_setores.setFocusPolicy(Qt.FocusPolicy.NoFocus)                     
        tabela_setores.setSelectionMode(QTableWidget.SelectionMode.NoSelection)   
        tabela_setores.setShowGrid(True) 
        
        tabela_setores.setAlternatingRowColors(True)

        tabela_setores.horizontalHeader().setVisible(True)
        tabela_setores.verticalHeader().setVisible(False)
        tabela_setores.setHorizontalHeaderLabels(["Setor", "Status"])
        tabela_setores.setColumnWidth(0, 750) 

        tabela_setores.setColumnWidth(1, 750) 

        tabela_setores.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        tabela_setores.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        tabela_setores.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff; /* Cor padrão para as linhas PARES (ex: SPT, NCO) */
                border: none;
                color: #000000;      
                font-size: 20px;     
                font-weight: bold;   
            }
            QTableWidget::item:alternate {
                background-color: #E9F2FF;
            }
            QTableWidget::item:selected {
                background-color: transparent;
            }
            QHeaderView::section {
                background-color: #356394;
                color: #ffffff;
                font-size: 22px;
                font-weight: bold;
                border: none;
                height: 60px;
            }
        """)

        for indice, nome_do_setor in enumerate(lista_setores):
            tabela_setores.setRowHeight(indice, 89)

            item_setor = QTableWidgetItem(nome_do_setor)
            item_setor.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_setor.setFlags(Qt.ItemFlag.ItemIsEnabled)
            tabela_setores.setItem(indice, 0, item_setor) 

            container_switch = QWidget()
            
            if indice % 2 != 0:
                container_switch.setStyleSheet("background-color: #E9F2FF; border: none; margin: 0px;")
            else:
                container_switch.setStyleSheet("background-color: #ffffff; border: none; margin: 0px;")
            
            layout_switch = QHBoxLayout(container_switch)
            layout_switch.setContentsMargins(0, 0, 0, 0) 
            layout_switch.setSpacing(0)
            layout_switch.setAlignment(Qt.AlignmentFlag.AlignCenter) 

            botao_switch = QCheckBox()
            botao_switch.setStyleSheet("background-color: transparent; border: none;") 
            
            layout_switch.addWidget(botao_switch)
            tabela_setores.setCellWidget(indice, 1, container_switch) 
        
        sublayou_interno_inferior.addWidget(tabela_setores, alignment=Qt.AlignmentFlag.AlignHCenter)
        sublayou_interno_inferior.addStretch()

















        layout_interno.addLayout(sublayou_interno_superior)
        layout_interno.addLayout(sublayou_interno_inferior)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaAdministrador()
    window.show()
    sys.exit(app.exec())
