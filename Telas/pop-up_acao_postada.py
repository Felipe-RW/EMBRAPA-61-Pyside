
import sys

from PySide6.QtCore import Qt, QPointF, QVariantAnimation
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QPushButton


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
        self.setFixedSize(
            1202,
            639
        )

        self.criar_interface()

    def criar_interface(self):

        self.setStyleSheet("""
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
            }

            QPushButton:hover {
                background-color: #058914;
            }

            QPushButton:pressed {
                background-color: #04620F;
            }
        """)

        title = QLabel(
            "Sua ação foi postada!",
            self
        )

        title.setObjectName(
            "title"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setGeometry(
            0,
            333,
            1202,
            48
        )


        subtitle = QLabel(
            "Sua ação foi enviada para os avaliadores.",
            self
        )

        subtitle.setObjectName(
            "subtitle"
        )

        subtitle.setAlignment(
            Qt.AlignCenter
        )

        subtitle.setGeometry(
            0,
            384,
            1202,
            38
        )


        self.button = QPushButton(
            "Fechar",
            self
        )

        self.button.setFixedSize(
            285,
            49
        )

        self.button.move(
            459,
            535
        )

        self.button.clicked.connect(
            self.close
        )


        self.animacao = QVariantAnimation(
            self
        )

        self.animacao.setDuration(
            200
        )

        self.animacao.setStartValue(
            QColor("#17298B")
        )

        self.animacao.setEndValue(
            QColor("#058914")
        )

        self.animacao.valueChanged.connect(
            self.mudar_cor
        )

    def mudar_cor(self, cor):

        self.button.setStyleSheet(f"""
            QPushButton {{
                background-color: {cor.name()};
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-weight: 400;
            }}
        """)

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )


        painter.setPen(
            Qt.NoPen
        )

        painter.setBrush(
            QColor("white")
        )

        painter.drawRoundedRect(
            0,
            0,
            self.width(),
            self.height(),
            20,
            20
        )

        painter.setBrush(
            QColor("#C6E0FF")
        )

        painter.drawEllipse(
            482,
            52,
            238,
            238
        )

        pen = QPen(
            QColor("#234B80")
        )

        pen.setWidth(
            5
        )

        pen.setCapStyle(
            Qt.RoundCap
        )

        pen.setJoinStyle(
            Qt.RoundJoin
        )

        painter.setPen(
            pen
        )

        painter.setBrush(
            Qt.NoBrush
        )

        painter.drawLine(
            QPointF(528, 171),
            QPointF(573, 216)
        )

        painter.drawLine(
            QPointF(573, 216),
            QPointF(669, 119)
        )

        painter.end()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    popup = SuccessPopup()

    # Centralizar na tela
    screen = QApplication.primaryScreen()
    geometry = screen.availableGeometry()

    x = (
        geometry.x()
        + (geometry.width() - popup.width()) // 2
    )

    y = (
        geometry.y()
        + (geometry.height() - popup.height()) // 2
    )

    popup.move(
        x,
        y
    )

    popup.exec()

    sys.exit(app.exec())

