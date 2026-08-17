import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)


class Popup(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sucesso")
        self.setFixedSize(600, 500)

        self.setStyleSheet("""
            QWidget{
                background:white;
            }
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Ícone
        icone = QLabel("✓")
        icone.setFixedSize(180, 180)

        icone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icone.setStyleSheet("""
            QLabel{
                background:#d7e8ff;
                border-radius:90px;
                font-size:90px;
            }
        """)

        # Título
        titulo = QLabel("O ano foi criado!")

        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo.setStyleSheet("""
            QLabel{
                font-size:30px;
                font-weight:700;
                background:white;
            }
        """)

        # Mensagem
        mensagem = QLabel(
            "Ano adicionado ao sistema com sucesso!"
        )

        mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mensagem.setStyleSheet("""
            QLabel{
                font-size:18px;
                color:#444;
                background:white;
            }
        """)

        # Botão
        botao = QPushButton("Fechar")

        botao.setFixedSize(300, 55)

        botao.setStyleSheet("""
            QPushButton{
                background:#1f2b88;
                color:white;
                border:none;
                border-radius:25px;
                font-size:20px;
            }

            QPushButton:hover{
                background:#26369d;
            }
        """)

        botao.clicked.connect(self.close)

        layout.addSpacing(20)
        layout.addWidget(icone)
        layout.addSpacing(20)
        layout.addWidget(titulo)
        layout.addWidget(mensagem)
        layout.addSpacing(90)
        layout.addWidget(
            botao,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.setLayout(layout)


app = QApplication(sys.argv)

janela = Popup()
janela.show()

sys.exit(app.exec())