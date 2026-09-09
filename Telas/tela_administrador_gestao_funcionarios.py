import sys, os
from PySide6.QtCore import QPropertyAnimation, QRectF, Qt, Property
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QColor, QPainter
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup, QTableWidget, QHeaderView, QTableWidgetItem, QCheckBox
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

class tela_de_empregados (QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1500, 1010)

        central = QWidget()
        self.setCentralWidget(central)

        layout_principal = QVBoxLayout(central)
        layout_principal.setContentsMargins(30, 30, 30, 30)
        layout_principal.setSpacing(30)
        self.setStyleSheet ("background-color: #EEF1F5;")

        titulo = QLabel("Gestão de Empregados")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        titulo.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(titulo)

        layout_acoes = QHBoxLayout()

        btn_cadastrar = QPushButton("Cadastrar Empregado")
        btn_cadastrar.setStyleSheet("""
            QPushButton {
                background-color: #1e7e34;
                color: white;
                font-weight: bold;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #155724;
            }
        """)
        
        btn_baixar = QPushButton("Baixar em Excel")
        btn_baixar.setStyleSheet("""
            QPushButton {
                background-color: #ffffff; 
                color: blue;
                font-weight: bold;
                border-radius: 6px;
                padding: 8px 16px;
                border: 1px solid #d0d0d0;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }                        
        """)

        campo_busca = QLineEdit()
        campo_busca.setPlaceholderText("Pesquise...")
        campo_busca.setMaximumWidth(360)
        campo_busca.setStyleSheet("""
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 6px;
                color: #333333;
                background-color: #ffffff;
            }
        """)

        layout_acoes.addWidget(btn_cadastrar)
        layout_acoes.addWidget(btn_baixar)
        layout_acoes.addStretch()
        layout_acoes.addWidget(campo_busca)

        layout_principal.addLayout(layout_acoes)

        dados_funcionarios = [
            ("Fulano da Silva","silva@gmail.com","Pesquisador","Ativo"," "),
            ("Fulano Ferreira", "ferreira@gmail.com", "Pesquisador", "Ativo"," "),
            ("Fulano Araujo", "araujo@gmail.com", "Validador SIPT", "Desativado"," "),
            ("Fulano Oliveira", "oliveira@gmail.com", "Validador SPAT", "Ativo"," "),
            ("Fulano Leite", "leite@gmail.com", "Validador NCO", "Ativo"," "),
            ("Fulano Da Guia", "guia@gmail.com", "Comitê", "Ativo"," "),
            ("Fulano Jacobina", "jacobina@gmail.com", "Comitê", "Desativado"," "),
            ("Fulano Nogueira", "nogueira@gmail.com", "Administrador", "Ativo"," "),
        ]

        tabela = QTableWidget(len(dados_funcionarios),5)
        tabela.setHorizontalHeaderLabels(["Nome","Email","Área de Atuação","Status","Ação"])
        tabela.horizontalHeader().setFixedHeight(70)
        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabela.verticalHeader().setVisible(False)
        tabela.verticalHeader().setDefaultSectionSize(50)
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        tabela.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                gridline-color: #e0e0e0;
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                color: #333333;
            }
            QHeaderView::section {
                background-color: #366896;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 15px 0px;
            }

            QHeaderView::section:first {
                border-top-left-radius: 10px;
            }
            QHeaderView::section:last {
                border-top-right-radius: 10px;
            }
        """)

        for linha_id, (nome, email, area, status, acao) in enumerate(dados_funcionarios):
            item_nome = QTableWidgetItem(nome)
            item_email = QTableWidgetItem(email)
            item_area = QTableWidgetItem(area)
            item_status = QTableWidgetItem(status)

            item_nome.setTextAlignment(Qt.AlignCenter)
            item_email.setTextAlignment(Qt.AlignCenter)
            item_area.setTextAlignment(Qt.AlignCenter)
            item_status.setTextAlignment(Qt.AlignCenter)

            if status == "Ativo":
                item_status.setForeground(QColor("green"))
            else:
                item_status.setForeground(QColor("orange"))

            tabela.setItem(linha_id, 0, item_nome)
            tabela.setItem(linha_id, 1, item_email)
            tabela.setItem(linha_id, 2, item_area)
            tabela.setItem(linha_id, 3, item_status)

            conteiner_botao = QWidget()
            layout_botao = QHBoxLayout(conteiner_botao)
            layout_botao.setContentsMargins(0,0,0,0)
            layout_botao.setAlignment(Qt.AlignCenter)

            btn_switch = AnimacaoBotao()
            btn_switch.setChecked( status == "Ativo")

            layout_botao.addWidget(btn_switch)
            tabela.setCellWidget(linha_id, 4, conteiner_botao)

        layout_principal.addWidget(tabela)

class AnimacaoBotao(QCheckBox):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(Qt.PointingHandCursor)

        self._bg_color_off = QColor("#cccccc")
        self._bg_color_on = QColor("#366896")
        self._circle_color = QColor("#ffffff")

        self.setFixedSize(38, 20)

        self._circle_position = 2.0

        self.animation = QPropertyAnimation(self, b"circle_position")
        self.animation.setDuration(150)

        self.stateChanged.connect(self.start_animation)

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()
    def start_animation(self, state):
        self.animation.stop()

        end_value = 20.0 if state == 2 else 2.0

        self.animation.setStartValue(self._circle_position)
        self.animation.setEndValue(end_value)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        bg_color = self._bg_color_on if self.isChecked() else self._bg_color_off
        painter.setBrush(bg_color)
        painter.setPen(Qt.NoPen)

        painter.drawRoundedRect(QRectF(0, 0, self.width(), self.height()), 10, 10)

        painter.setBrush(self._circle_color)
        painter.drawEllipse(QRectF(self._circle_position, 2, 16, 16))
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tela_de_empregados()
    window.show()
    sys.exit(app.exec())