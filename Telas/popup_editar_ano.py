from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys
from style import QSS

DROPDOWN = "Imagens/Vector_dropdown.png"

class popup_editar_ano(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(750,500)
        self.setWindowTitle("Editar ano")


        self.layout_vertical = QVBoxLayout()
        

        self.setLayout(self.layout_vertical)

        background_gaveta = QFrame()

        background_gaveta.setStyleSheet(QSS)

        background_gaveta.setObjectName("background_gaveta")

        self.layout_vertical.addWidget(background_gaveta,alignment=Qt.AlignmentFlag.AlignTop)
        
        self.layout_gaveta = QHBoxLayout()  

        self.layout_gaveta_interna = QHBoxLayout()

        background_gaveta_branco = QFrame()

        ano = QLabel("2027")

        icon = QLabel()
        pixmap = QPixmap(DROPDOWN)
        icon.setPixmap(pixmap)


        background_gaveta_branco.setLayout(self.layout_gaveta_interna)

        self.layout_gaveta_interna.addWidget(ano,alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout_gaveta_interna.addWidget(icon,alignment=Qt.AlignmentFlag.AlignRight)

        background_gaveta_branco.setStyleSheet("background-color: white")

        self.layout_gaveta.addWidget(background_gaveta_branco)

        background_gaveta.setLayout(self.layout_gaveta)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = popup_editar_ano()
    janela.show()
    sys.exit(app.exec())