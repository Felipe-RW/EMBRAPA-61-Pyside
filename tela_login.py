import os
import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QFont, QIcon, QLinearGradient, QPainter, QPainterPath, QPixmap
from PySide6.QtWidgets import (
    QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QMessageBox,
    QPushButton, QVBoxLayout, QWidget
)
  
"""A tela pin precisa fazer import de ControleDeAcesso, TelaAutenticacaoBase. Muito obrigado! """

CAMINHO_LOGO = os.path.join(os.path.dirname(__file__), "imagens", "embrapagadodecorte.jpg")
CAMINHO_FUNDO = os.path.join(os.path.dirname(__file__), "imagens", "fundo_login.png")



class Perfil:

    PESQUISADOR = "Pesquisador"
    VALIDADOR = "Validador"
    COMITE = "Comitê"
    ADMINISTRADOR = "Administrador"

    TODOS = (PESQUISADOR, VALIDADOR, COMITE, ADMINISTRADOR)


class ControleDeAcesso:
    

    _autorizados = {
        "jordana.dark@embrapa.br": Perfil.PESQUISADOR,
        "diana.mirror@embrapa.br": Perfil.PESQUISADOR,
        "angel.gray@embrapa.br": Perfil.VALIDADOR,
        "narciso.water@embrapa.br": Perfil.COMITE,
        "admin@embrapa.br": Perfil.ADMINISTRADOR,
    }

    @classmethod
    def esta_autorizado(cls, email: str) -> bool:
        
        return email.strip().lower() in cls._autorizados

    @classmethod
    def perfil_de(cls, email: str) -> str | None:
        
        return cls._autorizados.get(email.strip().lower())

    @classmethod
    def autorizar(cls, email: str, perfil: str):
       
        if perfil not in Perfil.TODOS:
            raise ValueError(f"Perfil inválido: {perfil}")
        cls._autorizados[email.strip().lower()] = perfil

    @classmethod
    def revogar(cls, email: str):
        cls._autorizados.pop(email.strip().lower(), None)



def _icone_usuario() -> QIcon:
    pixmap = QPixmap(20, 20)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setFont(QFont("Segoe UI", 11))
    painter.setPen(QColor("#9AA1AC"))
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "👤")
    painter.end()
    return QIcon(pixmap)



class FundoOndulado(QWidget):

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        pixmap = QPixmap(CAMINHO_FUNDO)
        if not pixmap.isNull():
            self._pintar_imagem_de_fundo(painter, pixmap)
        else:
            self._pintar_gradiente_reserva(painter)

        super().paintEvent(event)

    def _pintar_imagem_de_fundo(self, painter, pixmap):
        
        escalada = pixmap.scaled(
            self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
        )
        x = (self.width() - escalada.width()) / 2
        y = (self.height() - escalada.height()) / 2
        painter.drawPixmap(int(x), int(y), escalada)

    def _pintar_gradiente_reserva(self, painter):
        largura, altura = self.width(), self.height()

        gradiente = QLinearGradient(0, 0, largura, altura)
        gradiente.setColorAt(0.0, QColor("#3D6796"))
        gradiente.setColorAt(1.0, QColor("#1F3F63"))
        painter.fillRect(self.rect(), gradiente)

        camadas = [
            (0.50, QColor(255, 255, 255, 16)),
            (0.68, QColor(255, 255, 255, 12)),
            (0.86, QColor(0, 0, 0, 22)),
        ]
        for posicao_y, cor in camadas:
            caminho = QPainterPath()
            y_base = altura * posicao_y
            caminho.moveTo(0, y_base)
            caminho.cubicTo(largura * 0.22, y_base - 70, largura * 0.38, y_base + 70, largura * 0.6, y_base)
            caminho.cubicTo(largura * 0.78, y_base - 55, largura * 0.9, y_base + 45, largura, y_base - 15)
            caminho.lineTo(largura, altura)
            caminho.lineTo(0, altura)
            caminho.closeSubpath()
            painter.setPen(Qt.NoPen)
            painter.setBrush(cor)
            painter.drawPath(caminho)


