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
janela.setWindowTitle("Ação atualizada")
janela.setFixedSize(1200, 640 )
janela.setStyleSheet("""
    QWidget {
        background-color: white;
        border-radius: 20px
     
    }
""")

circulo = QLabel(janela)
circulo.setGeometry(475, 55, 238, 238)
circulo.setAlignment(Qt.AlignCenter)
circulo.setText("✓")
circulo.setStyleSheet("""
    QLabel {
        background-color: #C4E1FF;
        color: #356394;
        border: none;
        border-radius: 119px;
        font-size: 95px;
        font-weight: normal;
    }
""")

titulo = QLabel("Sua ação foi atualizada!", janela)
titulo.setGeometry(350, 330, 500, 40)
titulo.setAlignment(Qt.AlignCenter)
titulo.setStyleSheet(""" 
    QWidget {
        color: black;
        font-size: 34px;
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