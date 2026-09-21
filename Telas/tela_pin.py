from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QWidget
)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, Signal

LOGO = "Imagens/logo_embrapa.png"
FECHAR = "Imagens/Vector.png"
BACKGROUND = "Imagens/background.png"

VERDE = "#058914"
BRANCO = "#FFFFFF"


class tela_pin(QFrame):
    voltar_login_solicitado = Signal()

    def __init__(self):
        super().__init__()

        self.setFixedSize(1920, 1080)
        self.setWindowTitle("PIN")

        self.setStyleSheet(
            f"""
            QFrame {{
                background-image: url({BACKGROUND});
            }}
            """
        )

        layout_principal = QVBoxLayout()
        self.setLayout(layout_principal)

        window_pin = QWidget()
        window_pin.setFixedSize(1011, 884)
        window_pin.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 10px;
            }
        """)

        layout_principal.addWidget(window_pin)
        layout_principal.setAlignment(
            Qt.AlignCenter
        )

        layout_pin = QVBoxLayout()
        window_pin.setLayout(layout_pin)
        layout_pin.setAlignment(
            Qt.AlignCenter
        )
        layout_pin.setSpacing(40)

        self.botao_fechar = QPushButton()
        pixmap_fechar = QPixmap(FECHAR)

        if not pixmap_fechar.isNull():
            self.botao_fechar.setIcon(QIcon(pixmap_fechar))
            self.botao_fechar.setIconSize(pixmap_fechar.size())

        self.botao_fechar.setCursor(Qt.PointingHandCursor)
        self.botao_fechar.setStyleSheet(
            """
            QPushButton {
                background: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 15);
                border-radius: 4px;
            }
            """
        )
        self.botao_fechar.clicked.connect(self.voltar_login_solicitado.emit)

        layout_pin.addWidget(
            self.botao_fechar,
            alignment=Qt.AlignLeft
        )

        logo_embrapa = QLabel()
        pixmap_logo = QPixmap(LOGO)

        if not pixmap_logo.isNull():
            logo_embrapa.setPixmap(
                pixmap_logo
            )
            logo_embrapa.setScaledContents(
                True
            )

        logo_embrapa.setFixedSize(
            476,
            206
        )
        logo_embrapa.setStyleSheet(
            "background: transparent;"
        )

        layout_pin.addWidget(
            logo_embrapa,
            alignment=Qt.AlignCenter
        )

        sub_titulo = QLabel(
            "Digite o PIN enviado para seu E-mail"
        )

        sub_titulo.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 20px;
                background: transparent;
                font-family: Verdana;
                color: black;
            }
        """)

        sub_titulo.setAlignment(
            Qt.AlignCenter
        )

        layout_pin.addWidget(sub_titulo)

        self.input_pin = QLineEdit()
        self.input_pin.setPlaceholderText(
            "Digite o seu PIN."
        )
        self.input_pin.setFixedSize(
            612,
            99
        )

        self.input_pin.setStyleSheet("""
            QLineEdit {
                color: black;
                background-color: white;
                border: 1px solid gray;
                border-radius: 8px;
                padding-left: 20px;
                padding-right: 20px;
                font-size: 18px;
                font-family: Verdana;
            }

            QLineEdit:focus {
                border: 2px solid #058914;
            }
        """)

        layout_pin.addWidget(
            self.input_pin,
            alignment=Qt.AlignCenter
        )

        self.botao_verificar = QPushButton(
            "VERIFICAR"
        )
        self.botao_verificar.setFixedSize(
            530,
            84
        )
        self.botao_verificar.setCursor(
            Qt.PointingHandCursor
        )

        self.botao_verificar.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                border: none;
                border-radius: 9px;
                font-size: 20px;
                font-family: Verdana;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #04620F;
            }

            QPushButton:pressed {
                background-color: #034D0B;
            }
        """)

        layout_pin.addWidget(
            self.botao_verificar,
            alignment=Qt.AlignCenter
        )