class TelaAutenticacaoBase(FundoOndulado):
    

    LARGURA_CARD = 420       
    LARGURA_CARD_MAXIMA = 640 

    def titulo_tela(self) -> str:
        
        raise NotImplementedError(
            f"{type(self).__name__} precisa implementar titulo_tela()."
        )

    def _montar_card(self):
       
        layout_externo = QVBoxLayout(self)
        layout_externo.setAlignment(Qt.AlignCenter)

        self._card = QFrame()
        self._card.setFixedWidth(self.LARGURA_CARD)
        self._card.setStyleSheet("background: white; border-radius: 14px;")
        layout_externo.addWidget(self._card)

        layout_card = QVBoxLayout(self._card)
        return self._card, layout_card

    def resizeEvent(self, event):
    
        super().resizeEvent(event)
        if hasattr(self, "_card"):
            largura_proporcional = int(self.width() * 0.42)  
            nova_largura = max(self.LARGURA_CARD, min(largura_proporcional, self.LARGURA_CARD_MAXIMA))
            self._card.setFixedWidth(nova_largura)

    def _logo(self) -> QLabel:
        label_logo = QLabel()
        pixmap = QPixmap(CAMINHO_LOGO)
        if not pixmap.isNull():
            label_logo.setPixmap(pixmap.scaledToWidth(150, Qt.SmoothTransformation))
        else:
            label_logo.setText("Embrapa\nGado de Corte")
        label_logo.setAlignment(Qt.AlignCenter)
        return label_logo


class LoginScreen(TelaAutenticacaoBase):
  
    login_solicitado = Signal(str)  

    def titulo_tela(self) -> str:
        return "Login por e-mail"

    def __init__(self, parent=None):
        super().__init__(parent)
        _, card_layout = self._montar_card()
        card_layout.setContentsMargins(40, 36, 40, 40)
        card_layout.setSpacing(4)

        card_layout.addWidget(self._logo())
        card_layout.addSpacing(20)

        titulo = QLabel("Bem-vindo")
        titulo.setStyleSheet("font-size: 24px; font-weight: 800; border: none;")
        titulo.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(titulo)

        subtitulo = QLabel("Por favor, preencha os\ncampos com seus dados.")
        subtitulo.setStyleSheet("color: #6B7280; font-size: 12px; border: none;")
        subtitulo.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(subtitulo)
        card_layout.addSpacing(20)

        self.campo_email = QLineEdit()
        self.campo_email.setPlaceholderText("Digite seu E-mail aqui.")
        self.campo_email.addAction(_icone_usuario(), QLineEdit.LeadingPosition)
        self.campo_email.setFixedHeight(42)
        self.campo_email.setStyleSheet(
            "border-radius: 8px; padding-left: 6px;"
            "selection-background-color: #2196F3; selection-color: white;"
        )
        self.campo_email.returnPressed.connect(self._entrar)
        card_layout.addWidget(self.campo_email)
        card_layout.addSpacing(16)

        botao_entrar = QPushButton("ENTRAR")
        botao_entrar.setCursor(Qt.PointingHandCursor)
        botao_entrar.setFixedHeight(44)
        botao_entrar.setStyleSheet("""
            QPushButton { background-color: #1E9E4F; color: white; border-radius: 8px; font-weight: 700; }
            QPushButton:hover { background-color: #188540; }
        """)
        botao_entrar.clicked.connect(self._entrar)
        card_layout.addWidget(botao_entrar)

    def _entrar(self):
        email = self.campo_email.text().strip()
        usuario, _, dominio = email.partition("@")
        if not usuario or "." not in dominio:
            QMessageBox.warning(self, "E-mail inválido", "Digite um e-mail válido para continuar.")
            return

        if not ControleDeAcesso.esta_autorizado(email):
            QMessageBox.warning(
                self, "Acesso não autorizado",
                "Este e-mail ainda não foi cadastrado no sistema.\n\n"
                "Peça para um administrador criar e liberar o seu perfil de acesso."
            )
            return

        self.login_solicitado.emit(email)

    def limpar(self):
        self.campo_email.clear()



def _ao_logar_com_sucesso(email: str):
    perfil = ControleDeAcesso.perfil_de(email)
    QMessageBox.information(
        None, "Login autorizado",
        f"E-mail autorizado: {email}\nPerfil: {perfil}\n\n"
        f"(Aguardando a tela de PIN.)"
    )


def main():
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QWidget { font-family: 'Segoe UI'; color: #1C1C1C; }
        QLineEdit { background-color: white; color: #1C1C1C; }
        QMessageBox { background-color: white; }
        QMessageBox QLabel { color: #1C1C1C; }
    """)

    janela = QMainWindow()
    janela.setWindowTitle("Embrapa Gado de Corte — Login")
    janela.resize(950, 620)
    janela.setMinimumSize(700, 560)

    tela_login = LoginScreen()
    tela_login.login_solicitado.connect(_ao_logar_com_sucesso)
    janela.setCentralWidget(tela_login)

    janela.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
