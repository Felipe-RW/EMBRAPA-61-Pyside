import sys
from PySide6.QtCore import Qt, QSize, Property, QPropertyAnimation, QEasingCurve, QRectF
from PySide6.QtGui import QFont, QPainter, QColor, QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView,
    QComboBox, QAbstractButton, QSizePolicy
)

# área dos botões interruptores com a interacao
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
        cor_fundo = QColor("#3B6EA5") if self.isChecked() else QColor("#C9CFD8")
        pintor.setBrush(cor_fundo)
        pintor.drawRoundedRect(retangulo, retangulo.height() / 2, retangulo.height() / 2)

        pintor.setBrush(QColor("#FFFFFF"))
        pintor.drawEllipse(int(self._posicao_bolinha), 3, 18, 18)


class Janelinha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela")
        self.resize(1400, 760)
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

        # Criação dos butao
        botao_nova_acao = QPushButton("Nova Ação")
        botao_nova_acao.setCursor(Qt.ArrowCursor)
        botao_nova_acao.setFixedHeight(38)
        botao_nova_acao.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                padding: 0 20px;
                font-size: 13px;
                font-weight: 600;
                font-family: 'Verdana';
            }
            QPushButton:hover { background-color: #349041; }
        """)
        botao_nova_acao.setFocusPolicy(Qt.NoFocus)
        linha_topo.addWidget(botao_nova_acao)

        botao_baixar_excel = QPushButton("Baixar em Excel")
        icone = QIcon("Imagens/office.png")
        botao_baixar_excel.setIcon(icone)
        botao_baixar_excel.setIconSize(QSize(18, 18))
        botao_baixar_excel.setCursor(Qt.ArrowCursor)
        botao_baixar_excel.setFixedHeight(38)
        
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
                text-align: left;
                padding-left: 10px;
            }
            QPushButton:hover { background-color: #349041; }
        """)

        botao_baixar_excel.setFocusPolicy(Qt.NoFocus)
        linha_topo.addWidget(botao_baixar_excel)
        linha_topo.addStretch()

    # Espaço para busca/pesquisa
        campo_pesquisa = QLineEdit()
        campo_pesquisa.setPlaceholderText("Pesquise...")
        campo_pesquisa.setFixedWidth(260)
        campo_pesquisa.setFixedHeight(32)
        campo_pesquisa.setStyleSheet("""
            QLineEdit {
                border: none;
                border-bottom: 1px solid #B7C0CC;
                font-size: 13px;
                color: #4B5563;
                padding-left: 4px;
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
        tabela.setHorizontalHeaderLabels(["Nome da Ação", "Setor de Avaliação", "Status da Ação"])
        tabela.verticalHeader().setVisible(False)
        tabela.setShowGrid(False)
        tabela.setSelectionMode(QTableWidget.NoSelection)
        tabela.setFocusPolicy(Qt.NoFocus)
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        
    # Estilo da tabela aplicando a bordinha cinza
        tabela.setStyleSheet("""
            QTableWidget {
                background-color: white;
<<<<<<< HEAD
                border: 1px solid #D1D5DB;
                border-radius: 16px;
=======
                border: 1px solid #356394;
                border-radius: 20px;
>>>>>>> 14523cf01e7c89b0edd0628b51fd00eaf8dcd4c9
                font-size: 13px;
                color: #374151;
                font-family: 'Verdana';
            }

            QTableWidgetItem {
                background-color: #E9F2FF;
<<<<<<< HEAD
                color: #000000;
=======
                color: #00000;
>>>>>>> 14523cf01e7c89b0edd0628b51fd00eaf8dcd4c9
            }

            QHeaderView::section {
                background-color: #3B6EA5;
                color: white;
                font-weight: 600;
                font-size: 13px;
                padding: 10px;
                border: none;

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
                item_nome.setBackground(QColor("white"))
            else:
                item_nome.setBackground(QColor("#E9F2FF"))

            combo_setor = QComboBox()
            combo_setor.addItems(["Setor", "Comunicação", "Pesquisa", "Administrativo"])
<<<<<<< HEAD
=======
            combo_setor.setStyleSheet("""
                QComboBox {
                    border: none;
                    color: #6B7280;
                    font-size: 13px;
                    background: #FFFFFF;
                    font-family: 'Verdana';
                }
            """)

>>>>>>> 14523cf01e7c89b0edd0628b51fd00eaf8dcd4c9
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
                envolta1.setStyleSheet("background-color: white;")
            else:
<<<<<<< HEAD
                envolta1.setStyleSheet("background-color: #E9F2FF;")
=======
                envolta1.setStyleSheet("""
                    background-color: #E9F2FF;
                """)
>>>>>>> 14523cf01e7c89b0edd0628b51fd00eaf8dcd4c9
            tabela.setCellWidget(linha, 1, envolta1)

            interruptor = Interruptorzinho(ligado=(linha % 3 != 0))
            envolta2 = QWidget()
            l2 = QHBoxLayout(envolta2)
            l2.setContentsMargins(0, 0, 0, 0)
            l2.addStretch()
            l2.addWidget(interruptor)
            l2.addStretch()
            
            if linha % 2 == 1:
                envolta2.setStyleSheet("background-color: white;")
            else:
<<<<<<< HEAD
                envolta2.setStyleSheet("background-color: #E9F2FF;")
=======
                envolta2.setStyleSheet("""
                    background-color: #E9F2FF;
                """)
>>>>>>> 14523cf01e7c89b0edd0628b51fd00eaf8dcd4c9
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
