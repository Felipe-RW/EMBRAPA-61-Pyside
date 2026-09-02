import sys

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QPushButton,
    QWidget,
)


class CheckIcon(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(238, 238)

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)


        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#C6E0FF"))

        painter.drawEllipse(
            0,
            0,
            238,
            238
        )

    
        pen = QPen(QColor("#234B80"))

        pen.setWidth(2)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)

        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        painter.drawLine(
            QPointF(46, 119),
            QPointF(91, 164)
        )

        painter.drawLine(
            QPointF(91, 164),
            QPointF(187, 67)
        )


class SuccessPopup(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(
            Qt.Dialog |
            Qt.FramelessWindowHint
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )


        self.setFixedSize(1202, 639)

        self.setup_ui()

    def setup_ui(self):


        container = QWidget(self)
        container.setObjectName("container")

        container.setGeometry(
            0,
            0,
            self.width(),
            self.height()
        )

        container.setStyleSheet("""

            QWidget#container {
                background-color: white;
                border-radius: 20px;
            }

            QLabel#title {
                color: #111111;
                font-size: 38px;
                font-weight: 700;
                background: transparent;
            }

            QLabel#subtitle {
                color: #222222;
                font-size: 27px;
                font-weight: 400;
                background: transparent;
            }

            QPushButton {
                background-color: #17298B;
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-weight: 400;
                padding: 0px;
            }

            QPushButton:hover {
                background-color: #058914;
            }

            QPushButton:pressed {
                background-color: #04620F;
            }

        """)


        icon = CheckIcon(container)

        icon.setGeometry(
            482,
            52,
            238,
            238
        )


        title = QLabel(
            "Sua ação foi postada!",
            container
        )

        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        title.setGeometry(
            0,
            333,
            1202,
            48
        )

    
        subtitle = QLabel(
            "Sua ação foi enviada para os avaliadores.",
            container
        )

        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setGeometry(
            0,
            384,
            1202,
            38
        )

        button = QPushButton(
            "Fechar",
            container
        )

        button.setFixedSize(
            285,
            49
        )

        button.move(
            459,
            535
        )


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Minha Aplicação"
        )

        self.setFixedSize(
            1300,
            700
        )

        self.show_success()

    def show_success(self):

        popup = SuccessPopup(self)


        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        x = (
            screen_geometry.x()
            +
            (
                screen_geometry.width()
                -
                popup.width()
            ) // 2
        )

        y = (
            screen_geometry.y()
            +
            (
                screen_geometry.height()
                -
                popup.height()
            ) // 2
        )

        popup.move(x, y)

        popup.exec()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(
        app.exec()
    )