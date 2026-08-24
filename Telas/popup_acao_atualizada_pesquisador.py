import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import Qt


class PopupAcaoAtualizada(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ação atualizada")
        self.setFixedSize(1200, 640)

        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 20px;
            }
        """)

        self.circulo = QLabel(self)
        self.circulo.setGeometry(475, 55, 238, 238)
        self.circulo.setAlignment(Qt.AlignCenter)
        self.circulo.setText("✓")

        self.circulo.setStyleSheet("""
            QLabel {
                background-color: #C4E1FF;
                color: #356394;
                border: none;
                border-radius: 119px;
                font-size: 95px;
                font-weight: normal;
            }
        """)

        self.titulo = QLabel("Sua ação foi atualizada!", self)
        self.titulo.setGeometry(350, 330, 500, 40)
        self.titulo.setAlignment(Qt.AlignCenter)

        self.titulo.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 34px;
                font-family: Verdana;
                font-weight: bold;
                background-color: transparent;
            }
        """)

        self.texto = QLabel(
            "Sua ação foi reenviada para os avaliadores.",
            self
        )
        self.texto.setGeometry(300, 375, 600, 30)
        self.texto.setAlignment(Qt.AlignCenter)

        self.texto.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: Verdana;
                font-weight: normal;
                background-color: transparent;
            }
        """)

        self.botao = QPushButton("Fechar", self)
        self.botao.setGeometry(460, 550, 285, 48)

        self.botao.setStyleSheet("""
            QPushButton {
                background-color: #172b8c;
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 23px;
            }

            QPushButton:hover {
                background-color: #056510;
            }

            QPushButton:pressed {
                background-color: #056510;
            }
        """)


app = QApplication(sys.argv)

janela = PopupAcaoAtualizada()
janela.show()

sys.exit(app.exec())