import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QFormLayout, QGridLayout, QLabel, QLineEdit, 
    QPushButton, QCheckBox, QComboBox, QFrame,
)
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Gestão de Empregados")
janela.resize(1920, 1080)

layout_principal = QVBoxLayout(janela)
layout_principal.setContentsMargins(20, 20, 20, 20)
layout_principal.setSpacing(15)

titulo = QLabel("Cadastro e Configurações")
titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
titulo.setAlignment(Qt.AlignCenter)

layout_principal.addWidget(titulo)

btn_cadastrar = QPushButton("Cadastrar Empregados")
btn_cadastrar.setStyleSheet( "background-color: #27ae60; color: white; font-weight: bold; border-radius: 20px;")
btn_cadastrar.setGeometry(100, 100, 300, 200)

layout_principal.addSpacing(15)
layout_principal.addWidget(btn_cadastrar)

layout_superior = QHBoxLayout()
layout_superior.addWidget(btn_cadastrar)
layout_superior.addStretch()

layout_principal.addLayout(layout_superior)
layout_principal.addStretch()

layout_superior.addStretch()


janela.show()
sys.exit(app.exec())