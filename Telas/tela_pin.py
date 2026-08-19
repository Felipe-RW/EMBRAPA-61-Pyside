from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys
from style import QSS



LOGO = "Imagens/logo_embrapa.jpg"




class tela_pin(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920,1080)
        self.setWindowTitle("PIN")
        self.setStyleSheet(QSS)
        
        

        layout_principal = QVBoxLayout()
        layout_pin = QVBoxLayout()
        self.setLayout  (layout_principal)
        window_pin = QWidget()
        window_pin.setFixedSize(1011,884)
        window_pin.setStyleSheet("background-color: #FFFFFF")
        layout_principal.addWidget(window_pin)
        layout_principal.setAlignment(Qt.AlignCenter)
        window_pin.setLayout(layout_pin)
        layout_pin.setAlignment(Qt.AlignCenter)
        
        

        logo_embrapa = QLabel()
        pixmap = QPixmap(LOGO)
        logo_embrapa.setPixmap(pixmap)
        # logo_embrapa.setFixedSize(308,172)
        logo_embrapa.setScaledContents(True)
        layout_pin.addWidget(logo_embrapa)
        logo_embrapa.setObjectName("Logo")

        sub_titulo = QLabel("Digite o PIN enviado para seu E-mail")
        sub_titulo.setObjectName("sub_t")
        layout_pin.addWidget(sub_titulo)
        sub_titulo.setAlignment(Qt.AlignCenter)
        

        input_pin = QLineEdit()
        layout_pin.addWidget(input_pin)
        input_pin.setFixedSize(612,100)

        botao_verificar = QPushButton("VERIFICAR")
        botao_verificar.setFixedSize(530,84)
        layout_pin.addWidget(botao_verificar)
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela_pin()
    janela.show()
    sys.exit(app.exec())
