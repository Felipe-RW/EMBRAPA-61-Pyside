import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")


class DragDropUploadArea(QFrame):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setCursor(Qt.PointingHandCursor)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #f2f3f5;
                border: 2px dashed #999999;
                border-radius: 8px;
                padding: 15px;
                font-family: 'Verdana';
                font-weight: bold;
            }
            QFrame:hover {
                background-color: #e8ecef;
                border-color: #666666;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        icon_label = QLabel("↑")
        icon_label.setStyleSheet("""
            QLabel {
                font-family: 'Verdana';
                font-size: 18px;
                font-weight: bold;
                border: 2px solid #000;
                border-radius: 6px;
                padding: 2px 8px;
                background-color: white;
            }
        """)

        text_label = QLabel("Arraste seus comprovantes aqui ou clique para selecionar (PDF, DOCX, PNG, JPG)")
        text_label.setStyleSheet("""
            QLabel {
                font-family: 'Verdana';
                font-weight: bold;
                font-size: 13px;
                color: #333333;
                border: none;
            }
        """)

        layout.addWidget(icon_label)
        layout.addSpacing(10)
        layout.addWidget(text_label)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            files, _ = QFileDialog.getOpenFileNames(
                self, "Selecionar Comprovantes", "", "Arquivos (*.pdf *.docx *.png *.jpg *.jpeg)"
            )


class CriarAcaoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QWidget {
                font-family: 'Verdana';
                font-weight: bold;
                background-color: transparent;
            }
        """)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(15)

        # 1. TÍTULO
        title_label = QLabel("Criar ação")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-family: 'Verdana';
                font-size: 28px;
                font-weight: bold;
                color: #000000;
                border: none;
                margin-top: 10px;
            }
        """)
        main_layout.addWidget(title_label)

        # 2. CARD PRINCIPAL
        card = QFrame()
        card.setFixedSize(1485, 817)
        card.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 1px solid #dcdcdc;
                border-radius: 16px;
                font-family: 'Verdana';
                font-weight: bold;
            }
        """)
        
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 30, 40, 30)
        card_layout.setSpacing(15)

        input_style = """
            QLineEdit, QTextEdit, QComboBox {
                font-family: 'Verdana';
                font-weight: bold;
                border: 1px solid #777777;
                border-radius: 8px;
                padding: 8px 12px;
                background-color: #ffffff;
                font-size: 14px;
                color: #333333;
            }
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
                border: 2px solid #000000;
            }
        """

        label_style = "font-family: 'Verdana'; font-weight: bold; font-size: 15px; border: none; color: #000000;"

        # Título da ação e Data de realização
        top_row = QHBoxLayout()

        nome_box = QVBoxLayout()
        nome_label = QLabel("Título da ação:")
        nome_label.setStyleSheet(label_style)
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Digite o título da ação aqui...")
        self.nome_input.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.nome_input.setStyleSheet(input_style)
        nome_box.addWidget(nome_label)
        nome_box.addWidget(self.nome_input)

        data_box = QVBoxLayout()
        data_label = QLabel("Data de realização:")
        data_label.setStyleSheet(label_style)
        
        self.data_input = QLineEdit()
        self.data_input.setInputMask("99/99/9999;_")
        self.data_input.setAlignment(Qt.AlignCenter)
        self.data_input.setFixedWidth(200)
        self.data_input.setStyleSheet(input_style)
        
        data_box.addWidget(data_label)
        data_box.addWidget(self.data_input)

        top_row.addLayout(nome_box, stretch=4)
        top_row.addSpacing(30)
        top_row.addLayout(data_box, stretch=1)
        card_layout.addLayout(top_row)

        # Descrição
        desc_label = QLabel("Descrição:")
        desc_label.setStyleSheet(label_style)
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Digite a descrição da ação aqui...")
        self.desc_input.setStyleSheet(input_style)
        self.desc_input.setFixedHeight(120)
        card_layout.addWidget(desc_label)
        card_layout.addWidget(self.desc_input)

        # Categoria da Ação
        acao_label = QLabel("Categoria da ação:")
        acao_label.setStyleSheet(label_style)
        
        self.acao_combo = QComboBox()
        
        list_view = QListView(self.acao_combo)
        list_view.setStyleSheet("""
            QListView {
                font-family: 'Verdana';
                font-weight: bold;
                font-size: 14px;
                color: #333333;
                background-color: #ffffff;
                border: 1px solid #777777;
                outline: none;
            }
            QListView::item {
                min-height: 38px;
            }
            QListView::item:hover {
                background-color: #e8ecef;
                color: #000000;
            }
            QListView::item:selected {
                background-color: #d0d5dd;
                color: #000000;
            }
        """)
        self.acao_combo.setView(list_view)

        model = QStandardItemModel()
        opcoes = ["Selecionar categoria", "Palestra", "Entrevista", "Visita Técnica", "Participação em Evento"]
        for opcao in opcoes:
            item = QStandardItem(opcao)
            item.setTextAlignment(Qt.AlignCenter)
            model.appendRow(item)
            
        self.acao_combo.setModel(model)

        self.acao_combo.setStyleSheet(input_style + """
            QComboBox {
                text-align: center;
            }
            QComboBox::drop-down {
                border: none;
                padding-right: 20px;
            }
        """)
        
        card_layout.addWidget(acao_label)
        card_layout.addWidget(self.acao_combo)

        # Área de Upload de Comprovantes (Nota: a URL foi removida)
        upload_label = QLabel("Comprovantes:")
        upload_label.setStyleSheet(label_style)
        self.upload_area = DragDropUploadArea()
        self.upload_area.setFixedHeight(120)
        card_layout.addWidget(upload_label)
        card_layout.addWidget(self.upload_area)

        card_layout.addStretch()

        # Botões inferiores
        bottom_layout = QHBoxLayout()

        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.setCursor(Qt.PointingHandCursor)
        self.btn_cancelar.setFixedSize(180, 44)
        self.btn_cancelar.setStyleSheet("""
            QPushButton {
                font-family: 'Verdana';
                font-weight: bold;
                color: #d90429;
                border: 2px solid #d90429;
                border-radius: 22px;
                font-size: 15px;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #ffe6e6;
            }
        """)

        right_box = QVBoxLayout()
        right_box.setAlignment(Qt.AlignRight)

        aviso_label = QLabel("Sua ação será enviada para validação")
        aviso_label.setStyleSheet("""
            QLabel {
                font-family: 'Verdana';
                font-weight: bold;
                color: #6c757d;
                font-size: 11px;
                border: none;
            }
        """)
        aviso_label.setAlignment(Qt.AlignRight)

        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.setCursor(Qt.PointingHandCursor)
        self.btn_salvar.setFixedSize(180, 44)
        self.btn_salvar.setStyleSheet("""
            QPushButton {
                font-family: 'Verdana';
                font-weight: bold;
                color: #ffffff;
                background-color: #121f66;
                border: none;
                border-radius: 22px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #0d164a;
            }
        """)

        right_box.addWidget(aviso_label)
        right_box.addWidget(self.btn_salvar, alignment=Qt.AlignRight)

        bottom_layout.addWidget(self.btn_cancelar)
        bottom_layout.addStretch()
        bottom_layout.addLayout(right_box)

        card_layout.addLayout(bottom_layout)
        main_layout.addWidget(card, alignment=Qt.AlignCenter)


class ModeloTelaPesquisador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar ação")
        self.setFixedSize(1920, 1080)
        
        self.setStyleSheet("""
            QWidget {
                font-family: 'Verdana';
                font-weight: bold;
                background-color: #356394;
            }
        """)

        # Menu Lateral
        menu_lateral = QWidget(self)
        menu_lateral.setGeometry(0, 0, 280, 1080)
        menu_lateral.setStyleSheet("QWidget { background-color: #356394; }")

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)

        self.btn_home = btn_layout(os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_acoes = btn_layout(os.path.join(BASE, "Imagens/Ações-Icone.png"), "Minhas Ações")

        logo_label = QLabel()
        logo = QPixmap(LOGO)
        logo_certa = logo.scaled(220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_certa)
        logo_label.setAlignment(Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_acoes)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_acoes)
        
        menu_lateral_layout.addStretch()

        # Cabeçalho
        cabecalho = QWidget(self)
        cabecalho.setGeometry(280, 0, 1640, 70)
        cabecalho.setStyleSheet("QWidget { background-color: #356394; }")

        nome_empregado = QLabel("Fulano da Silva Rodrigues", cabecalho)
        nome_empregado.setGeometry(35, 22, 400, 30)
        nome_empregado.setStyleSheet("QLabel { font-size: 24px; color: #ffffff; }")

        separador = QLabel("|", cabecalho)
        separador.setGeometry(420, 22, 5, 30)
        separador.setStyleSheet("QLabel { font-size: 24px; color: #ffffff; }")

        funcao_empregado = QLabel("Pesquisador", cabecalho)
        funcao_empregado.setGeometry(470, 22, 200, 30)
        funcao_empregado.setStyleSheet("QLabel { color: #ffffff; font-size: 24px; }")

        nome_tela = QLabel("Minhas Ações", cabecalho)
        nome_tela.setGeometry(1000, 22, 300, 30)
        nome_tela.setStyleSheet("QLabel { color: #ffffff; font-size: 20px; font-weight: lighter; }")

        botao_logout = QPushButton("Logout", cabecalho)
        botao_logout.setGeometry(1450, 15, 150, 40)
        botao_logout.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }
        """)

        # Área de Conteúdo Principal (Frame Branco)
        paginaprincipal = QFrame(self)
        paginaprincipal.setGeometry(280, 70, 1640, 1010)
        paginaprincipal.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
            }
        """)

        # Adiciona os campos/inputs dentro do container principal
        container_layout = QVBoxLayout(paginaprincipal)
        container_layout.setContentsMargins(0, 0, 0, 0)
        self.tela_criar_acao = CriarAcaoWidget()
        container_layout.addWidget(self.tela_criar_acao)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaPesquisador()
    window.show()
    sys.exit(app.exec())