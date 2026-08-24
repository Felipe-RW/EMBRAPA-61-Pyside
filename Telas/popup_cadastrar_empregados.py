import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QCheckBox,
    QComboBox,
    QLineEdit
)
from PySide6.QtCore import Qt


class PopUp_Cadastrarempregados(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastrar Empregados")
        self.setFixedSize(1436, 664)
        self.setStyleSheet("""
            QWidget {
                background-color: #92C498;
                border-radius: 20px
            }
        """)

        # Alterado de QLabel para QLineEdit com PlaceholderText
        self.campo_nome = QLineEdit(self)
        self.campo_nome.setGeometry(30, 90, 1376, 92)
        self.campo_nome.setPlaceholderText("Digite o nome:")
        self.campo_nome.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #4A4A4A;
                border-radius: 20px;
                font-family: verdana;
                font-weight: bold;
                font-size: 20px;   
                padding-left: 15px;
             }
        """)

        # Alterado de QLabel para QLineEdit com PlaceholderText
        self.campo_email = QLineEdit(self)
        self.campo_email.setGeometry(30, 270, 1376, 92)
        self.campo_email.setPlaceholderText("Digite o email:")
        self.campo_email.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #4A4A4A;
                border-radius: 20px;
                font-family: verdana;
                font-weight: bold;
                font-size: 20px;   
                padding-left: 15px;
             }
        """)

        self.botao_cancelar = QPushButton("Cancelar", self)
        self.botao_cancelar.setGeometry(30, 550, 563, 67)
        self.botao_cancelar.setStyleSheet("""
            QPushButton {
                background-color: #172b8c;
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-family: verdana;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0C2750;
            }
            QPushButton:pressed {
                background-color: #0C2750;
            }
        """)

        self.botao_cadastrar = QPushButton("Cadastrar", self)
        self.botao_cadastrar.setGeometry(840, 550, 563, 67)
        self.botao_cadastrar.setStyleSheet("""
            QPushButton {
                background-color: #058914;
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-family: verdana;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #04620F;
            }
            QPushButton:pressed {
                background-color: #04620F;
            }
        """)

        self.checkbox_pesquisador = QCheckBox("Pesquisador", self)
        self.checkbox_pesquisador.setGeometry(1200, 400, 200, 100)
        self.checkbox_pesquisador.setStyleSheet("""
            QCheckBox {
                color: black;
                font-size: 20px;
                font-family: verdana;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
                background-color: white; 
                border: 1px solid #333333;
                border-radius: 10px;
            }
            QCheckBox::indicator:checked {
                background-color: #7DA883;
                image: url(check.png);  
            }
        """)

        self.checkbox_comite = QCheckBox("Comitê", self)
        self.checkbox_comite.setGeometry(900, 400, 200, 100)
        self.checkbox_comite.setStyleSheet("""
            QCheckBox {
                color: black;
                font-size: 20px;
                font-family: verdana;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
                background-color: white; 
                border: 1px solid #333333;
                border-radius: 10px;
            }
            QCheckBox::indicator:checked {
                background-color: #7DA883; 
                image: url(check.png); 
            }
        """)

        self.checkbox_administrador = QCheckBox("Administrador", self)
        self.checkbox_administrador.setGeometry(300, 400, 200, 100)
        self.checkbox_administrador.setStyleSheet("""
            QCheckBox {
                color: black;
                font-size: 20px;
                font-family: verdana;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
                background-color: white; 
                border: 1px solid #333333;
                border-radius: 10px;
            }
            QCheckBox::indicator:checked {
                background-color: #7DA883; 
                image: url(check.png); 
            }
        """)

        self.texto_nome = QLabel(self)
        self.texto_nome.setGeometry(30, 35, 300, 50)
        self.texto_nome.setText("Nome do empregado:")
        self.texto_nome.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: verdana;
                font-weight: bold;      
            }
        """)

        self.texto_email = QLabel(self)
        self.texto_email.setGeometry(30, 210, 300, 50)
        self.texto_email.setText("Email do empregado:")
        self.texto_email.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: verdana;
                font-weight: bold;      
            }
        """)

        self.texto_funcao = QLabel(self)
        self.texto_funcao.setGeometry(30, 422, 200, 50)
        self.texto_funcao.setText("Tipo de função:")
        self.texto_funcao.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: verdana;
                font-weight: bold;      
            }
        """)

        self.dropdown_validador = QComboBox(self)
        self.dropdown_validador.addItems(["SPAT", "SPIT", "NCO"])
        self.dropdown_validador.setGeometry(580, 422, 220, 45)
        self.dropdown_validador.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 18px;
                font-family: Verdana;
                font-weight: bold;
                border-radius: 0px;
                border: 1px solid gray;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = PopUp_Cadastrarempregados()
    janela.show()
    sys.exit(app.exec())
