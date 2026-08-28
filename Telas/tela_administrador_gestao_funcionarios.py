import sys
from PySide6.QtWidgets import (
  QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
  QPushButton,QTableWidget, QHeaderView, QTableWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

app = QApplication(sys.argv)

janela = QWidget()
janela.setObjectName("janela_funcionarios")
janela.setWindowTitle("Gestão de Empregados")
janela.resize(1920, 1080)
janela.setStyleSheet("background-color: #ffffffffff;")

layout_principal = QVBoxLayout(janela)
layout_principal.setContentsMargins(30, 30, 30, 30)
layout_principal.setSpacing(30)

titulo = QLabel("Gestão de Empregados")
titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
titulo.setAlignment(Qt.AlignCenter)
layout_principal.addWidget(titulo)

layout_acoes = QHBoxLayout()

btn_cadastrar = QPushButton("Cadastrar Empregado")
btn_cadastrar.setStyleSheet("""
    QPushButton {
        background-color: #1e7e34;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 8px 16px;
    }
    QPushButton:hover {
        background-color: #155724;
    }
""")
btn_baixar = QPushButton("Baixar em Excel")
btn_baixar.setStyleSheet("""
    QPushButton {
      background-color: #fffffff;
      color: blue;
      font-weight: bold;
      border-radius: 6px;
      padding: 8px 16px;
      border: 1px solid #d0d0d0;
    }
    QPushButton:hover {
        background-color: #d0d0d0;
    }                        
""")

campo_busca = QLineEdit()
campo_busca.setPlaceholderText("Pesquise...")
campo_busca.setStyleSheet("""
    QLineEdit {
        border: 1px solid #cccccc;
        border-radius: 4px;
        padding: 6px;
        width: 200px;
    }
""")

layout_acoes.addWidget(btn_cadastrar)
layout_acoes.addWidget(btn_baixar)
layout_acoes.addStretch()
layout_acoes.addWidget(campo_busca)

layout_principal.addLayout(layout_acoes)

dados_funcionarios = [
  ("Fulano da Silva","silva@gmail.com","Pesquisador","Ativo"," "),
  ("Fulano Ferreira", "ferreira@gmail.com", "Pesquisador", "Ativo"," "),
  ("Fulano Araujo", "araujo@gmail.com", "Validador SIPT", "Desativado"," "),
  ("Fulano Oliveira", "oliveira@gmail.com", "Validador SPAT", "Ativo"," "),
  ("Fulano Leite", "leite@gmail.com", "Validador NCO", "Ativo"," "),
  ("Fulano Da Guia", "guia@gmail.com", "Comitê", "Ativo"," "),
  ("Fulano Jacobina", "jacobina@gmail.com", "Comitê", "Desativado"," "),
  ("Fulano Nogueira", "nogueira@gmail.com", "Administrador", "Ativo"," "),
]

tabela = QTableWidget(len(dados_funcionarios),4)
tabela.setHorizontalHeaderLabels(["Nome","Email","Àrea de Atuação","Status"," "])
tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
tabela.verticalHeader().setVisible(False)
tabela.setStyleSheet("""
    QTableWidget {
        background-color: #ffffff;
        gridline-color: #e0e0e0;
        border: 1px solid #d0d0d0;
        border-radius: 8px;
    }
    QHeaderView::section {
        background-color: #366896;
        color: white;
        font-weight: bold;
        padding: 10px;
        border: none;
        border-radius: 15px 0px;
    }
""")

for linha_id, (nome, email, area, status,botao) in enumerate(dados_funcionarios):
  item_nome = QTableWidgetItem(nome)
  item_email = QTableWidgetItem(email)
  item_area = QTableWidgetItem(area)
  item_status = QTableWidgetItem(status)
  item_botao = QTableWidgetItem(botao)

  item_email.setTextAlignment(Qt.AlignCenter)
  item_area.setTextAlignment(Qt.AlignCenter)
  item_status.setTextAlignment(Qt.AlignCenter)
  item_botao.setTextAlignment(Qt.AlignCenter)

  if status == "Ativo":
    item_status.setForeground(QColor("green"))
  else:
    item_status.setForeground(QColor("orange"))

  tabela.setItem(linha_id, 0, item_nome)
  tabela.setItem(linha_id, 1, item_email)
  tabela.setItem(linha_id, 2, item_area)
  tabela.setItem(linha_id, 3, item_status)
  tabela.setItem(linha_id, 4, item_botao)

layout_principal.addWidget(tabela)


janela.show()
sys.exit(app.exec())