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
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget
)


# =========================================================
# CAMINHOS DAS IMAGENS
# =========================================================

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


# =========================================================
# PERFIS
# =========================================================

class Perfil:

    PESQUISADOR = "Pesquisador"
    VALIDADOR = "Validador"
    COMITE = "Comitê"
    ADMINISTRADOR = "Administrador"

    TODOS = (
        PESQUISADOR,
        VALIDADOR,
        COMITE,
        ADMINISTRADOR
    )


# =========================================================
# CONTROLE DE ACESSO
# =========================================================

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

        return cls._autorizados.get(
            email.strip().lower()
        )

    @classmethod
    def autorizar(cls, email: str, perfil: str):

        if perfil not in Perfil.TODOS:

            raise ValueError(
                f"Perfil inválido: {perfil}"
            )

        cls._autorizados[
            email.strip().lower()
        ] = perfil

    @classmethod
    def revogar(cls, email: str):

        cls._autorizados.pop(
            email.strip().lower(),
            None
        )


# =========================================================
# ÍCONE DE USUÁRIO
# =========================================================

def _icone_usuario() -> QIcon:

    pixmap = QPixmap(20, 20)

    pixmap.fill(
        Qt.transparent
    )

    painter = QPainter(pixmap)

    painter.setRenderHint(
        QPainter.Antialiasing
    )

    painter.setFont(
        QFont("Segoe UI", 11)
    )

    painter.setPen(
        QColor("#9AA1AC")
    )

    painter.end()

    return QIcon(pixmap)


# =========================================================
# FUNDO
# =========================================================

class FundoOndulado(QWidget):

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        painter.setRenderHint(
            QPainter.SmoothPixmapTransform
        )

        pixmap = QPixmap(
            CAMINHO_FUNDO
        )

        if not pixmap.isNull():

            escalada = pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            x = (
                self.width()
                - escalada.width()
            ) // 2

            y = (
                self.height()
                - escalada.height()
            ) // 2

            painter.drawPixmap(
                x,
                y,
                escalada
            )

        else:

            self._pintar_gradiente_reserva(
                painter
            )

        painter.end()

    def _pintar_gradiente_reserva(
        self,
        painter
    ):

        largura = self.width()
        altura = self.height()

        gradiente = QLinearGradient(
            0,
            0,
            largura,
            altura
        )

        gradiente.setColorAt(
            0.0,
            QColor("#3D6796")
        )

        gradiente.setColorAt(
            1.0,
            QColor("#1F3F63")
        )

        painter.fillRect(
            self.rect(),
            gradiente
        )

        camadas = [
            (
                0.50,
                QColor(
                    255,
                    255,
                    255,
                    16
                )
            ),
            (
                0.68,
                QColor(
                    255,
                    255,
                    255,
                    12
                )
            ),
            (
                0.86,
                QColor(
                    0,
                    0,
                    0,
                    22
                )
            )
        ]

        for posicao_y, cor in camadas:

            caminho = QPainterPath()

            y_base = (
                altura * posicao_y
            )

            caminho.moveTo(
                0,
                y_base
            )

            caminho.cubicTo(
                largura * 0.22,
                y_base - 70,
                largura * 0.38,
                y_base + 70,
                largura * 0.6,
                y_base
            )

            caminho.cubicTo(
                largura * 0.78,
                y_base - 55,
                largura * 0.9,
                y_base + 45,
                largura,
                y_base - 15
            )

            caminho.lineTo(
                largura,
                altura
            )

            caminho.lineTo(
                0,
                altura
            )

            caminho.closeSubpath()

            painter.setPen(
                Qt.NoPen
            )

            painter.setBrush(
                cor
            )

            painter.drawPath(
                caminho
            )


# =========================================================
# TELA DE AUTENTICAÇÃO
# =========================================================

class TelaAutenticacaoBase(
    FundoOndulado
):

    # TELA
    LARGURA_TELA = 1920
    ALTURA_TELA = 1080

    # CARD
    LARGURA_CARD = 1011
    ALTURA_CARD = 884

    def _montar_card(self):

        layout_externo = QVBoxLayout(
            self
        )

        layout_externo.setAlignment(
            Qt.AlignCenter
        )

        layout_externo.setContentsMargins(
            0,
            0,
            0,
            0
        )

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

        layout_externo.addWidget(
            self._card
        )

        layout_card = QVBoxLayout(
            self._card
        )

        return (
            self._card,
            layout_card
        )

    # =====================================================
    # LOGO
    # =====================================================

    def _logo(self):

        label_logo = QLabel()

        pixmap = QPixmap(
            CAMINHO_LOGO
        )

        if not pixmap.isNull():

            label_logo.setPixmap(
                pixmap.scaledToWidth(
                    300,
                    Qt.SmoothTransformation
                )
            )

        else:

            label_logo.setText(
                "Embrapa\nGado de Corte"
            )

        label_logo.setAlignment(
            Qt.AlignCenter
        )

        return label_logo

    # =====================================================
    # F11
    # =====================================================

    def keyPressEvent(
        self,
        event
    ):

        if event.key() == Qt.Key_F11:

            janela = self.window()

            if janela.isFullScreen():

                janela.showNormal()

                janela.resize(
                    self.LARGURA_TELA,
                    self.ALTURA_TELA
                )

            else:

                janela.showFullScreen()

        else:

            super().keyPressEvent(
                event
            )


# =========================================================
# LOGIN
# =========================================================

