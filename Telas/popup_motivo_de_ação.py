import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QLabel, QTextEdit,
    QPushButton, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor

class PopupRejeicao(QDialog):
    def __init__(self):
        super().__init__()

        self.setFixedSize(830, 466)

        # Deixa o fundo da janela transparente
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)

        titulo = QLabel("Motivo para rejeição da ação")
        titulo.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: black;
            }
        """)
        titulo.setAlignment(Qt.AlignCenter)

        fechar = QPushButton("X")
        fechar.setFixedSize(50, 50)
        fechar.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                font-size: 36px;
                font-weight: bold;
                color: black;
            }

            QPushButton:hover {
                color: #555;
            }
        """)
        fechar.clicked.connect(self.close)

        cabecalho = QHBoxLayout()
        cabecalho.addStretch()
        cabecalho.addWidget(titulo)
        cabecalho.addStretch()
        cabecalho.addWidget(fechar)

        razao = QLabel("Razão")
        razao.setStyleSheet("""
            QLabel {
                font-size: 30px;
                font-weight: bold;
                color: black;
            }
        """)

        texto = QTextEdit()
        texto.setPlaceholderText(
            "Explique o porquê a ação foi rejeitada, disserte sobre..."
        )
        texto.setStyleSheet("""
            QTextEdit {
                border: 1px solid #999;
                background-color: white;
                font-size: 20px;
                color: black;
                padding: 10px;
                border-radius: 10px;
            }
        """)

        cancelar = QPushButton("Cancelar")
        cancelar.setFixedHeight(60)
        cancelar.setStyleSheet("""
            QPushButton {
                background-color: #2055A0;
                color: white;
                border: none;
                border-radius: 30px;
                font-size: 21px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #174582;
            }
        """)
        cancelar.clicked.connect(self.close)

        enviar = QPushButton("Enviar")
        enviar.setFixedHeight(60)
        enviar.setStyleSheet("""
            QPushButton {
                background-color: #009414;
                color: white;
                border: none;
                border-radius: 30px;
                font-size: 21px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #007a10;
            }
        """)
        enviar.clicked.connect(self.enviar)

        botoes = QHBoxLayout()
        botoes.setSpacing(35)
        botoes.addWidget(cancelar)
        botoes.addWidget(enviar)

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 20, 50, 35)
        layout.setSpacing(15)
        layout.addLayout(cabecalho)
        layout.addWidget(razao)
        layout.addWidget(texto)
        layout.addLayout(botoes)

        self.setLayout(layout)

    # Desenha a janela com os cantos arredondados
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor("white"))
        painter.setPen(Qt.NoPen)

        painter.drawRoundedRect(
            self.rect(),
            25,
            25
        )

    def enviar(self):
        motivo = self.findChild(QTextEdit).toPlainText()
        print("Motivo:", motivo)
        self.close()


app = QApplication(sys.argv)
popup = PopupRejeicao()
popup.exec()
sys.exit()