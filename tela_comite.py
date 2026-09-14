
import os
import sys

from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QFont, QColor, QIcon, QPixmap, QPainter, QPen, QBrush, QPainterPath, QRegion
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QAbstractItemView, QStackedWidget, QFrame, QButtonGroup,
    QScrollArea, QSizePolicy
)


BASE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-logo.png")


class btn_layout(QPushButton):
    """Botão da sidebar com ícone + texto lado a lado (igual ao seu original)."""

    def __init__(self, path, texto, parent=None):
        super().__init__(parent)

        self.setStyleSheet("""
            QPushButton {
                height: 50px;
                padding: 10px;
                border: none;
                background-color: transparent;
                border-top-left-radius: 20px;
                border-bottom-left-radius: 20px;
            }
            QPushButton:hover {
                background-color: #4A7AB0;
            }
            QPushButton:checked {
                background-color: #2A4E70;
            }
            QLabel {
                background-color: transparent;
                text-align: center;
                font-family: Verdana;
                font-weight: bold;
                color: white;
                font-size: 20px;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 0, 10, 0)

        self.icone_label = QLabel()
        self.icone_label.setPixmap(QIcon(path).pixmap(QSize(23, 25)))

        self.texto_label = QLabel(texto)
        self.texto_label.setAlignment(Qt.AlignCenter)

        self.icone_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.texto_label.setAttribute(Qt.WA_TransparentForMouseEvents)

        layout.addWidget(self.icone_label)
        layout.addStretch()
        layout.addWidget(self.texto_label)
        layout.addStretch()

    def setText(self, texto):
        super().setText(texto)
        self.texto_label.setText(texto)

    def setIcon(self, icone_path, size=QSize(23, 25)):
        self.icone_label.setPixmap(QIcon(icone_path).pixmap(size))




COLABORADORES = [
    {"nome": "Fulano Da Silva", "acoes": 70, "aprovadas": 25},
    {"nome": "Fulano Ferreira", "acoes": 95, "aprovadas": 50},
    {"nome": "Fulano Araujo", "acoes": 97, "aprovadas": 50},
    {"nome": "Fulano Oliveira", "acoes": 45, "aprovadas": 2},
    {"nome": "Fulano Leite", "acoes": 32, "aprovadas": 25},
    {"nome": "Fulano Da Guia", "acoes": 81, "aprovadas": 60},
    {"nome": "Fulano Jacobina", "acoes": 50, "aprovadas": 30},
    {"nome": "Fulano Nogueira", "acoes": 34, "aprovadas": 16},
    {"nome": "Fulano Medina", "acoes": 77, "aprovadas": 20},
    {"nome": "Fulano Ortiz", "acoes": 98, "aprovadas": 56},
    {"nome": "Fulano Braun", "acoes": 104, "aprovadas": 50},
    {"nome": "Fulano Maruan", "acoes": 46, "aprovadas": 21},
    {"nome": "Fulano Millan", "acoes": 105, "aprovadas": 39},
]


def criar_icone_excel():
    tamanho = 20
    pixmap = QPixmap(tamanho, tamanho)
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)

    painter.setBrush(QBrush(QColor("#1e7e34")))
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(0, 0, tamanho, tamanho, 3, 3)

    painter.setPen(QPen(QColor("#ffffff"), 1))
    y = 6
    while y < tamanho - 3:
        painter.drawLine(3, y, tamanho - 3, y)
        y += 3

    fonte = QFont()
    fonte.setBold(True)
    fonte.setPixelSize(11)
    painter.setFont(fonte)
    painter.setPen(QColor("#ffffff"))
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "X")

    painter.end()
    return QIcon(pixmap)


class CampoBusca(QFrame):
    def __init__(self, placeholder="", largura=280):
        super().__init__()
        self.setFixedWidth(largura)
        self.setStyleSheet("""
            CampoBusca {
                background-color: #ffffff;
                border: 1px solid #c9d2da;
                border-radius: 6px;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 4, 10, 4)
        layout.setSpacing(6)

        self.linha = QLineEdit()
        self.linha.setPlaceholderText(placeholder)
        self.linha.setFrame(False)
        font_italico = QFont()
        font_italico.setItalic(True)
        self.linha.setFont(font_italico)
        self.linha.setStyleSheet("""
            QLineEdit {
                border: none;
                background: transparent;
                color: #3a3a3a;
                padding: 4px 0;
            }
        """)

        lbl_icone = QLabel("🔍")
        lbl_icone.setStyleSheet("color: #9aa4ae; font-size: 13px; border: none;")

        layout.addWidget(self.linha)
        layout.addWidget(lbl_icone)

    @property
    def textChanged(self):
        return self.linha.textChanged



class TabelaArredondada(QTableWidget):
    """QTableWidget comum, mas com uma MÁSCARA de recorte aplicada nos
    4 cantos. O 'border-radius' do CSS às vezes não é respeitado igual
    em todos os temas do Windows (principalmente quando as células têm
    fundo colorido pintado por cima, como nas linhas zebradas) — a
    máscara resolve isso de vez, recortando o widget de verdade em vez
    de só pedir educadamente pro estilo arredondar."""

    RAIO = 19

    def resizeEvent(self, event):
        super().resizeEvent(event)
        caminho = QPainterPath()
        caminho.addRoundedRect(0, 0, self.width(), self.height(), self.RAIO, self.RAIO)
        self.setMask(QRegion(caminho.toFillPolygon().toPolygon()))



class ListaColaboradoresScreen(QWidget):
    def __init__(self, ir_para_acoes_callback):
        super().__init__()
        self._ir_para_acoes = ir_para_acoes_callback
        self._dados = COLABORADORES
        self._build_ui()
        self._preencher_tabela(self._dados)

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 20, 24, 24)
        layout.setSpacing(16)

        topo = QHBoxLayout()

        btn_excel = QPushButton("  Baixar em Excel")
        btn_excel.setIcon(criar_icone_excel())
        btn_excel.setIconSize(QSize(20, 20))
        btn_excel.setCursor(Qt.PointingHandCursor)
        btn_excel.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #1a5fb4;
                border: 1px solid #c9d2da;
                border-radius: 6px;
                padding: 8px 14px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #f4f7fa; }
        """)
        btn_excel.clicked.connect(lambda: print("Exportar em Excel - a implementar"))

        titulo = QLabel("Lista de colaboradores")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 22px; font-weight: bold; color: #1c2b39;")

        self.campo_busca = CampoBusca(placeholder="Fulano", largura=240)
        self.campo_busca.textChanged.connect(self._filtrar)

        topo.addWidget(btn_excel, 0, Qt.AlignLeft)
        topo.addStretch()
        topo.addWidget(self.campo_busca, 0, Qt.AlignRight)

        layout.addWidget(titulo)
        layout.addLayout(topo)

        self.tabela = TabelaArredondada(0, 4)
        self.tabela.setHorizontalHeaderLabels(
            ["Empregados", "Quantidade de ações", "Aprovadas", ""]
        )
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.setShowGrid(False)
        self.tabela.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setFocusPolicy(Qt.NoFocus)
        self.tabela.verticalHeader().setDefaultSectionSize(42)

        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        self.tabela.setColumnWidth(3, 120)
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3f6f9c, stop:1 #2f5b7c
                );
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
            }
            QHeaderView::section:first {
                border-top-left-radius: 19px;
            }
            QHeaderView::section:last {
                border-top-right-radius: 19px;
            }
        """)


        self.tabela.setStyleSheet("""
            QTableWidget {
                border: 1px solid #dfe4e8;
                border-radius: 20px;
                gridline-color: transparent;
                background-color: #ffffff;
                color: #1c2b39;
            }
            QTableWidget::item {
                padding: 6px;
                color: #1c2b39;
            }
        """)

       
        self.tabela.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabela.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabela.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        area_rolavel = QScrollArea()
        area_rolavel.setWidgetResizable(True)
        area_rolavel.setFrameShape(QFrame.NoFrame)
        area_rolavel.setStyleSheet("background: transparent;")
        area_rolavel.setWidget(self.tabela)

  
        LARGURA_TABELA = 1400
        area_rolavel.setFixedWidth(LARGURA_TABELA)

        linha_tabela = QHBoxLayout()
        linha_tabela.addStretch()
        linha_tabela.addWidget(area_rolavel)
        linha_tabela.addStretch()
        layout.addLayout(linha_tabela)

    def _preencher_tabela(self, dados):
        self.tabela.setRowCount(0)
        cor_texto = QColor("#1c2b39")

        for linha, colaborador in enumerate(dados):
            self.tabela.insertRow(linha)
            cor_fundo = QColor("#e8f1fb") if linha % 2 == 0 else QColor("#ffffff")

            item_nome = QTableWidgetItem(colaborador["nome"])
            item_nome.setTextAlignment(Qt.AlignCenter)

            item_qtd = QTableWidgetItem(str(colaborador["acoes"]))
            item_qtd.setTextAlignment(Qt.AlignCenter)

            item_aprov = QTableWidgetItem(str(colaborador["aprovadas"]))
            item_aprov.setTextAlignment(Qt.AlignCenter)

            for item in (item_nome, item_qtd, item_aprov):
                item.setForeground(cor_texto)
                item.setBackground(cor_fundo)

            self.tabela.setItem(linha, 0, item_nome)
            self.tabela.setItem(linha, 1, item_qtd)
            self.tabela.setItem(linha, 2, item_aprov)

            btn_visualizar = QPushButton("Visualizar")
            btn_visualizar.setCursor(Qt.PointingHandCursor)
            btn_visualizar.setMinimumWidth(90)
            btn_visualizar.setStyleSheet("""
                QPushButton {
                    background-color: qlineargradient(
                        x1:0, y1:0, x2:0, y2:1,
                        stop:0 #3d7fc4, stop:1 #2c5fa0
                    );
                    color: white;
                    border: none;
                    border-radius: 14px;
                    padding: 6px 16px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: qlineargradient(
                        x1:0, y1:0, x2:0, y2:1,
                        stop:0 #3672b3, stop:1 #254f89
                    );
                }
            """)
       
            item_botao = QTableWidgetItem()
            item_botao.setBackground(cor_fundo)
            self.tabela.setItem(linha, 3, item_botao)

      
            wrapper = QWidget()
            wrapper.setAttribute(Qt.WA_TranslucentBackground)

            h = QHBoxLayout(wrapper)
            h.setContentsMargins(0, 0, 8, 0)
            h.setSpacing(0)
            h.addWidget(btn_visualizar, 0, Qt.AlignRight | Qt.AlignVCenter)

            self.tabela.setCellWidget(linha, 3, wrapper)

        altura_cabecalho = self.tabela.horizontalHeader().height()
        altura_linhas = sum(self.tabela.rowHeight(i) for i in range(self.tabela.rowCount()))
        self.tabela.setFixedHeight(altura_cabecalho + altura_linhas + 4)

    def _filtrar(self, texto):
        texto = texto.strip().lower()
        if not texto:
            filtrados = self._dados
        else:
            filtrados = [d for d in self._dados if texto in d["nome"].lower()]
        self._preencher_tabela(filtrados)




