import os
import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import (
    QColor,
    QFont,
    QIcon,
    QLinearGradient,
    QPainter,
    QPainterPath,
    QPixmap
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

CAMINHO_LOGO = os.path.join(
    os.path.dirname(__file__),
    "imagens",
    "embrapagadodecorte.jpg"
)
CAMINHO_FUNDO = os.path.join(
    os.path.dirname(__file__),
    "imagens",
    "fundo_login.png"
)

class FundoOndulado(QWidget):

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        pixmap = QPixmap(CAMINHO_FUNDO)

        if not pixmap.isNull():
            escalada = pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            x = (self.width() - escalada.width()) // 2
            y = (self.height() - escalada.height()) // 2

            painter.drawPixmap(x, y, escalada)
        else:
            self._pintar_gradiente_reserva(painter)

        painter.end()

    def _pintar_gradiente_reserva(self, painter):
        largura = self.width()
        altura = self.height()

        gradiente = QLinearGradient(0, 0, largura, altura)
        gradiente.setColorAt(0.0, QColor("#3D6796"))
        gradiente.setColorAt(1.0, QColor("#1F3F63"))

        painter.fillRect(self.rect(), gradiente)

        camadas = [
            (0.50, QColor(255, 255, 255, 16)),
            (0.68, QColor(255, 255, 255, 12)),
            (0.86, QColor(0, 0, 0, 22))
        ]

        for posicao_y, cor in camadas:
            caminho = QPainterPath()
            y_base = altura * posicao_y

            caminho.moveTo(0, y_base)
            caminho.cubicTo(
                largura * 0.22, y_base - 70,
                largura * 0.38, y_base + 70,
                largura * 0.6, y_base
            )
            caminho.cubicTo(
                largura * 0.78, y_base - 55,
                largura * 0.9, y_base + 45,
                largura, y_base - 15
            )
            caminho.lineTo(largura, altura)
            caminho.lineTo(0, altura)
            caminho.closeSubpath()

            painter.setPen(Qt.NoPen)
            painter.setBrush(cor)
            painter.drawPath(caminho)

class TelaAutenticacaoBase(FundoOndulado):

   
    LARGURA_TELA = 1280
    ALTURA_TELA = 720
    LARGURA_CARD = 1011
    ALTURA_CARD = 884

    def _montar_card(self):
        layout_externo = QVBoxLayout(self)
        layout_externo.setAlignment(Qt.AlignCenter)
        layout_externo.setContentsMargins(0, 0, 0, 0)

        self._card = QFrame()
        self._card.setFixedSize(
            self.LARGURA_CARD,
            self.ALTURA_CARD
        )
        self._card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 14px;
            }
        """)

        layout_externo.addWidget(self._card)

        layout_card = QVBoxLayout(self._card)
        return self._card, layout_card

    def _logo(self):
        label_logo = QLabel()
        pixmap = QPixmap(CAMINHO_LOGO)

        if not pixmap.isNull():
            label_logo.setPixmap(
                pixmap.scaledToWidth(
                    300,
                    Qt.SmoothTransformation
                )
            )
        else:
            label_logo.setText("Embrapa\nGado de Corte")

        label_logo.setAlignment(Qt.AlignCenter)
        return label_logo

class LoginScreen(TelaAutenticacaoBase):

    login_solicitado = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        _, card_layout = self._montar_card()
        card_layout.setContentsMargins(100, 60, 100, 60)
        card_layout.setSpacing(0)
        logo = self._logo()
        card_layout.addWidget(logo)
        card_layout.addSpacing(30)

        titulo = QLabel("Bem-vindo")
        titulo.setStyleSheet("""
            QLabel {
                font-size: 48px;
                font-weight: 800;
                color: #111111;
                border: none;
            }
        """)
        titulo.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(titulo)
        card_layout.addSpacing(10)

        subtitulo = QLabel("Por favor, preencha os\ncampos com seus dados.")
        subtitulo.setStyleSheet("""
            QLabel {
                color: #6B7280;
                font-size: 18px;
                border: none;
            }
        """)
        subtitulo.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(subtitulo)
        card_layout.addSpacing(40)

        self.campo_email = QLineEdit()
        self.campo_email.setPlaceholderText("Digite seu E-mail aqui.")
        self.campo_email.setFixedSize(612, 99)

        self.campo_email.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #1C1C1C;
                border: 1px solid #D0D0D0;
                border-radius: 8px;
                padding-left: 20px;
                padding-right: 20px;
                font-size: 18px;
            }
            QLineEdit:focus {
                border: 2px solid #D0D0D0;
            }
        """)
        self.campo_email.returnPressed.connect(self._entrar)

        card_layout.addWidget(self.campo_email, 0, Qt.AlignCenter)
        card_layout.addSpacing(30)

        botao_entrar = QPushButton("ENTRAR")
        botao_entrar.setCursor(Qt.PointingHandCursor)
        botao_entrar.setFixedSize(530, 84)

        botao_entrar.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                border: none;
                border-radius: 9px;
                font-size: 24px;
                font-weight: 700;
            }
            QPushButton:hover {
                background-color: #04620F;
            }
            QPushButton:pressed {
                background-color: #04620F;
            }
        """)
        botao_entrar.clicked.connect(self._entrar)

        card_layout.addWidget(botao_entrar, 0, Qt.AlignCenter)

 
    def _entrar(self):
        email = self.campo_email.text().strip()
        self.login_solicitado.emit(email)

    def limpar(self):
        self.campo_email.clear()

def _ao_logar_com_sucesso(email):
    pass

def main():
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QWidget {
            font-family: 'Segoe UI';
            color: #1C1C1C;
        }
    """)

    janela = QMainWindow()
    janela.setWindowTitle("Embrapa Gado de Corte — Login")
    janela.setWindowFlags(
        Qt.Window |
        Qt.WindowMinimizeButtonHint |
        Qt.WindowMaximizeButtonHint |
        Qt.WindowCloseButtonHint
    )
    janela.resize(1280, 720)
    janela.setMinimumSize(1024, 600)

    tela_login = LoginScreen()
    tela_login.login_solicitado.connect(_ao_logar_com_sucesso)

    janela.setCentralWidget(tela_login)
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()