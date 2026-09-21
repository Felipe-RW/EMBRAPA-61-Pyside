import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QColor, QRegion, QPainterPath
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

        menuLateral = QWidget(self)
        menuLateral.setGeometry(0, 0, 280, 1080)
        menuLateral.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        menuLateralLayout = QVBoxLayout(menuLateral)
        menuLateralLayout.setContentsMargins(30, 0, 0, 0)

        self.btn_home = btn_layout (os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_calendario = btn_layout (os.path.join(BASE, "Imagens/Calendario-Icone.png"), "Calendário")
        self.btn_acoes = btn_layout (os.path.join(BASE, "Imagens/Ações-Icone.png"), "Ações")
        self.btn_empregados = btn_layout (os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Empregados")
        self.btn_validadores = btn_layout (os.path.join(BASE, "Imagens/Validadores-Icone.png"), "Validadores")

        logoLabel = QLabel ()
        logo = QPixmap (LOGO)
        logoCerta = logo.scaled (220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logoLabel.setPixmap (logoCerta)
        logoLabel.setAlignment (Qt.AlignLeft)
        
        menuLateralLayout.addWidget(logoLabel)
        menuLateralLayout.addWidget(self.btn_home)
        menuLateralLayout.setSpacing(5)
        menuLateralLayout.addWidget(self.btn_calendario)
        menuLateralLayout.setSpacing(5)
        menuLateralLayout.addWidget(self.btn_acoes)
        menuLateralLayout.setSpacing(5)
        menuLateralLayout.addWidget(self.btn_empregados)
        menuLateralLayout.setSpacing(5)
        menuLateralLayout.addWidget(self.btn_validadores)
            
        self.grupoBotoes = QButtonGroup(self)
        self.grupoBotoes.setExclusive(True)
        self.grupoBotoes.addButton(self.btn_home)
        self.grupoBotoes.addButton(self.btn_calendario)
        self.grupoBotoes.addButton(self.btn_acoes)
        self.grupoBotoes.addButton(self.btn_empregados)
        self.grupoBotoes.addButton(self.btn_validadores)
        
        menuLateralLayout.addStretch()

        cabecalho = QWidget(self)
        cabecalho.setGeometry(280, 0, 1640, 70)
        cabecalho.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        nomeEmpregado = QLabel("Fulano da Silva Rodrigues", cabecalho)
        nomeEmpregado.setGeometry(35, 22, 400, 30)
        nomeEmpregado.setStyleSheet("""
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

        funcaoEmpregado = QLabel("Administrador", cabecalho)
        funcaoEmpregado.setGeometry(470, 22, 200, 30)
        funcaoEmpregado.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 24px
            }
        """)

        nomeTela = QLabel("Validadores", cabecalho)
        nomeTela.setGeometry(1000, 22, 300, 30)
        nomeTela.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter
            }
        """)

        botaoLogout = QPushButton("Logout", cabecalho)
        botaoLogout.setGeometry(1450, 15, 150, 40)
        botaoLogout .setStyleSheet("""
            QPushButton{
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }
        """)

        self.paginaPrincipal = QFrame(self)
        self.paginaPrincipal.setGeometry(280, 70, 1600, 1010)
        self.paginaPrincipal.setStyleSheet("""
            QFrame{
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px
            }
        """)

        titulo = QLabel("Validadores", self.paginaPrincipal)
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
        fundo = QFrame(self.paginaPrincipal)
        fundo.setFrameShape(QFrame.Shape.NoFrame)
        fundo.setGeometry(50, 120, 1500, 840) 
        fundo.setStyleSheet("QFrame { background-color: transparent; }")

        layoutInterno = QVBoxLayout(fundo)
        layoutInterno.setContentsMargins(0, 0, 0, 0)
        layoutInterno.setAlignment(Qt.AlignmentFlag.AlignTop)

        sublayouInternoSuperior = QHBoxLayout()
        sublayouInternoSuperior.setContentsMargins(0, 0, 0, 0)
        sublayouInternoSuperior.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        novoSetor = QPushButton("Novo setor")
        novoSetor.setFixedSize(186, 52)
        novoSetor.setStyleSheet("""
            QPushButton {
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
        sublayouInternoSuperior.addWidget(novoSetor)

        sublayouInternoSuperior.addStretch()
        
        barraPesquisa = QLineEdit()
        barraPesquisa.setPlaceholderText("Pesquise...")
        barraPesquisa.setFixedSize(358, 50)
        barraPesquisa.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border-radius: 5px;
                border: 1px solid;
                border-color: #686868;
                color: #B3B3B3;
                font-size: 20px;
                font-weight: italic;
            }
        """)
        sublayouInternoSuperior.addWidget(barraPesquisa)

        sublayouInternoInferior = QVBoxLayout()
        sublayouInternoInferior.setContentsMargins(0, 100, 0, 0)

        listaSetores = ["SPT", "SPIT", "NCO"]
        quantLinhas = len(listaSetores)

        tabelaSetores = QTableWidget(fundo)
        tabelaSetores.setFixedSize(1500, 500) 
        tabelaSetores.setContentsMargins(0, 0, 0, 0)
        tabelaSetores.setColumnCount(2)     
        tabelaSetores.setRowCount(quantLinhas)        

        tabelaSetores.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        tabelaSetores.setFocusPolicy(Qt.FocusPolicy.NoFocus)                     
        tabelaSetores.setSelectionMode(QTableWidget.SelectionMode.NoSelection)   
        tabelaSetores.setShowGrid(True) 
        
        tabelaSetores.setAlternatingRowColors(False)

        tabelaSetores.horizontalHeader().setVisible(True)
        tabelaSetores.verticalHeader().setVisible(False)
        tabelaSetores.setHorizontalHeaderLabels(["Setor", "Status"])
        tabelaSetores.setColumnWidth(0, 750) 
        tabelaSetores.setColumnWidth(1, 750) 

        tabelaSetores.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        tabelaSetores.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # O seletor QTableWidget::item:hover foi removido para tirar o efeito de hover
        tabelaSetores.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                border: none;
                font-size: 20px;     
                font-weight: bold;
                border-radius: 15px;
            }
            
            QHeaderView {
                background-color: transparent;
                border-top-left-radius: 15px;
                border-top-right-radius: 15px;
                border: none;
            }

            QHeaderView::section:horizontal:first {
                border-top-left-radius: 15px;
            }
            QHeaderView::section:horizontal:last {
                border-top-right-radius: 15px;
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

        for indice, nome_do_setor in enumerate(listaSetores):
            tabelaSetores.setRowHeight(indice, 89)

            item_setor = QTableWidgetItem(nome_do_setor)
            item_setor.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_setor.setFlags(Qt.ItemFlag.ItemIsEnabled)
            
            # CORES INVERTIDAS: Ímpares (1, 3...) recebem azul e Pares (0, 2...) recebem branco
            if indice % 2 != 0:
                cor_fundo = "#E9F2FF"  # Ímpar (Azul)
            else:
                cor_fundo = "#ffffff"  # Par (Branco)

            # Aplica a cor de fundo no texto do setor (Coluna 0)
            item_setor.setBackground(QColor(cor_fundo))
            tabelaSetores.setItem(indice, 0, item_setor) 

            # Aplica a mesma cor de fundo no container do Switch (Coluna 1)
            container_switch = QFrame()
            container_switch.setStyleSheet(f"""
                QFrame {{
                    background-color: {cor_fundo}; 
                    border-radius: 0px;
                }}
            """)
            
            layoutSwitch = QHBoxLayout(container_switch)
            layoutSwitch.setContentsMargins(0, 0, 0, 0) 
            layoutSwitch.setSpacing(0)
            layoutSwitch.setAlignment(Qt.AlignmentFlag.AlignCenter) 

            botaoSwitch = QCheckBox()
            botaoSwitch.setStyleSheet("background-color: transparent; border: none;") 
            
            layoutSwitch.addWidget(botaoSwitch)
            tabelaSetores.setCellWidget(indice, 1, container_switch)

        sublayouInternoInferior.addWidget(tabelaSetores, alignment=Qt.AlignmentFlag.AlignHCenter)
        sublayouInternoInferior.addStretch()

        layoutInterno.addLayout(sublayouInternoSuperior)
        layoutInterno.addLayout(sublayouInternoInferior)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaAdministrador()
    window.show()
    sys.exit(app.exec())
