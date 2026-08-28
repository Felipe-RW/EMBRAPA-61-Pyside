import sys
from PySide6.QtCore import Qt,QPointF
from PySide6.QtGui import QColor, QPainter,QPen
from PySide6.QtWidgets import(
    QApplication,
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QGraphicsOpacityEffect,
)

class CheckIcon(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(120, 120)

    
    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)


        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#C6E0FF"))
        painter.drawEllipse(0,0,120,120)

        pen = QPen(QColor("#234B80"))
        pen.setWidth(1)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)

        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        painter.drawLine(
            QPointF(23,56),
            QPointF(44,77)
        )


        painter.drawLine(
            QPointF(44,77),
            QPointF(89,31)
        )


class SuccessPopup(QDialog):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowFlags(
            Qt.Dialog |
            Qt.FramelessWindowHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setFixedSize(576,806)

        self.setup_ui()


    def setup_ui(self):

        container = QWidget(self)
        container.setObjectName("container")
        container.setGeometry(0,0,576,306)

        container.setStyleSheet("""
                                
            QWidget#container {
                background-color: white;
                border-radius: 10px;
            }

            QLabel#title {
                color: #111111;
                font-size: 20px;
                font-weight: 700;
            }

            QLabel#subtitle {
                color: #222222;
                font-size: 13px;
            }

            QPushButton {
                background-color: #17298B;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 12px;
                font-weight: 700;
                padding: 0px;
            }

            QPushButton:hover {
                background-color: #2037A5;
            }

            QPushButton:pressed {
                background-color: #111F6D;
            }

            """
        )

        layout = QVBoxLayout(container)
        layout.setContentsMargins(0,25,0,26)
        layout.setSpacing(0)

        icon = CheckIcon()
        layout.addWidget(icon, alignment=Qt.AlignHCenter)

        layout.addSpacing(19)

        title = QLabel("Sua ação foi postada!")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        subtitle = QLabel(
            "Sua ação foi enviada para os avaliadores."
        )

            
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        layout.addWidget(subtitle)

        layout.addSpacing(59)

        button = QPushButton("Fechar")
        button.setFixedSize(137,23)
        button.clicked.connect(self.accept)

        layout.addWidget(
            button,
            alignment=Qt.AlignHCenter
        )

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minha Aplicação")
        self.resize(800, 500)

        button = QPushButton("Postar ação", self)
        button.setGeometry(550, 420, 200, 40)

        button.setStyleSheet("""
            QPushButton {
                background-color: #17298B;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 12px;
                font-weight: 700;
                padding: 0px;
            }

            QPushButton:hover {
                background-color: #2037A5;
            }

            QPushButton:pressed {
                background-color: #111F6D;
            }
        """)

        button.clicked.connect(self.show_success)


    def show_success(self):

        popup = SuccessPopup(self)

        popup.move(
            self.x() + (self.width() - popup.width()) // 2,
            self.y() + (self.height()) - popup.height() // 2
        )

        popup.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())