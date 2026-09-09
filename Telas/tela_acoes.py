import sys
from PySide6.QtCore import Qt, QSize, Property, QPropertyAnimation, QEasingCurve, QRectF
from PySide6.QtGui import QFont, QPainter, QColor, QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QFrame, QTableWidget, QTableWidgetItem, QHeaderView,
    QComboBox, QAbstractButton, QSizePolicy
)

#Area dos botões interruptores com a interacao

class Interruptorzinho(QAbstractButton):
    def __init__(self, parent=None, ligado=True):
        super().__init__(parent)
        self.setCheckable(True)
        self.setChecked(ligado)
        self.setCursor(Qt.ArrowCursor)
        self.setFixedSize(46, 24)
        self.setFocusPolicy(Qt.NoFocus)

        self.setChecked(True)

        self._posicao_bolinha = 25
        self._animacao = QPropertyAnimation(self, b"posicao_bolinha", self)
        self._animacao.setDuration(150)
        self._animacao.setEasingCurve(QEasingCurve.InOutCubic)

        self.toggled.connect(self._ao_clicar)

    def _ao_clicar(self, ligado):
        self._animacao.stop()
        self._animacao.setStartValue(self._posicao_bolinha)
        self._animacao.setEndValue(25 if ligado else 3)
        self._animacao.start()

    def pegar_posicao_bolinha(self):
        return self._posicao_bolinha

    def definir_posicao_bolinha(self, pos):
        self._posicao_bolinha = pos
        self.update()

    posicao_bolinha = Property(float, pegar_posicao_bolinha, definir_posicao_bolinha)

    def paintEvent(self, event):
        pintor = QPainter(self)
        pintor.setRenderHint(QPainter.Antialiasing)
        pintor.setPen(Qt.NoPen)

        retangulo = QRectF(0, 0, self.width(), self.height())
        cor_fundo = QColor("#C9CFD8") if self.isChecked() else QColor("#058914")
        pintor.setBrush(cor_fundo)
        pintor.drawRoundedRect(retangulo, retangulo.height() / 2, retangulo.height() / 2)

        pintor.setBrush(QColor("#FFFFFF"))
        pintor.drawEllipse(int(self._posicao_bolinha), 3, 18, 18)

class Janelinha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tela_administrador_acoes_gestaoAcoes")
        self.resize(1600, 1010)
        self.setMinimumSize(1100, 650)
        self.setStyleSheet("background-color: #EEF1F5; font-family: 'Verdana';")

        painel_central = self._montar_conteudo()
        self.setCentralWidget(painel_central)

    # Texto entre os quadrados
    def _montar_conteudo(self):
        conteudo = QWidget()
        layout = QVBoxLayout(conteudo)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(20)

        titulo = QLabel("Gestão de Ações")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color: #1F2937; font-size: 26px; font-weight: 700; font-family: 'Verdana';")
        layout.addWidget(titulo)

        linha_topo = QHBoxLayout()

#Criaçao dos botões

        icone_nova_acao = QIcon("Imagens/icone_nova_acao")
        botao_nova_acao = QPushButton("Nova Ação")
        botao_nova_acao.setIcon(icone_nova_acao)
        botao_nova_acao.setIconSize(QSize(24, 24))
        botao_nova_acao.setCursor(Qt.ArrowCursor)
        botao_nova_acao.setFixedSize(186, 52)
        botao_nova_acao.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                padding: 0 20px;
                font-size: 13px;
                font-weight: 600;
                font-family: 'Verdana';
                text-align: center;
            }
           
            QPushButton:hover {
                background-color: #04620F;
            }
        """)
        botao_nova_acao.setFocusPolicy(Qt.NoFocus)
        linha_topo.addWidget(botao_nova_acao)

        icone_baixer_excel = QIcon("Imagens/icone_baixar_excel")
        botao_baixar_excel = QPushButton("Baixar em Excel")
        botao_baixar_excel.setIcon(icone_baixer_excel)
        botao_baixar_excel.setIconSize(QSize(26, 30))
        botao_baixar_excel.setCursor(Qt.ArrowCursor)
        botao_baixar_excel.setFixedSize(224, 52)
       
        botao_baixar_excel.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                border: 2px solid #D3D3D3;
                border-radius: 5px;
                color: #134593;
                padding: 0 20px;
                font-size: 13px;
                font-weight: 700;
                font-family: 'Verdana';    
                text-align: center;
                padding-left: 10px;
            }
                                     
            QPushButton:hover {
                color: #FFFFFF;
                background-color: #134593;
            }
        """)

        botao_baixar_excel.setFocusPolicy(Qt.NoFocus)
        linha_topo.addWidget(botao_baixar_excel)
        botao_baixar_excel.setFocusPolicy(Qt.NoFocus)
        linha_topo.addWidget(botao_baixar_excel)
        linha_topo.addStretch()

