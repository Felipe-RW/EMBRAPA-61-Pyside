import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import Qt

from Telas.tela_login import LoginScreen
from Telas.tela_pin import tela_pin

app = QApplication(sys.argv)

janela = QMainWindow()
janela.setWindowTitle("Embrapa Gado de Corte – Login")
janela.setWindowFlags(
    Qt.Window |
    Qt.WindowMinimizeButtonHint |
    Qt.WindowMaximizeButtonHint |
    Qt.WindowCloseButtonHint
)
janela.resize(1280, 720)
janela.setMinimumSize(1024, 600)

stacked_widget = QStackedWidget()

login = LoginScreen()
pin = tela_pin()

stacked_widget.addWidget(login)
stacked_widget.addWidget(pin)

login.login_solicitado.connect(lambda email: stacked_widget.setCurrentWidget(pin))
pin.voltar_login_solicitado.connect(lambda: stacked_widget.setCurrentWidget(login))

janela.setCentralWidget(stacked_widget)

janela.showMaximized()
sys.exit(app.exec())