class TelaComite(QWidget):
    """Era ModeloTelaComite(QMainWindow) com setFixedSize(1920, 1080)
    e tudo posicionado por setGeometry(). Agora é QWidget, sem tamanho
    fixo, com layouts — para se encaixar dentro da janela do sistema.
    """

    sair_solicitado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #356394; font-family: 'Verdana';")

        layout_raiz = QHBoxLayout(self)
   
        layout_raiz.setContentsMargins(16, 0, 16, 0)
        layout_raiz.setSpacing(0)


        menu_lateral = QWidget()
        menu_lateral.setFixedWidth(280)
        menu_lateral.setStyleSheet("background-color: #356394;")
        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 10, 0)
        menu_lateral_layout.setSpacing(0)

        logo_label = QLabel()
        logo = QPixmap(LOGO)
        if not logo.isNull():
            logo_certa = logo.scaled(220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(logo_certa)
        logo_label.setAlignment(Qt.AlignLeft)
        menu_lateral_layout.addWidget(logo_label)

        self.btn_home = btn_layout(os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_empregados = btn_layout(os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Pesquisadores")
        self.btn_home.setCheckable(True)
        self.btn_empregados.setCheckable(True)

        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.addWidget(self.btn_empregados)

        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_empregados)

        menu_lateral_layout.addStretch()
        layout_raiz.addWidget(menu_lateral)

        area_direita = QVBoxLayout()
        area_direita.setContentsMargins(0, 0, 0, 0)
        area_direita.setSpacing(0)

        cabecalho = QWidget()
        cabecalho.setFixedHeight(70)
        cabecalho.setStyleSheet("background-color: #356394;")
        cabecalho_layout = QHBoxLayout(cabecalho)
        cabecalho_layout.setContentsMargins(35, 0, 35, 0)

        self.nome_empregado = QLabel("Fulano da Silva Rodrigues")
        self.nome_empregado.setStyleSheet("font-size: 24px; color: #ffffff; font-weight: bold;")
        separador = QLabel("|")
        separador.setStyleSheet("font-size: 24px; color: #ffffff;")
        funcao_empregado = QLabel("Comitê")
        funcao_empregado.setStyleSheet("color: #ffffff; font-size: 24px; font-weight: bold;")

        cabecalho_layout.addWidget(self.nome_empregado)
        cabecalho_layout.addSpacing(12)
        cabecalho_layout.addWidget(separador)
        cabecalho_layout.addSpacing(12)
        cabecalho_layout.addWidget(funcao_empregado)
        cabecalho_layout.addStretch()

        self.nome_tela = QLabel("Pesquisadores")
        self.nome_tela.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: normal;")
        cabecalho_layout.addWidget(self.nome_tela)
        cabecalho_layout.addStretch()

        botao_logout = QPushButton("Logout")
        botao_logout.setFixedSize(150, 40)
        botao_logout.setCursor(Qt.PointingHandCursor)
        botao_logout.setStyleSheet("""
            QPushButton {
                background-color: #ffffff; color: #08175C; font-size: 18px;
                border: 0px solid #ffffff; border-radius: 10px; font-weight: bold;
            }
            QPushButton:hover { background-color: #EDEDED; }
        """)
        botao_logout.clicked.connect(self.sair_solicitado.emit)
        cabecalho_layout.addWidget(botao_logout)

        area_direita.addWidget(cabecalho)

        paginaprincipal = QFrame()
        paginaprincipal.setStyleSheet("""
            QFrame { background-color: #ffffff; border-top-left-radius: 20px; border-top-right-radius: 20px; }
        """)
        pagina_layout = QVBoxLayout(paginaprincipal)
        pagina_layout.setContentsMargins(0, 0, 0, 0)

     
        self.stack_paginas = QStackedWidget()
        self.pagina_painel = self._montar_painel_principal_placeholder()
        self.pagina_pesquisadores = ListaColaboradoresScreen(lambda colaborador: None)

        self.stack_paginas.addWidget(self.pagina_painel)
        self.stack_paginas.addWidget(self.pagina_pesquisadores)
        self.stack_paginas.setCurrentWidget(self.pagina_pesquisadores)

        pagina_layout.addWidget(self.stack_paginas)
        area_direita.addWidget(paginaprincipal)

        layout_raiz.addLayout(area_direita)

        self.btn_home.clicked.connect(lambda: self._trocar_pagina(self.pagina_painel, "Painel Principal"))
        self.btn_empregados.clicked.connect(lambda: self._trocar_pagina(self.pagina_pesquisadores, "Pesquisadores"))
        self.btn_empregados.setChecked(True)

    def _montar_painel_principal_placeholder(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)
        aviso = QLabel("Painel Principal\n(ainda não implementado)")
        aviso.setAlignment(Qt.AlignCenter)
        aviso.setStyleSheet("color: #6B7280; font-weight: normal;")
        layout.addWidget(aviso)
        return widget

    def _trocar_pagina(self, pagina, nome):
        self.stack_paginas.setCurrentWidget(pagina)
        self.nome_tela.setText(nome)

    def definir_usuario(self, nome: str, email: str):
        """Chamado pelo principal.py antes de mostrar esta tela."""
        self.nome_empregado.setText(nome)


def main():
    """Roda só a tela do Comitê sozinha, para teste isolado."""
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    janela = TelaComite()
    janela.setWindowTitle("Comitê")
    janela.resize(1100, 700)
    janela.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
