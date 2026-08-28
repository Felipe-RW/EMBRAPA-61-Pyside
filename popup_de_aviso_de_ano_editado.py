import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QApplication
import estilo

class PopupDeAvisoDeAnoCriado(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("Sucesso")
        self.setFixedSize(1000, 650)
        self.setStyleSheet(estilo.ESTILO_Geral)
        
        self.container = QWidget(self)
        self.container.setObjectName("container")
        self.container.resize(1000, 550)
        
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(0, 40, 0, 60)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        circulo = QLabel("✓")
        circulo.setFixedSize(210, 210)
        circulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        circulo.setStyleSheet(estilo.ESTILO_Circulo)

        titulo = QLabel("As informações do ano foram atualizadas!")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet(estilo.ESTILO_Titulo)

        msg1 = QLabel("Alterações realizadas com sucesso!")
        msg1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        msg1.setStyleSheet(estilo.ESTILO_Mensagem1)

        botao = QPushButton("Fechar")
        botao.setFixedSize(370, 56)
        botao.setStyleSheet(estilo.ESTILO_Botao)
        botao.clicked.connect(self.close)

        layout.addWidget(circulo, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(35)
        layout.addWidget(titulo)
        layout.addSpacing(10)
        layout.addWidget(msg1)
        layout.addSpacing(5)
        layout.addSpacing(50)
        layout.addWidget(botao, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    
    janela = PopupDeAvisoDeAnoCriado()
    janela.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()