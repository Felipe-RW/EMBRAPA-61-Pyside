import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QColor, QIcon, QPixmap, QPainter, QPen, QBrush
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QAbstractItemView, QStackedWidget, QFrame, QTextEdit, QSizePolicy,
    QScrollArea
)




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

DESCRICAO_LOREM = (
    '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod '
    'tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, '
    'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo '
    'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse '
    'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
    'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'
)


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


def gerar_pesquisas():
    
    datas = ["23/03/2026", "29/04/2026", "22/06/2026", "23/07/2026", "29/08/2026"]
    pesquisas = []
    for i, data in enumerate(datas, start=1):
        pesquisas.append({
            "tipo_acao": f"Pesquisa {i}",
            "tipo": "Artigo Científico",
            "data": data,
            "nome": "Palestra",
            "pesquisador": "Davi de Souza Escalone da Silva Silvestre",
            "data_execucao": data,
            "descricao": DESCRICAO_LOREM,
            "acao": "ARTIGO CIENTIFICO",
            "comprovante_url": "Lorem_ipsum_dolor_sit_amet.com",
            "comprovantes": [
                {"nome": "foto_palestra.jpg", "tamanho": "5.4 mb"} for _ in range(6)
            ],
        })
    return pesquisas



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

        self.tabela = QTableWidget(0, 4)
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
        """)

        self.tabela.setStyleSheet("""
            QTableWidget {
                border: 1px solid #dfe4e8;
                border-radius: 4px;
                gridline-color: transparent;
                background-color: #ffffff;
                color: #1c2b39;
            }
            QTableWidget::item {
                padding: 6px;
                color: #1c2b39;
            }
        """)

        layout.addWidget(self.tabela)

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
            btn_visualizar.clicked.connect(
                lambda checked=False, c=colaborador: self._ir_para_acoes(c)
            )

            wrapper = QWidget()
            h = QHBoxLayout(wrapper)
            h.setContentsMargins(0, 0, 8, 0)
            h.addWidget(btn_visualizar, 0, Qt.AlignRight)
            self.tabela.setCellWidget(linha, 3, wrapper)

            self.tabela.setRowHeight(linha, 42)

    def _filtrar(self, texto):
        texto = texto.strip().lower()
        if not texto:
            filtrados = self._dados
        else:
            filtrados = [d for d in self._dados if texto in d["nome"].lower()]
        self._preencher_tabela(filtrados)



class ComprovanteItem(QFrame):
    """Chip de arquivo comprovante (icone JPG + nome + tamanho + acoes)."""

    def __init__(self, nome, tamanho):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                border: 1px solid #d7dce1;
                border-radius: 4px;
                background-color: #ffffff;
            }
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(8)

        icone = QLabel("📄")
        icone.setStyleSheet("color: #2f6fb0; font-size: 16px;")

        textos = QVBoxLayout()
        textos.setSpacing(0)
        nome_lbl = QLabel(nome)
        nome_lbl.setStyleSheet("font-size: 11px; color: #1c2b39;")
        tam_lbl = QLabel(tamanho)
        tam_lbl.setStyleSheet("font-size: 10px; color: #8a94a0;")
        textos.addWidget(nome_lbl)
        textos.addWidget(tam_lbl)

        btn_del = QPushButton("🗑")
        btn_del.setFlat(True)
        btn_del.setCursor(Qt.PointingHandCursor)
        btn_del.setStyleSheet("border: none; color: #b23b3b;")
        btn_down = QPushButton("⬇")
        btn_down.setFlat(True)
        btn_down.setCursor(Qt.PointingHandCursor)
        btn_down.setStyleSheet("border: none; color: #2f6fb0;")

        layout.addWidget(icone)
        layout.addLayout(textos)
        layout.addWidget(btn_del)
        layout.addWidget(btn_down)


class PesquisaRow(QFrame):
    """Uma linha da tabela de ações, expansível ao clicar na seta."""

    def __init__(self, pesquisa, zebra=False):
        super().__init__()
        self.pesquisa = pesquisa
        self._expandido = False

        self.setStyleSheet(f"""
            PesquisaRow {{
                background-color: {'#E9F2FF' if zebra else '#ffffff'};
                border-bottom: 1px solid #dfe4e8;
            }}
        """)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)


        header = QWidget()
        header.setStyleSheet(f"""
    background-color: {'#e8f1fb' if zebra else '#ffffff'};
