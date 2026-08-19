import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)


class PopupSucesso(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sucesso")
        self.setFixedSize(1000, 650)

        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 40, 0, 60)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Círculo
        circulo = QLabel("✓")
        circulo.setFixedSize(210, 210)
        circulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        circulo.setStyleSheet("""
            QLabel {
                background-color:#d9ebff;
                border-radius: 105px;
                font-size: 90px;
            }
        """)

        # Título
        titulo = QLabel("O ano foi criado!")

        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo.setStyleSheet("""
            QLabel {
                background: green;
                font-size: 30px;
                font-weight: 700;
            }
        """)


    # Texto 1
        mensagem = QLabel(
            "As informações do ano foram atualizadas!"
        )

        mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mensagem.setStyleSheet("""
            QLabel {
                background: white;
                font-size: 21px;
                color: #444;
            }
        """)

        # Texto 2
        mensagem = QLabel(
            "Alterações realizadas com sucesso!"
        )

        mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mensagem.setStyleSheet("""
            QLabel {
                background: white;
                font-size: 18px;
                color: #444;
            }
        """)

        # Botão
        botao = QPushButton("Fechar")

        botao.setFixedSize(370, 56)

        botao.setStyleSheet("""
            QPushButton {
                background-color: #1f2d87;
                color: white;
                border: none;
                border-radius: 28px;
                font-size: 18px;
            }
        """)

        botao.clicked.connect(self.close)

        layout.addWidget(
            circulo,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        layout.addSpacing(35)

        layout.addWidget(titulo)

        layout.addSpacing(10)

        layout.addWidget(mensagem)

        layout.addSpacing(180)

        layout.addWidget(
            botao,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        self.setLayout(layout)


app = QApplication(sys.argv)

janela = PopupSucesso()
janela.show()

sys.exit(app.exec())