import sys

from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QLabel


class Form(QWidget):
    def __init__(self):
        super().__init__()

        # Janela principal
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Form")
        self.setStyleSheet("""
            background-color: rgb(53, 99, 148);
        """)


        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(280, 60, 1600, 1010))

        self.frame.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
        """)

        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)


        self.frame_3 = QFrame(self.frame)
        self.frame_3.setGeometry(QRect(85, 123, 1431, 829))

        self.frame_3.setStyleSheet("""
            border: 2px solid gray;
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
        """)

        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)


        self.label_4 = QLabel(self.frame_3)
        self.label_4.setGeometry(QRect(40, 100, 121, 41))

        font_nome = QFont()
        font_nome.setFamily("Verdana")
        font_nome.setPointSize(20)
        font_nome.setBold(True)

        self.label_4.setFont(font_nome)

        self.label_4.setStyleSheet("""
            color: rgb(8, 8, 8);
        """)

        self.label_4.setText("Nome:")


        self.label_3 = QLabel(self.frame)
        self.label_3.setGeometry(QRect(632, 40, 301, 81))

        font_titulo = QFont()
        font_titulo.setFamily("Verdana")
        font_titulo.setPointSize(26)
        font_titulo.setBold(True)

        self.label_3.setFont(font_titulo)

        self.label_3.setStyleSheet("""
            color: rgb(11, 11, 11);
        """)

        self.label_3.setText("Ação Realizada")


        self.frame_2 = QFrame(self)
        self.frame_2.setGeometry(QRect(30, 0, 219, 189))

        self.frame_2.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            border-bottom-left-radius: 25px;
            border-bottom-right-radius: 25px;
        """)

        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)


        self.label = QLabel(self.frame_2)
        self.label.setGeometry(QRect(-10, 40, 231, 111))
        self.label.setText("")

        pixmap = QPixmap(
            r"C:\Users\GabrielOliveira\Downloads\Embrapa-Gado-de-Corte-Publicacoes.jpg"
        )

        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)


        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(300, 10, 401, 41))

        font_usuario = QFont()
        font_usuario.setFamily("Verdana")
        font_usuario.setPointSize(20)
        font_usuario.setBold(True)

        self.label_2.setFont(font_usuario)
        self.label_2.setText("Fulano da Silva Rodrigues")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Form()
    window.show()

    sys.exit(app.exec())