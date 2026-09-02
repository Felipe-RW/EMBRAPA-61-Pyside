
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
janela.setWindowTitle("Popup Ano Aberto")
janela.setFixedSize(1202, 639)
janela.setStyleSheet("""
    QWidget {
        background-color: white;
        border-radius: 20px
     
    }
""")
import qtawesome as qta
 
 
# icone = qta.icon('fa5s.exclamation-triangle', color='#FFC107')  # amarelo
 
circulo = QLabel("", janela)
 
icone_label = QLabel(circulo)
icone = qta.icon('fa5s.exclamation-triangle', color='#FFC107')
icone_label.setPixmap(icone.pixmap(114, 95))
icone_label.setAlignment(Qt.AlignCenter)
icone_label.setGeometry(0, 0, 238, 238)
 
circulo.setGeometry(475, 55, 238, 238)
circulo.setAlignment(Qt.AlignCenter)
 
circulo.setStyleSheet ("""
    QLabel {
        background-color: #FFE374;
        border-radius: 119px;    
        font-size: 95px;
        text-align: center;
        justify-content: center;        
        color: #356694;
}
""")
 
# icone = qta.icon('fa5s.exclamation-triangle', color='orange')
# icone_label.setPixmap(icone.pixmap(48, 48))
# icone_label = QLabel(circulo)  # parent = circulo, para ficar posicionado dentro dele
# icone = qta.icon('fa5s.exclamation-triangle', color='#356694')
# icone_label.setPixmap(icone.pixmap(90, 90))
# icone_label.setAlignment(Qt.AlignCenter)
# icone_label.setGeometry(0, 0, 238, 238)
 
titulo = QLabel("Esse ano está em aberto.", janela)
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
 
subtitulo = QLabel("Não é possível fecha-lo!", janela)
subtitulo.setGeometry(245, 380, 720, 30)
subtitulo.setAlignment(Qt.AlignCenter)
subtitulo.setStyleSheet("""
    QLabel {
        font-size: 24px;
        font-family: 'Verdana', sans-serif;
        font-weight: lighter;
}
""")
 
botao_fechar = QPushButton("Cancelar", janela)
botao_fechar.setGeometry(460, 550, 285, 48)
botao_fechar.setStyleSheet("""
    QPushButton{
        background-color: white;
        color: red;
        border: 2px solid;
        border-color: red;
        border-radius: 20px;
        font-size: 23px;
    }
 
    QPushButton:hover {
        background-color: red;
        color: white;
    }
 
    QPushButton:pressed {
        background-color: red;
    }
""")
                       
 
 
 
janela.show()
 
sys.exit(app.exec())
 
 