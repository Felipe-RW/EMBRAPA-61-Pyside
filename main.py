import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from Telas.tela_login import LoginScreen


def ao_logar_com_sucesso(email):
    print("E-mail informado:", email)

def main():

    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QWidget {
            font-family: 'Segoe UI';
            color: #1C1C1C;
        }
    """)

    janela = QMainWindow()

    janela.setWindowTitle(
        "Embrapa Gado de Corte — Login"
    )

    janela.setWindowFlags(
        Qt.Window |
        Qt.WindowMinimizeButtonHint |
        Qt.WindowMaximizeButtonHint |
        Qt.WindowCloseButtonHint
    )

    janela.resize(1280, 720)

    janela.setMinimumSize(
        1024,
        600
    )

    tela_login = LoginScreen()

    tela_login.login_solicitado.connect(
        ao_logar_com_sucesso
    )

    janela.setCentralWidget(
        tela_login
    )

    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()