import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication, QDialog, QGraphicsDropShadowEffect,
    QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget
)


class SuccessPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(1202, 639)

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)

        container_popup = QWidget(self)
        container_popup.setObjectName("container")
        container_popup.setStyleSheet("""
            QWidget#container {
                background-color: #ffffff;
                border-radius: 16px;
            }
        """)

        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(0)
        sombra.setYOffset(6)
        sombra.setColor(QColor(0, 0, 0, 35))
        container_popup.setGraphicsEffect(sombra)

        layout_container = QVBoxLayout(container_popup)
        layout_container.setAlignment(Qt.AlignCenter)
        layout_container.setSpacing(50)
        layout_container.setContentsMargins(40, 35, 40, 35)

        icone_label = QLabel("✓")
        icone_label.setAlignment(Qt.AlignCenter)
        icone_label.setFixedSize(218, 218)
        icone_label.setStyleSheet("""
            QLabel {
                background-color: #e0edff;
                color: #2b52f6;
                border-radius: 109px;
                font-size: 90px;
                font-weight: bold;
            }
        """)
        
        layout_icone = QHBoxLayout()
        layout_icone.addStretch()
        layout_icone.addWidget(icone_label)
        layout_icone.addStretch()
        layout_container.addLayout(layout_icone)

        layout_container.addSpacing(0)

        titulo_label = QLabel("As informações do setor foram criadas!")
        titulo_label.setAlignment(Qt.AlignCenter)
        titulo_label.setStyleSheet("""
            QLabel {
                color: #1e293b;
                font-size: 36px;
                font-weight: bold;
                font-family: 'Segoe UI', sans-serif;
            }
        """)

        subtitulo_label = QLabel("Alterações realizadas com sucesso!")
        subtitulo_label.setAlignment(Qt.AlignCenter)
        subtitulo_label.setStyleSheet("""
            QLabel {
                color: #64748b;
                font-size: 30px;
                font-family: 'Segoe UI', sans-serif;
            }
        """)

        layout_container.addWidget(titulo_label)
        layout_container.addWidget(subtitulo_label)

        layout_container.addSpacing(5)

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setCursor(Qt.PointingHandCursor)
        botao_fechar.setFixedSize(285, 48)
        botao_fechar.setStyleSheet("""
            QPushButton {
                background-color: #102174;
                color: white;
                border-radius: 18px;
                font-size: 23px;
                font-weight: bold;
                font-family: 'Segoe UI', Inter;
                border: none;
            }
            QPushButton:hover {
                background-color: #058914;
            }
            QPushButton:pressed {
                background-color: #057111;
            }
        """)
        botao_fechar.clicked.connect(self.accept)

        layout_botao = QHBoxLayout()
        layout_botao.addStretch()
        layout_botao.addWidget(botao_fechar)
        layout_botao.addStretch()
        layout_container.addSpacing(100)
        layout_container.addLayout(layout_botao)

        layout_principal.addWidget(container_popup)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    popup = SuccessPopup()
    popup.exec()