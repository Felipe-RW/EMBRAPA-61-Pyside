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
 
botao_relatorio_tipos_de_acoes = QPushButton("Relatório de Tipos de Ações", janela)
botao_relatorio_tipos_de_acoes.setGeometry(54, 150, 303, 40)
botao_relatorio_tipos_de_acoes.setStyleSheet("""
    QPushButton {
        color: black;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #DFDFDF;    
        border-radius: 20px;                 
    }
""")

botao_relatorio_empregados = QPushButton("Relatório de Empregados", janela)
botao_relatorio_empregados.setGeometry(375, 150, 303, 40)
botao_relatorio_empregados.setStyleSheet("""
    QPushButton {
        color: black;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #DFDFDF;    
        border-radius: 20px;                
    }
""")

botao_relatorio_anos = QPushButton("Relatório de Anos", janela)
botao_relatorio_anos.setGeometry(696, 150, 303, 40)
botao_relatorio_anos.setStyleSheet("""
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

anos = QLabel("Anos", opcoes_relatorio)
anos.setGeometry(61, 28, 200, 30)
anos.setStyleSheet("""
    QLabel {
    color: black;
    font-size: 20px;
    font-family: verdana;
    font-weight: bold 
}
""")

botao_selecionar_anos = QPushButton("Selecionar Anos", opcoes_relatorio)
botao_selecionar_anos.setGeometry(61, 74, 192, 30)
botao_selecionar_anos.setStyleSheet("""
    QPushButton {
    color: white;
    font-size: 13;
    font-family: verdana;
    font-weight: bold;
    background-color: #356394;
    border-radius: 15px                          
}
""")

botao_todos_os_anos = QPushButton("Todos os Anos", opcoes_relatorio)
botao_todos_os_anos.setGeometry(275, 74, 192, 30)
botao_todos_os_anos.setStyleSheet("""
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
    font-weight: lighter
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

selecionar_dados = QCheckBox("Status", opcoes_relatorio)
selecionar_dados.setGeometry(624, 74, 400, 20)
selecionar_dados.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_dados2 = QCheckBox("Número de Ações Enviadas", opcoes_relatorio)
selecionar_dados2.setGeometry(624, 104, 400, 20)
selecionar_dados2.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_dados3 = QCheckBox("Número de Ações Avaliadas", opcoes_relatorio)
selecionar_dados3.setGeometry(624, 134, 400, 20)
selecionar_dados3.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_dados4 = QCheckBox("Tipos de Ações", opcoes_relatorio)
selecionar_dados4.setGeometry(624, 164, 400, 20)
selecionar_dados4.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

janela.show()
 
sys.exit(app.exec())