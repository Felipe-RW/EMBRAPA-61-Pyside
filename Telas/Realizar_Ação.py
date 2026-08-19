import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView
)

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

        # Texto ajustado para ficar mais limpo
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


class CriarAcaoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar ação")
        self.setFixedSize(1600, 1010)
        
        self.setStyleSheet("""
            QWidget {
                font-family: 'Verdana';
                font-weight: bold;
                background-color: #f8f9fa;
            }
        """)
        
        self.centralizar_na_tela()
        self.init_ui()

    def centralizar_na_tela(self):
        geo_tela = QApplication.primaryScreen().availableGeometry()
        centro = geo_tela.center()
        geo_janela = self.frameGeometry()
        geo_janela.moveCenter(centro)
        self.move(geo_janela.topLeft())

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(15)

        # 1. TÍTULO FORA DO FRAME PRINCIPAL
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

        # 2. CARD PRINCIPAL (FRAME)
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

        # Nome e Data
        top_row = QHBoxLayout()

        nome_box = QVBoxLayout()
        nome_label = QLabel("Nome:")
        nome_label.setStyleSheet(label_style)
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Digite o nome do artigo aqui...")
        self.nome_input.setAlignment(Qt.AlignCenter)
        self.nome_input.setStyleSheet(input_style)
        nome_box.addWidget(nome_label)
        nome_box.addWidget(self.nome_input)

        data_box = QVBoxLayout()
        data_label = QLabel("Data:")
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
        self.desc_input.setPlaceholderText("Digite a descrição do artigo aqui...")
        self.desc_input.setStyleSheet(input_style)
        self.desc_input.setFixedHeight(120)
        card_layout.addWidget(desc_label)
        card_layout.addWidget(self.desc_input)

        # ComboBox de Ação
        acao_label = QLabel("Ação:")
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
        opcoes = ["Selecionar ação", "Palestra", "Pesquisa", "Entrevista"]
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

        # URL
        url_label = QLabel("Comprovante URL:")
        url_label.setStyleSheet(label_style)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Digite a URL do seu link...")
        self.url_input.setAlignment(Qt.AlignCenter)
        self.url_input.setStyleSheet(input_style)
        
        card_layout.addWidget(url_label)
        card_layout.addWidget(self.url_input)

        # Área de Upload
        upload_label = QLabel("Comprovantes:")
        upload_label.setStyleSheet(label_style)
        self.upload_area = DragDropUploadArea()
        self.upload_area.setFixedHeight(85)
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

        aviso_label = QLabel("Sua postagem será revisada em breve")
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

        self.btn_postar = QPushButton("Postar")
        self.btn_postar.setCursor(Qt.PointingHandCursor)
        self.btn_postar.setFixedSize(180, 44)
        self.btn_postar.setStyleSheet("""
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
        right_box.addWidget(self.btn_postar, alignment=Qt.AlignRight)

        bottom_layout.addWidget(self.btn_cancelar)
        bottom_layout.addStretch()
        bottom_layout.addLayout(right_box)

        card_layout.addLayout(bottom_layout)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CriarAcaoWindow()
    window.show()
    sys.exit(app.exec())