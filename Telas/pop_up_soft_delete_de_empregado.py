import sys
from PySide6.QtGui import Qt, QPixmap
from PySide6.QtWidgets import (
    QLabel, 
    QPushButton, 
    QVBoxLayout,
    QHBoxLayout,
    QWidget, 
    QApplication)

ESTILO = """   
    #container {
        background-color: #FFFFFF;
        border-radius: 20px;
    }

    #icone_aviso {
        background-color: #FFE374;
        border-radius: 100px;
    }

    #titulo {
        color: #000000;
        font-size: 24px;
        font-weight: bold;
    }

    #msg_aviso {
        color: #000000;
        font-size: 20px;
    }

    #botao_cancelar {
        color: #CD0000;
        font-size: 23px;
        border: 2.5px solid #CD0000;
        border-radius: 20px;
    }

    #botao_cancelar:hover {
        color: #FFFFFF;
        font-size: 23px;
        background-color: #CD0000;
        border: 2.5px solid #CD0000;
        border-radius: 20px;
    }

    #botao_desativar {
        color: #FFFFFF;
        font-size: 23px;
        background-color: #102174;
        border-radius: 20px;
    }

    #botao_desativar:hover {
        background-color: #056510;
    }
"""

class PopupDeAvisoDeSoftDeleteDeEmpregado(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.setWindowTitle("Aviso de soft delete!")
        self.setFixedSize(1202, 639)
        self.setObjectName("pop_up")
        self.setStyleSheet(ESTILO)
        
        self.container = QWidget(self)
        self.container.setObjectName("container")
        self.container.resize(1202, 639)
        
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(0, 40, 0, 60)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        widget_botoes = QWidget()
        layout_botoes = QHBoxLayout()
        widget_botoes.setLayout(layout_botoes)
        
        icone_aviso = QLabel()
        icone_aviso.setPixmap(QPixmap("icone_de_aviso.png"))
        icone_aviso.setObjectName("icone_aviso")
        icone_aviso.setFixedSize(210, 210)
        icone_aviso.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo = QLabel("Tem certeza que deseja desativar esse empregado?")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        msg_aviso = QLabel("Os dados sobre o empregado continuarão armazenadas, mas ele perderá o acesso ao sistema.")
        msg_aviso.setObjectName("msg_aviso")
        msg_aviso.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("botao_cancelar")
        botao_cancelar.setFixedSize(285, 48)
        botao_cancelar.clicked.connect(self.close)

        botao_desativar = QPushButton("Desativar")
        botao_desativar.setObjectName("botao_desativar")
        botao_desativar.setFixedSize(285, 48)
        #Conectar o método que desativa o empregado aqui.

        layout.addWidget(icone_aviso, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(50)
        layout.addWidget(titulo)
        layout.addSpacing(20)
        layout.addWidget(msg_aviso)
        layout.addSpacing(150)
        layout.addWidget(widget_botoes)
        layout_botoes.addWidget(botao_cancelar, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_botoes.addWidget(botao_desativar, alignment=Qt.AlignmentFlag.AlignRight)
        layout_botoes.setContentsMargins(50, 0, 50, 0)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    
    janela = PopupDeAvisoDeSoftDeleteDeEmpregado()
    janela.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()