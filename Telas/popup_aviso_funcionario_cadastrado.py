import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QFrame,
    QVBoxLayout,
    QCheckBox,
    QLineEdit
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

circulo = QLabel("✓", janela)
circulo.setGeometry(475, 55, 238, 238)
circulo.setAlignment(Qt.AlignCenter)
circulo.setStyleSheet ("""
    QLabel {
        background-color: #C4E1FF;          
        border-radius: 119px;    
        font-size: 95px;
        text-align: center;
        justify-content: center;         
        color: #356694;
}
""")

titulo = QLabel("Empregado cadastrado com sucesso!", janela)
titulo.setGeometry(245, 330, 720, 50)
titulo.setAlignment(Qt.AlignCenter)
titulo.setStyleSheet("""
    QLabel{
        font-size: 34px;
        font-family: 'Verdana', sans-serif;
        font-weight: bold;    
        width: 100%;                 
        text-align: center;
}
""")

subtitulo = QLabel("O empregado foi adicionado ao sistema.", janela)
subtitulo.setGeometry(245, 380, 720, 30)
subtitulo.setAlignment(Qt.AlignCenter)
subtitulo.setStyleSheet("""
    QLabel {
        font-size: 24px;
        font-family: 'Verdana', sans-serif;
        font-weight: lighter;
}
""")

botao_fechar = QPushButton("Fechar", janela)
botao_fechar.setGeometry(460, 550, 285, 48)
botao_fechar.setStyleSheet("""
    QPushButton{
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