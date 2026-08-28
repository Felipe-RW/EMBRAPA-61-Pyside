import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QFrame,
    QVBoxLayout,
    QCheckBox,
    QLineEdit
)
from PySide6.QtCore import Qt
 
app = QApplication(sys.argv)
 
janela = QWidget()
janela.setWindowTitle("Popup Relatório Administrador Tipos de Ações")
janela.setFixedSize(1202, 639)
janela.setStyleSheet("""
    QWidget {
        background-color: white;
        border-radius: 20px
     
    }
""")

titulo = QLabel("Relatório", janela)
titulo.setGeometry(350, 37, 500, 40)
titulo.setAlignment(Qt.AlignCenter)
titulo.setStyleSheet("""
    QWidget {
        color: black;
        font-size: 32px;
        font-family: verdana;
        font-weight: bold;
        background-color: transparent;            
    }
""")
 
botao_relatorio_tipos_de_acoes = QPushButton("Relatório de Ações", janela)
botao_relatorio_tipos_de_acoes.setGeometry(54, 150, 303, 40)
botao_relatorio_tipos_de_acoes.setStyleSheet("""
    QPushButton {
        color: white;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #356394;    
        border-radius: 20px;                 
    }
""")

opcoes_relatorio = QFrame(janela)
opcoes_relatorio.setGeometry(54, 215, 1094, 354)
opcoes_relatorio.setStyleSheet("""
    QWidget {
    background-color: #DFDFDF; 
    border-radius: 0px;                             
}
""")

acoes = QLabel("Anos", opcoes_relatorio)
acoes.setGeometry(61, 28, 67, 30)
acoes.setStyleSheet("""
    QLabel {
    color: black;
    font-size: 20px;
    font-family: verdana;
    font-weight: bold 
}
""")

botao_selecionar_acoes = QPushButton("Selecionar Anos", opcoes_relatorio)
botao_selecionar_acoes.setGeometry(61, 74, 192, 30)
botao_selecionar_acoes.setStyleSheet("""
    QPushButton {
    color: white;
    font-size: 13;
    font-family: verdana;
    font-weight: bold;
    background-color: #356394;
    border-radius: 15px                          
}
""")

botao_todas_as_acoes = QPushButton("Todos os Anos", opcoes_relatorio)
botao_todas_as_acoes.setGeometry(275, 74, 192, 30)
botao_todas_as_acoes.setStyleSheet("""
    QPushButton {
    color: black;
    font-size: 13;
    font-family: verdana;
    font-weight: bold;
    background-color: white;
    border-radius: 15px                          
}
""")

caixa_de_busca = QLineEdit(opcoes_relatorio)
caixa_de_busca.setPlaceholderText("Pesquisar...")
caixa_de_busca.setGeometry(113, 125, 300, 25)
caixa_de_busca.setStyleSheet("""
    QLineEdit {
    background-color: white;
    border-radius: 10px;
    padding: 3px;
    border: 0.5px solid #686868;
    }
""")

selecionar_ano1 = QCheckBox("2026", opcoes_relatorio)
selecionar_ano1.setGeometry(61, 170, 400, 20)
selecionar_ano1.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter;
}
""")

selecionar_ano2 = QCheckBox("2025", opcoes_relatorio)
selecionar_ano2.setGeometry(61, 200, 400, 20)
selecionar_ano2.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_ano3 = QCheckBox("2024", opcoes_relatorio)
selecionar_ano3.setGeometry(61, 230, 400, 20)
selecionar_ano3.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_ano4 = QCheckBox("2023", opcoes_relatorio)
selecionar_ano4.setGeometry(61, 260, 400, 20)
selecionar_ano4.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

dados = QLabel("Dados", opcoes_relatorio)
dados.setGeometry(624, 28, 75, 30)
dados.setStyleSheet("""
    QLabel {
    color: black;
    font-size: 20px;
    font-family: verdana;
    font-weight: bold 
}
""")

selecionar_dados = QCheckBox("Setor", opcoes_relatorio)
selecionar_dados.setGeometry(624, 74, 400, 20)
selecionar_dados.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_dados2 = QCheckBox("Status", opcoes_relatorio)
selecionar_dados2.setGeometry(624, 104, 400, 20)
selecionar_dados2.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

janela.show()
 
sys.exit(app.exec())