""")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(16, 10, 16, 10)

        lbl_tipo_acao = QLabel(pesquisa["tipo_acao"])
        lbl_tipo_acao.setAlignment(Qt.AlignCenter)
        lbl_tipo = QLabel(pesquisa["tipo"])
        lbl_tipo.setAlignment(Qt.AlignCenter)
        lbl_data = QLabel(pesquisa["data"])
        lbl_data.setAlignment(Qt.AlignCenter)


        for lbl in (lbl_tipo_acao, lbl_tipo, lbl_data):
            lbl.setStyleSheet("color: #1c2b39; font-size: 13px;")
            lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.btn_seta = QPushButton("▾")
        self.btn_seta.setFlat(True)
        self.btn_seta.setCursor(Qt.PointingHandCursor)
        self.btn_seta.setFixedWidth(30)
        self.btn_seta.setStyleSheet("border: none; font-size: 14px; color: #1c2b39;")
        self.btn_seta.clicked.connect(self._toggle)

        header_layout.addWidget(lbl_tipo_acao)
        header_layout.addWidget(lbl_tipo)
        header_layout.addWidget(lbl_data)
        header_layout.addWidget(self.btn_seta, 0, Qt.AlignRight)

        outer.addWidget(header)

        self.painel_detalhe = self._build_detalhe(pesquisa)
        self.painel_detalhe.setVisible(False)
        outer.addWidget(self.painel_detalhe)

    def _toggle(self):
        self._expandido = not self._expandido
        self.painel_detalhe.setVisible(self._expandido)
        self.btn_seta.setText("▴" if self._expandido else "▾")

    def _campo(self, titulo, widget):
        box = QVBoxLayout()
        box.setSpacing(4)
        lbl = QLabel(titulo)
        lbl.setStyleSheet("font-weight: bold; color: #1c2b39; font-size: 12px;")
        box.addWidget(lbl)
        box.addWidget(widget)
        return box

    def _build_detalhe(self, p):
        painel = QFrame()
        painel.setStyleSheet("""
            QFrame { background-color: #ffffff; border-top: 1px solid #dfe4e8; }
            QLineEdit, QTextEdit {
                border: 1px solid #c9d2da;
                border-radius: 4px;
                padding: 6px 8px;
                color: #2c3a48;
                background-color: #ffffff;
            }
        """)
        layout = QVBoxLayout(painel)
        layout.setContentsMargins(20, 16, 20, 20)
        layout.setSpacing(14)

        linha1 = QHBoxLayout()
        linha1.setSpacing(20)

        ed_nome = QLineEdit(p["nome"])
        ed_nome.setReadOnly(True)
        ed_pesquisador = QLineEdit(p["pesquisador"])
        ed_pesquisador.setReadOnly(True)
        ed_data = QLineEdit(p["data_execucao"])
        ed_data.setReadOnly(True)
        ed_data.setFixedWidth(120)

        linha1.addLayout(self._campo("Nome:", ed_nome), 2)
        linha1.addLayout(self._campo("Pesquisador:", ed_pesquisador), 3)
        linha1.addLayout(self._campo("Data de Execução:", ed_data), 1)
        layout.addLayout(linha1)

        
        txt_desc = QTextEdit(p["descricao"])
        txt_desc.setReadOnly(True)
        txt_desc.setFixedHeight(80)
        layout.addLayout(self._campo("Descrição:", txt_desc))

    
        ed_acao = QLineEdit(p["acao"])
        ed_acao.setReadOnly(True)
        layout.addLayout(self._campo("Ação:", ed_acao))

     
        ed_url = QLineEdit(p["comprovante_url"])
        ed_url.setReadOnly(True)
        layout.addLayout(self._campo("Comprovante URL:", ed_url))

        lbl_comp = QLabel("Comprovantes:")
        lbl_comp.setStyleSheet("font-weight: bold; color: #1c2b39; font-size: 12px;")
        layout.addWidget(lbl_comp)

        comp_container = QFrame()
        comp_container.setStyleSheet("""
            QFrame { border: 1px solid #dfe4e8; border-radius: 4px; }
        """)
        comp_layout = QHBoxLayout(comp_container)
        comp_layout.setContentsMargins(10, 10, 10, 10)
        comp_layout.setSpacing(10)

  
        comp_v = QVBoxLayout()
        comp_v.setSpacing(8)
        chips = [ComprovanteItem(c["nome"], c["tamanho"]) for c in p["comprovantes"]]
        for i in range(0, len(chips), 5):
            linha = QHBoxLayout()
            linha.setSpacing(8)
            for chip in chips[i:i + 5]:
                linha.addWidget(chip)
            linha.addStretch()
            comp_v.addLayout(linha)

        comp_layout.addLayout(comp_v)
        layout.addWidget(comp_container)

        return painel



class AcoesColaboradorScreen(QWidget):
    def __init__(self, voltar_callback):
        super().__init__()
        self._voltar = voltar_callback
        self._pesquisas = []
        self._linhas = []
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 20, 24, 24)
        layout.setSpacing(16)

        topo_nav = QHBoxLayout()
        btn_voltar = QPushButton("←  Voltar")
        btn_voltar.setCursor(Qt.PointingHandCursor)
        btn_voltar.setFlat(True)
        btn_voltar.setStyleSheet("border: none; color: #2f6fb0; font-weight: bold;")
        btn_voltar.clicked.connect(self._voltar)
        topo_nav.addWidget(btn_voltar, 0, Qt.AlignLeft)
        topo_nav.addStretch()
        layout.addLayout(topo_nav)

        titulo = QLabel("Lista de colaboradores")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 22px; font-weight: bold; color: #1c2b39;")
        layout.addWidget(titulo)

        linha_nome_busca = QHBoxLayout()
        self.lbl_nome = QLabel()
        self.lbl_nome.setStyleSheet("font-size: 15px; font-weight: bold; color: #1c2b39;")

        self.campo_busca = CampoBusca(placeholder="Ação", largura=280)
        self.campo_busca.textChanged.connect(self._filtrar)

        linha_nome_busca.addWidget(self.lbl_nome, 0, Qt.AlignLeft)
        linha_nome_busca.addStretch()
        linha_nome_busca.addWidget(self.campo_busca, 0, Qt.AlignRight)
        layout.addLayout(linha_nome_busca)

        header = QFrame()
        header.setStyleSheet("background-color: #2f5b7c; border-radius: 4px;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(16, 10, 16, 10)
        for texto in ("Tipo da Ação", "Tipo", "Data"):
            lbl = QLabel(texto)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color: white; font-weight: bold; font-size: 13px;")
            lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            header_layout.addWidget(lbl)
        espaco_seta = QLabel("")
        espaco_seta.setFixedWidth(30)
        header_layout.addWidget(espaco_seta)
        layout.addWidget(header)

       
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea { border: 1px solid #dfe4e8; border-top: none; border-radius: 0 0 4px 4px; }
        """)
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)
        self.container_layout.addStretch()
        scroll.setWidget(self.container)
        layout.addWidget(scroll)

    def carregar(self, colaborador):
        self.lbl_nome.setText(colaborador["nome"])
        self._pesquisas = gerar_pesquisas()
        self._popular(self._pesquisas)

    def _popular(self, pesquisas):
       
        for linha in self._linhas:
            linha.setParent(None)
        self._linhas = []

        while self.container_layout.count():
            item = self.container_layout.takeAt(0)
            w = item.widget()
            if w:
                w.setParent(None)

        for i, pesquisa in enumerate(pesquisas):
            row = PesquisaRow(pesquisa, zebra=(i % 2 == 0))
            self.container_layout.addWidget(row)
            self._linhas.append(row)
        self.container_layout.addStretch()

    def _filtrar(self, texto):
        texto = texto.strip().lower()
        if not texto:
            filtrados = self._pesquisas
        else:
            filtrados = [
                p for p in self._pesquisas
                if texto in p["tipo_acao"].lower() or texto in p["tipo"].lower()
            ]
        self._popular(filtrados)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de colaboradores")
        self.resize(1000, 680)
        self.setStyleSheet("background-color: #ffffff;")

        self.stack = QStackedWidget(self)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addWidget(self.stack)

        self.tela_lista = ListaColaboradoresScreen(self.ir_para_acoes)
        self.tela_acoes = AcoesColaboradorScreen(self.voltar_para_lista)

        self.stack.addWidget(self.tela_lista)
        self.stack.addWidget(self.tela_acoes)
        self.stack.setCurrentWidget(self.tela_lista)

    def ir_para_acoes(self, colaborador):
        self.tela_acoes.carregar(colaborador)
        self.stack.setCurrentWidget(self.tela_acoes)

    def voltar_para_lista(self):
        self.stack.setCurrentWidget(self.tela_lista)


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
