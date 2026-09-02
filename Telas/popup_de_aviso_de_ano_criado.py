from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

class PopupDeAvisoDeAnoCriado(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("Sucesso")
        self.setMinimumSize(1200, 640)
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 30px;
            }
        """)

        
        self.container = QWidget(self)
        self.container.setObjectName("container")
        self.container.resize(1920, 1080)

        
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(0, 40, 0, 60)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        
        circulo = QLabel("✓")
        circulo.setMinimumSize(210, 210)
        circulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        circulo.setStyleSheet("""
            QLabel {
                background-color: #d9ebff;
                border-radius: 105px;
                font-size: 90px;
                color: #1f2d87;
            }
        """)

        titulo = QLabel("O ano foi criado!")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            QLabel {
                background: white;
                font-size: 30px;
                font-weight: 700;
                color: #222;
            }
        """)

        msg1 = QLabel("Ano adicionado ao sistema com sucesso!")
        msg1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        msg1.setStyleSheet("""
            QLabel {
                background: white;
                font-size: 21px;
                color: #444;
            }
        """)

        
        botao = QPushButton("Fechar")
        botao.setMinimumSize(370, 56)
        botao.setStyleSheet("""
            QPushButton {
                background-color: #1f2d87;
                color: white;
                border: none;
                border-radius: 28px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #2a3cb0;
            }
        """)
        botao.clicked.connect(self.close)

        
        layout.addWidget(circulo, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(35)
        layout.addWidget(titulo)
        layout.addSpacing(10)
        layout.addWidget(msg1)
        layout.addSpacing(5)
        layout.addSpacing(50)
        layout.addWidget(botao, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)