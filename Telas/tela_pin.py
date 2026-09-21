from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys




LOGO = "Imagens/logo_embrapa.png"
FECHAR = "Imagens/Vector.png"

BACKGROUND = "Imagens/background.png"
VERDE =  "#058914"
BRANCO = "#FFFFFF"
PRETO = "#000000"




class tela_pin(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920,1080)
        self.setWindowTitle("PIN")
        self.setStyleSheet(f"background-image:url({BACKGROUND})")


        layout_principal = QVBoxLayout()
        layout_pin = QVBoxLayout()
        self.setLayout  (layout_principal)
        window_pin = QWidget()
        window_pin.setFixedSize(1011,884)
        
        window_pin.setStyleSheet(f"""
        background:{BRANCO};
        border-radius: 10px;"""
        )
        
        layout_principal.addWidget(window_pin)
        layout_principal.setAlignment(Qt.AlignCenter)
        window_pin.setLayout(layout_pin)
        layout_pin.setAlignment(Qt.AlignCenter)
        
        layout_pin.setSpacing(80)
        
        

        fechar = QLabel()
        map = QPixmap(FECHAR)
        fechar.setPixmap(map)
        fechar.setStyleSheet("background: none;")
        layout_pin.addWidget(fechar, alignment=Qt.AlignmentFlag.AlignLeft)
        
        

        logo_embrapa = QLabel()
        pixmap = QPixmap(LOGO)
        logo_embrapa.setPixmap(pixmap)
        logo_embrapa.setScaledContents(True)
        layout_pin.addWidget(logo_embrapa, alignment=Qt.AlignmentFlag.AlignCenter)
        logo_embrapa.setStyleSheet("""
        max-width :476px;
        max-height: 206px;""")
        
        

        sub_titulo = QLabel("Digite o PIN enviado para seu E-mail")
        sub_titulo.setStyleSheet(f"""
            font-weight: bold;
            font-size: 20px;
            background : transparent;
            font-family: Verdana;
            """)
        layout_pin.addWidget(sub_titulo)
        sub_titulo.setAlignment(Qt.AlignCenter)
        

        input_pin = QLineEdit()
        layout_pin.addWidget(input_pin,alignment=Qt.AlignmentFlag.AlignCenter)
        input_pin.setStyleSheet(f"""
        border: 1px solid gray;
        border-radius: 8px;
        padding-left: 20px;
        padding-right: 20px;""")
        input_pin.setFixedSize(612, 99)
       
        input_pin.setPlaceholderText("Digite o seu PIN.")
        

        botao_verificar = QPushButton("VERIFICAR")
        botao_verificar.setFixedSize(530,84)
        layout_pin.addWidget(botao_verificar,alignment=Qt.AlignmentFlag.AlignCenter)
        botao_verificar.setStyleSheet(f"""
            background-color: {VERDE};
            color:{BRANCO};
            font-size: 20px;
            font-family: Verdana;
            font-weight: bold;
            """
            )
        
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela_pin()
    janela.show()
    sys.exit(app.exec())
