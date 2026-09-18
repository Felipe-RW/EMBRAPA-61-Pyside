from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys
from style import QSS



LOGO = "Imagens/logo_embrapa.png"
FECHAR = "Imagens/Vector.png"




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
        window_pin.setStyleSheet(QSS)
        window_pin.setObjectName("Painel")
        layout_principal.addWidget(window_pin)
        layout_principal.setAlignment(Qt.AlignCenter)
        window_pin.setLayout(layout_pin)
        layout_pin.setAlignment(Qt.AlignCenter)
        
        layout_pin.setSpacing(70)
        
        

        fechar = QLabel()
        map = QPixmap(FECHAR)
        fechar.setPixmap(map)
        fechar.setObjectName("Botao_fechar")
        layout_pin.addWidget(fechar, alignment=Qt.AlignmentFlag.AlignLeft)
        
        

        logo_embrapa = QLabel()
        pixmap = QPixmap(LOGO)
        logo_embrapa.setPixmap(pixmap)
        logo_embrapa.setScaledContents(True)
        layout_pin.addWidget(logo_embrapa, alignment=Qt.AlignmentFlag.AlignCenter)
        logo_embrapa.setObjectName("Logo")
        
        

        sub_titulo = QLabel("Digite o PIN enviado para seu E-mail")
        sub_titulo.setObjectName("sub_t")
        layout_pin.addWidget(sub_titulo)
        sub_titulo.setAlignment(Qt.AlignCenter)
        

        input_pin = QLineEdit()
        layout_pin.addWidget(input_pin,alignment=Qt.AlignmentFlag.AlignCenter)
        input_pin.setStyleSheet(QSS)
        input_pin.setObjectName("Input_pin")
        input_pin.setPlaceholderText("Digite o seu PIN.")
        

        botao_verificar = QPushButton("VERIFICAR")
        botao_verificar.setFixedSize(530,84)
        layout_pin.addWidget(botao_verificar,alignment=Qt.AlignmentFlag.AlignCenter)
        botao_verificar.setStyleSheet(QSS)
        botao_verificar.setObjectName("butao")
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela_pin()
    janela.show()
    sys.exit(app.exec())