class LoginScreen(
    TelaAutenticacaoBase
):

    login_solicitado = Signal(str)

    def __init__(
        self,
        parent=None
    ):

        super().__init__(
            parent
        )

        _, card_layout = (
            self._montar_card()
        )

        # =================================================
        # ESPAÇAMENTO DO CARD
        # =================================================

        card_layout.setContentsMargins(
            100,
            70,
            100,
            80
        )

        card_layout.setSpacing(
            0
        )

        # =================================================
        # LOGO
        # =================================================

        card_layout.addWidget(
            self._logo()
        )

        card_layout.addSpacing(
            70
        )

        # =================================================
        # TÍTULO
        # =================================================

        titulo = QLabel(
            "Bem-vindo"
        )

        titulo.setStyleSheet("""
            QLabel {
                font-size: 55px;
                font-weight: 800;
                color: #111111;
                border: none;
            }
        """)

        titulo.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            titulo
        )

        subtitulo = QLabel(
            "Por favor, preencha os\n"
            "campos com seus dados."
        )

        subtitulo.setStyleSheet("""
            QLabel {
                color: #6B7280;
                font-size: 20px;
                border: none;
            }
        """)

        subtitulo.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            subtitulo
        )

        card_layout.addSpacing(
            55
        )

        # =================================================
        # E-MAIL
        # =================================================

        self.campo_email = QLineEdit()

        self.campo_email.setPlaceholderText(
            "Digite seu E-mail aqui."
        )
        self.campo_email.setFixedHeight(60)  # Definindo a altura da caixa
        self.campo_email.setStyleSheet("""
            QLineEdit {
                background-color: white;          /* Fundo branco */
                color: #1C1C1C;                   /* Cor do texto */
                border: 1px solid #D0D0D0;        /* Borda cinza */
                border-radius: 5px;               /* Bordas arredondadas */
                padding-left: 5px;                /* Espaçamento interno */
                font-size: 18px;                  /* Tamanho da fonte */
            }

            QLineEdit:focus {
                border: 1px solid #D0D0D0;        /* Borda verde quando focado */
            }
        """)
        self.campo_email.returnPressed.connect(
            self._entrar
        )

        # Adicionar o campo de email ao layout do cartão
        card_layout.addWidget(self.campo_email)



        # =================================================
        # BOTÃO ENTRAR
        # =================================================

        botao_entrar = QPushButton(
            "ENTRAR"
        )

        botao_entrar.setCursor(
            Qt.PointingHandCursor
        )

        botao_entrar.setFixedHeight(
            84
        )
        botao_entrar.setFixedWidth(
           530
        )

        botao_entrar.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                border: none;
                border-radius: 9px;
                font-size: 17px;
                font-weight: 700;
            }

            QPushButton:hover {
                background-color: #04620F;
            }

            QPushButton:pressed {
                background-color: #04620F;
            }
        """)

        botao_entrar.clicked.connect(
            self._entrar
        )

        card_layout.addWidget(
            botao_entrar,
        0,
        Qt.AlignCenter
        )

    # =====================================================
    # LOGIN
    # =====================================================

    def _entrar(self):

        email = (
            self.campo_email
            .text()
            .strip()
        )

        usuario, _, dominio = (
            email.partition("@")
        )

        if (
            not usuario
            or "." not in dominio
        ):

            QMessageBox.warning(
                self,
                "E-mail inválido",
                "Digite um e-mail válido "
                "para continuar."
            )

            return

        if not ControleDeAcesso.esta_autorizado(
            email
        ):

            QMessageBox.warning(
                self,
                "Acesso não autorizado",
                "Este e-mail ainda não foi "
                "cadastrado no sistema.\n\n"
                "Peça para um administrador "
                "criar e liberar o seu perfil "
                "de acesso."
            )

            return

        self.login_solicitado.emit(
            email
        )

    def limpar(self):

        self.campo_email.clear()


# =========================================================
# LOGIN AUTORIZADO
# =========================================================

def _ao_logar_com_sucesso(
    email
):

    perfil = (
        ControleDeAcesso
        .perfil_de(email)
    )

    QMessageBox.information(
        None,
        "Login autorizado",
        f"E-mail autorizado: {email}\n"
        f"Perfil: {perfil}\n\n"
        "(Aguardando a tela de PIN.)"
    )


# =========================================================
# MAIN
# =========================================================

def main():

    app = QApplication(
        sys.argv
    )

    app.setStyleSheet("""
        QWidget {
            font-family: 'Segoe UI';
            color: #1C1C1C;
        }

        QMessageBox {
            background-color: white;
        }

        QMessageBox QLabel {
            color: #1C1C1C;
        }
    """)

    janela = QMainWindow()

    janela.setWindowTitle(
        "Embrapa Gado de Corte — Login"
    )

    # =====================================================
    # DIMENSÃO DA JANELA
    # =====================================================

    janela.resize(
        1920,
        1080
    )

    janela.setMinimumSize(
        1920,
        1080
    )

    # =====================================================
    # TELA DE LOGIN
    # =====================================================

    tela_login = LoginScreen()

    tela_login.login_solicitado.connect(
        _ao_logar_com_sucesso
    )

    janela.setCentralWidget(
        tela_login
    )

    # =====================================================
    # TELA CHEIA
    # =====================================================

    janela.showFullScreen()

    sys.exit(
        app.exec()
    )


# =========================================================
# EXECUTAR
# =========================================================

if __name__ == "__main__":
    main()