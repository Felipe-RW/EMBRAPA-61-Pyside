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
btn_cadastrar.setGeometry(200, 300, 20, 30)
btn_cadastrar.setStyleSheet( "background-color: #27ae60; color: white; font-weight: bold; border-radius: 20px; height: 44px; width: 20px;")

layout_principal.addStretch

layout_principal.addWidget(btn_cadastrar)

layout_principal.addStretch()


janela.show()
sys.exit(app.exec())