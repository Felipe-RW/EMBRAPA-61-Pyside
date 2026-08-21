from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QButtonGroup

class btn_layout(QPushButton):
    def __init__(self, path, texto, parent=None):
        super().__init__(parent)

        self.setStyleSheet("text-align: left; padding: 0px;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)

        self.logica = QButtonGroup(self)
        self.logica.setExclusive(True)

        self.icone_label = QLabel()
        self.icone_label.setPixmap(QIcon(path).pixmap(QSize(23, 25)))

        self.texto_label = QLabel(texto)
        self.texto_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.icone_label)
        layout.addStretch()
        layout.addWidget(self.texto_label)
        layout.addStretch()

    def setText(self, texto):
        self.texto_label.setText(texto)
        
    def setIcon(self, icone_path, size=QSize(23, 25)):
        self.icone_label.setPixmap(QIcon(icone_path).pixmap(size))