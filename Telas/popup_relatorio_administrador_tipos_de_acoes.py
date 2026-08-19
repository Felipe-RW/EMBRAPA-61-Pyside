import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import Qt
 
app = QApplication(sys.argv)
 
janela = QWidget()
janela.setWindowTitle("Popup Relatório Administrador Tipos de Ações")
janela.setFixedSize(1202, 639)
janela.setStyleSheet("""
    QWidget {
        background-color: white;
        border-radius: 20px
     
    }
""")



titulo = QLabel("Relatório", janela)
titulo.setGeometry(350, 37, 500, 40)
titulo.setAlignment(Qt.AlignCenter)
titulo.setStyleSheet("""
    QWidget {
        color: black;
        font-size: 32px;
        font-family: verdana;
        font-weight: bold;
        background-color: transparent;            
    }
""")
 
texto = QLabel("Sua ação foi reenviada para os avaliadores.", janela)
texto.setGeometry(300, 375, 600, 30)
texto.setAlignment(Qt.AlignCenter)
texto.setStyleSheet("""
    QWidget {
        color: black;
        font-size: 24px;
        font-family: verdana;
        font-weight: regular;
        background-color: transparent;
    }
""")
 
botao = QPushButton("Fechar", janela)
botao.setGeometry(460, 550, 285, 48)
botao.setStyleSheet("""
    QPushButton {
        background-color: #172b8c;
        color: white;
        border: none;
        border-radius: 20px;
        font-size: 23px;
    }
    QPushButton:hover {
        background-color: #056510;
    }
    QPushButton:pressed {
        background-color: #056510;
    }
""")
 
 
janela.show()
 
sys.exit(app.exec())