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
 
botao_relatorio_tipos_de_acoes = QPushButton("Relatório de Tipos de Ações", janela)
botao_relatorio_tipos_de_acoes.setGeometry(54, 150, 303, 40)
botao_relatorio_tipos_de_acoes.setStyleSheet("""
    QPushButton {
        color: white;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #356394;    
        border-radius: 20px;                 
    }
""")

botao_relatorio_empregados = QPushButton("Relatório de Empregados", janela)
botao_relatorio_empregados.setGeometry(375, 150, 303, 40)
botao_relatorio_empregados.setStyleSheet("""
    QPushButton {
        color: black;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #DFDFDF;    
        border-radius: 20px;                 
    }
""")

botao_relatorio_anos = QPushButton("Relatório de Anos", janela)
botao_relatorio_anos.setGeometry(696, 150, 303, 40)
botao_relatorio_anos.setStyleSheet("""
    QPushButton {
        color: black;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #DFDFDF;    
        border-radius: 20px;                 
    }
""")
 
janela.show()
 
sys.exit(app.exec())