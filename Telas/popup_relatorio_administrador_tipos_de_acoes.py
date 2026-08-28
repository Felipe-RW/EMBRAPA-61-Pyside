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
        color: white;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #356394;    
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
        color: black;
        font-size: 16px;
        font-family: verdana;
        font-weight: bold;
        background-color: #DFDFDF;    
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

acoes = QLabel("Ações", opcoes_relatorio)
acoes.setGeometry(61, 28, 67, 30)
acoes.setStyleSheet("""
    QLabel {
    color: black;
    font-size: 20px;
    font-family: verdana;
    font-weight: bold 
}
""")

botao_selecionar_acoes = QPushButton("Selecionar Ações", opcoes_relatorio)
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

botao_todas_as_acoes = QPushButton("Todas as Ações", opcoes_relatorio)
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

selecionar_acao1 = QCheckBox("Coordenação de evento REGIONAL", opcoes_relatorio)
selecionar_acao1.setGeometry(61, 170, 400, 20)
selecionar_acao1.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter;
}
""")

selecionar_acao2 = QCheckBox("Artigos de Divulgação na mídia", opcoes_relatorio)
selecionar_acao2.setGeometry(61, 200, 400, 20)
selecionar_acao2.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_acao3 = QCheckBox("Produção de Vídeos Técnicos", opcoes_relatorio)
selecionar_acao3.setGeometry(61, 230, 400, 20)
selecionar_acao3.setStyleSheet("""
    QCheckBox {
    color: black;
    font-size: 16px;
    font-family: verdana;
    font-weight: lighter
}
""")

selecionar_acao4 = QCheckBox("Elaboração do Plano em Marketing", opcoes_relatorio)
selecionar_acao4.setGeometry(61, 260, 400, 20)
selecionar_acao4.setStyleSheet("""
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