#espaço para busca/pesquisa

        icone_campo_pesquisa = QPixmap("Imagens/icone_lupa.png").scaled(50, 50)
        campo_pesquisa = QLineEdit()
        campo_pesquisa.setPlaceholderText("Pesquise...")
        campo_pesquisa.setFixedSize(358, 50)
        campo_pesquisa.addAction(QIcon(icone_campo_pesquisa), QLineEdit.TrailingPosition)
        campo_pesquisa.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #686868;
                border-radius: 10px;
                font-size: 20px;
                color: #B3B3B3;
                padding-left: 3px;
                font-family: 'Verdana';
            }
        """)
        campo_pesquisa.setReadOnly(True)
        campo_pesquisa.setFocusPolicy(Qt.NoFocus)
        campo_pesquisa.setCursor(Qt.ArrowCursor)
        linha_topo.addWidget(campo_pesquisa)

        layout.addLayout(linha_topo)
        layout.addWidget(self._montar_tabela())
        layout.addStretch()

        return conteudo

    def _montar_tabela(self):
        acoes = [
            "Coordenação de evento LOCAL",
            "Artigos de divulgação na mídia",
            "Produção de vídeos técnicos",
            "Elaboração do plano em marketing",
            "Cursos em pós-graduação",
            "Atendimento em visitas técnicas",
            "Representação em grupos externos",
            "Ministração de aulas/palestras",
            "Curso e-Campo juntamente com SIPT",
        ]

    # Cabeçalho de status
        tabela = QTableWidget(len(acoes), 3)
        tabela.setHorizontalHeaderLabels(["Nome", "Setor de Avaliação", "Status"])
        tabela.verticalHeader().setVisible(False)
        tabela.setShowGrid(False)
        tabela.setSelectionMode(QTableWidget.NoSelection)
        tabela.setFocusPolicy(Qt.NoFocus)
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        
    # Estilo da tabela aplicando a bordinha cinza
        tabela.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #4E73AE;
                font-size: 13px;
                color: #374151;
                font-family: 'Verdana';
            }

            QHeaderView::section:horizontal:first {
                border-top-left-radius: 5px;
            }

            QHeaderView::section:horizontal:last {
                border-top-right-radius: 5px;
            }

            QHeaderView::section {
                background-color: #3B6EA5;
                color: white;
                font-weight: 600;
                font-size: 13px;
                padding: 10px;
                border: 1px solid #3B6EA5;
                font-family: 'Verdana';
            }
        """)
        tabela.setAttribute(Qt.WA_StyledBackground, True)

        cabecalho_tabela = tabela.horizontalHeader()
        cabecalho_tabela.setSectionResizeMode(0, QHeaderView.Stretch)
        cabecalho_tabela.setSectionResizeMode(1, QHeaderView.Stretch)
        cabecalho_tabela.setSectionResizeMode(2, QHeaderView.Stretch)
        cabecalho_tabela.setDefaultAlignment(Qt.AlignCenter)
        cabecalho_tabela.setMinimumSectionSize(150)
        tabela.setColumnWidth(1, 170)
        tabela.setColumnWidth(2, 170)
        tabela.verticalHeader().setDefaultSectionSize(44)

        for linha, nome in enumerate(acoes):
            item_nome = QTableWidgetItem("   " + nome)
            item_nome.setFlags(Qt.ItemIsEnabled)
            tabela.setItem(linha, 0, item_nome)

            if linha % 2 == 1:
                item_nome.setBackground(QColor("#E9F2FF"))
            else:
                item_nome.setBackground(QColor("white"))

            combo_setor = QComboBox()
            combo_setor.addItems(["Setor", "CIPT", "SPAT", "NCO"])
            combo_setor.setFocusPolicy(Qt.NoFocus)
            combo_setor.setStyleSheet("""QComboBox{
            border: 0;
            }
            QComboBox:drop-down{
            border: none;
            }
            QComboBox:down-arrow{
            image: url(Imagens/seta_pra_baixo.png);
            }
            """)
            
            envolta1 = QWidget()
            l1 = QHBoxLayout(envolta1)
            l1.setContentsMargins(0, 0, 0, 0)
            l1.addStretch()
            l1.addWidget(combo_setor)
            l1.addStretch()
            
            if linha % 2 == 1:
                envolta1.setStyleSheet("background-color: #E9F2FF;")
                combo_setor.setStyleSheet("color: black; background-color: #E9F2FF;")
            else:
                envolta1.setStyleSheet("background-color: white;")
                combo_setor.setStyleSheet("color: black; background-color: white;")

            tabela.setCellWidget(linha, 1, envolta1)

            interruptor = Interruptorzinho(ligado=(linha % 3 != 0))
            envolta2 = QWidget()
            l2 = QHBoxLayout(envolta2)
            l2.setContentsMargins(0, 0, 0, 0)
            l2.addStretch()
            l2.addWidget(interruptor)
            l2.addStretch()
            
            if linha % 2 == 1:
                envolta2.setStyleSheet("background-color: #E9F2FF;")
            else:
                envolta2.setStyleSheet("background-color: white;")
            tabela.setCellWidget(linha, 2, envolta2)

        tabela.setAlternatingRowColors(False)

        altura_cabecalho = tabela.horizontalHeader().height()
        altura_linhas = tabela.verticalHeader().defaultSectionSize() * len(acoes)
        tabela.setFixedHeight(altura_cabecalho + altura_linhas + 2)
        tabela.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        return tabela

def principal():
    app = QApplication(sys.argv)
    app.setFont(QFont("Verdana", 10))
    janela = Janelinha()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    principal()