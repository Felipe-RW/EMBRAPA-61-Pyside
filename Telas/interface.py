

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from estilos import ESTILO_GERAL


class JanelaPopupRelatorio(QDialog):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Relatório")
    self.resize(950, 520)
    self.setStyleSheet(ESTILO_GERAL)

   
    layout_principal = QVBoxLayout(self)
    layout_principal.setContentsMargins(25, 15, 25, 25)

    
    layout_topo = QHBoxLayout()
    layout_topo.addStretch()

    titulo_topo = QLabel("Relatório")
    titulo_topo.setObjectName("TituloRelatorio")
    layout_topo.addWidget(titulo_topo)

    layout_topo.addStretch()

    botao_fechar = QPushButton("✕")
    botao_fechar.setObjectName("BotaoFechar")
    botao_fechar.clicked.connect(self.close)
    layout_topo.addWidget(botao_fechar)

    layout_principal.addLayout(layout_topo)

    
    layout_aba = QHBoxLayout()
    botao_aba = QPushButton("Relatório de Pesquisas")
    botao_aba.setObjectName("BotaoAbaAtivo")
    layout_aba.addWidget(botao_aba)
    layout_aba.addStretch()

    layout_principal.addLayout(layout_aba)

    
    painel_cinza = QFrame()
    painel_cinza.setObjectName("PainelFundo")
    layout_painel = QHBoxLayout(painel_cinza)
    layout_painel.setContentsMargins(30, 30, 30, 30)
    layout_painel.setSpacing(40)

    
    coluna_dados = QVBoxLayout()
    titulo_dados = QLabel("Dados do Relatório")
    titulo_dados.setProperty("class", "TituloColuna")
    coluna_dados.addWidget(titulo_dados)
    coluna_dados.addSpacing(10)

    for texto in [
        "Categoria de Ação",
        "Data de Postagem",
        "Status",
        "Pesquisador",
        "Setor",
    ]:
      coluna_dados.addWidget(QCheckBox(texto))
    coluna_dados.addStretch()
    layout_painel.addLayout(coluna_dados)

    
    linha1 = QFrame()
    linha1.setFrameShape(QFrame.VLine)
    linha1.setStyleSheet("color: #B0B0B0;")
    layout_painel.addWidget(linha1)

   
    coluna_anos = QVBoxLayout()
    titulo_anos = QLabel("Anos")
    titulo_anos.setProperty("class", "TituloColuna")
    coluna_anos.addWidget(titulo_anos)
    coluna_anos.addSpacing(10)

    layout_botoes_anos = QHBoxLayout()
    btn_sel_anos = QPushButton("Selecionar anos")
    btn_sel_anos.setObjectName("BotaoFiltroAtivo")
    btn_todos_anos = QPushButton("Todos os anos")
    btn_todos_anos.setObjectName("BotaoFiltroInativo")
    layout_botoes_anos.addWidget(btn_sel_anos)
    layout_botoes_anos.addWidget(btn_todos_anos)
    layout_botoes_anos.addStretch()
    coluna_anos.addLayout(layout_botoes_anos)
    coluna_anos.addSpacing(10)

    for ano in ["2022", "2023", "2024", "2025", "2026"]:
      coluna_anos.addWidget(QCheckBox(ano))
    coluna_anos.addStretch()
    layout_painel.addLayout(coluna_anos)

    
    linha2 = QFrame()
    linha2.setFrameShape(QFrame.VLine)
    linha2.setStyleSheet("color: #B0B0B0;")
    layout_painel.addWidget(linha2)

    
    coluna_pesquisadores = QVBoxLayout()
    titulo_pesq = QLabel("Pesquisadores")
    titulo_pesq.setProperty("class", "TituloColuna")
    coluna_pesquisadores.addWidget(titulo_pesq)
    coluna_pesquisadores.addSpacing(10)

    layout_botoes_pesq = QHBoxLayout()
    btn_sel_pesq = QPushButton("Selecionar pesquisadores")
    btn_sel_pesq.setObjectName("BotaoFiltroAtivo")
    btn_todos_pesq = QPushButton("Todos os pesquisadores")
    btn_todos_pesq.setObjectName("BotaoFiltroInativo")
    layout_botoes_pesq.addWidget(btn_sel_pesq)
    layout_botoes_pesq.addWidget(btn_todos_pesq)
    layout_botoes_pesq.addStretch()
    coluna_pesquisadores.addLayout(layout_botoes_pesq)
    coluna_pesquisadores.addSpacing(10)

    campo_pesquisa = QLineEdit()
    campo_pesquisa.setObjectName("CampoPesquisa")
    campo_pesquisa.setPlaceholderText("Pesquise...")
    coluna_pesquisadores.addWidget(campo_pesquisa)
    coluna_pesquisadores.addSpacing(5)

    for nome in ["Fulano da Silva", "Ciclano da Silva", "Beltrano da Silva"]:
      coluna_pesquisadores.addWidget(QCheckBox(nome))
    coluna_pesquisadores.addStretch()
    layout_painel.addLayout(coluna_pesquisadores)

    layout_principal.addWidget(painel_cinza)

  
    layout_rodape = QHBoxLayout()
    layout_rodape.addStretch()
    botao_gerar = QPushButton("Gerar Relatório")
    botao_gerar.setObjectName("BotaoGerar")
    layout_rodape.addWidget(botao_gerar)

    layout_principal.addLayout(layout_rodape)