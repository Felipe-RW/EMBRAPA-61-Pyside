import sys
import os
from pathlib import Path
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QButtonGroup,)

BASE = Path(__file__).resolve().parents[1]
CAMINHO_LOGO = BASE / "Imagens" / "Embrapa-Logo.png"
CAMINHO_ICONE_UPLOAD = BASE / "Imagens" / "Upload-Icone.png"

sys.path.insert(0, str(BASE))

ESTILO_QSS = r"""

QMainWindow,
#areaPrincipal {
    background: #356394;
    font-family: Verdana;
}

#menuLateral,
#cabecalho,
#areaDireita {
    background: #356394;
}

#nomeEmpregado,
#separador,
#funcaoEmpregado,
#nomeTela {
    color: #ffffff;
}

#nomeEmpregado {
    font-size: 24px;
    font-weight: bold;
}

#separador {
    font-size: 24px;
}

#funcaoEmpregado {
    font-size: 24px;
    font-weight: bold;
}

#nomeTela {
    font-size: 20px;
    font-weight: bold;
}

#botaoLogout {
    background: #ffffff;
    color: #08175C;
    border: none;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}

#botaoLogout:hover {
    background: #E9E9E9;
}

#areaConteudo {
    background: #ffffff;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}

#titulo {
    color: #111111;
    font-size: 30px;
    font-weight: 700;
}

#cartaoFormulario {
    background: #ffffff;
    border: 1px solid #D9D9D9;
    border-radius: 11px;
}

#rotulo {
    color: #111111;
    font-size: 14px;
    font-weight: 700;
}

#campoNome,
#campoData,
#campoUrl,
#seletorAcao {
    background: #ffffff;
    color: #333333;
    border: 1px solid #999999;
    border-radius: 5px;
    font-size: 13px;
    padding: 0 8px;
}

#campoNome:focus,
#campoData:focus,
#campoUrl:focus,
#seletorAcao:focus,
#campoDescricao:focus {
    border: 1px solid #5FBCE4;
}

#campoNome,
#campoData,
#campoUrl {
    min-height: 34px;
    max-height: 34px;
}

#campoNome::placeholder,
#campoData::placeholder,
#campoUrl::placeholder {
    color: #AAAAAA;
    font-weight: 600;
}

#campoData {
    min-width: 180px;
    max-width: 180px;
}

#campoDescricao {
    background: #ffffff;
    color: #333333;
    border: 1px solid #999999;
    border-radius: 5px;
    font-size: 13px;
    padding: 8px;
}

#campoDescricao::placeholder {
    color: #AAAAAA;
    font-weight: 600;
}

#seletorAcao {
    min-height: 34px;
    max-height: 34px;
}

#seletorAcao::drop-down {
    width: 30px;
    border: none;
}

#seletorAcao QAbstractItemView {
    background: #ffffff;
    color: #222222;
    border: 1px solid #999999;
    selection-background-color: #E9E9E9;
    selection-color: #222222;
}

#areaUpload {
    background: #F0F1F3;
    border: 1px dashed #777777;
    border-radius: 4px;
}

#iconeUpload {
    background: transparent;
}

#textoUpload {
    background: transparent;
    color: #222222;
    font-size: 12px;
}

#botaoCancelar {
    background: #ffffff;
    color: #E00000;
    border: 1px solid #E00000;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 700;
}

#botaoCancelar:hover {
    background: #E00000;
    color: #ffffff;
}

#botaoPostar {
    background: #102174;
    color: #ffffff;
    border: none;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 700;
}

#botaoPostar:hover {
    background: #058914;
}

#textoAviso {
    color: #102174;
    font-size: 10px;
    padding-right: 5px;
}

"""

class btn_layout(QPushButton):
    def __init__(self, path, texto, parent=None):
        super().__init__(parent)

        self.setStyleSheet ("""
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

class TelaCriarAcao(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Criar ação")
        self.setFixedSize(1920, 1080)

        self.criar_interface()

        self.setStyleSheet(ESTILO_QSS)

    def criar_interface(self):

        area_principal = QWidget()
        area_principal.setObjectName("areaPrincipal")
        self.setCentralWidget(area_principal)

        menu_lateral = QWidget(area_principal)
        menu_lateral.setObjectName("menuLateral")
        menu_lateral.setGeometry(0, 0, 280, 1080)

        layout_menu = QVBoxLayout(menu_lateral)
        layout_menu.setContentsMargins(30, 0, 0, 0)
        layout_menu.setSpacing(5)

        etiqueta_logo = QLabel()
        logo = QPixmap(str(CAMINHO_LOGO))
        logo_certa = logo.scaled(220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        etiqueta_logo.setPixmap(logo_certa)
        etiqueta_logo.setAlignment(Qt.AlignLeft)

        layout_menu.addWidget(etiqueta_logo)

        self.botao_painel = btn_layout(str(BASE / "Imagens" / "Painel-Principal-Icone.png"), "Painel Principal")
        self.botao_acoes = btn_layout(str(BASE / "Imagens" / "acoes.png"),"Ações")

        layout_menu.addWidget(self.botao_painel)
        layout_menu.addWidget(self.botao_acoes)
        layout_menu.addStretch()

        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.botao_painel)
        self.grupo_botoes.addButton(self.botao_acoes)

        cabecalho = QWidget(area_principal)
        cabecalho.setObjectName("cabecalho")
        cabecalho.setGeometry(280, 0, 1600, 70)

        nome_empregado = QLabel("Fulano da Silva Rodrigues", cabecalho)
        nome_empregado.setObjectName("nomeEmpregado")
        nome_empregado.setGeometry(35, 22, 400, 30)

        separador = QLabel("|", cabecalho)
        separador.setObjectName("separador")
        separador.setGeometry(360, 22, 5, 30)

        funcao_empregado = QLabel("Pesquisador", cabecalho)
        funcao_empregado.setObjectName("funcaoEmpregado")
        funcao_empregado.setGeometry(400, 22, 200, 30)

        nome_tela = QLabel("Criar ação", cabecalho)
        nome_tela.setObjectName("nomeTela")
        nome_tela.setGeometry(800, 22, 300, 30)
        nome_tela.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        botao_logout = QPushButton("Logout", cabecalho)
        botao_logout.setObjectName("botaoLogout")
        botao_logout.setGeometry(1450, 15, 150, 40)

        area_direita = QWidget(area_principal)
        area_direita.setObjectName("areaDireita")
        area_direita.setGeometry(1880, 0, 40, 1080)

        area_conteudo = QFrame(area_principal)
        area_conteudo.setObjectName("areaConteudo")
        area_conteudo.setGeometry(280, 70, 1600, 1010)

        layout_conteudo = QVBoxLayout(area_conteudo)
        layout_conteudo.setContentsMargins(70, 35, 70, 45)
        layout_conteudo.setSpacing(12)

        titulo = QLabel("Criar ação")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        layout_conteudo.addWidget(titulo)

        cartao = QFrame()
        cartao.setObjectName("cartaoFormulario")
        layout_conteudo.addWidget(cartao, 1)

        layout_cartao = QVBoxLayout(cartao)
        layout_cartao.setContentsMargins(28, 22, 28, 20)
        layout_cartao.setSpacing(10)

        linha_nome_data = QHBoxLayout()
        linha_nome_data.setSpacing(36)

        bloco_nome = QVBoxLayout()
        bloco_nome.setSpacing(5)

        rotulo_nome = QLabel("Nome:")
        rotulo_nome.setObjectName("rotulo")
        bloco_nome.addWidget(rotulo_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setObjectName("campoNome")
        self.campo_nome.setPlaceholderText("Digite o nome do artigo aqui...")
        bloco_nome.addWidget(self.campo_nome)

        linha_nome_data.addLayout(bloco_nome, 1)

        bloco_data = QVBoxLayout()
        bloco_data.setSpacing(5)

        rotulo_data = QLabel("Data de Execução:")
        rotulo_data.setObjectName("rotulo")
        bloco_data.addWidget(rotulo_data)

        self.campo_data = QLineEdit()
        self.campo_data.setObjectName("campoData")
        self.campo_data.setPlaceholderText("___/___/____")
        bloco_data.addWidget(self.campo_data)

        linha_nome_data.addLayout(bloco_data)

        layout_cartao.addLayout(linha_nome_data)

        rotulo_descricao = QLabel("Descrição:")
        rotulo_descricao.setObjectName("rotulo")
        layout_cartao.addWidget(rotulo_descricao)

        self.campo_descricao = QTextEdit()
        self.campo_descricao.setObjectName("campoDescricao")
        self.campo_descricao.setPlaceholderText("Digite a descrição do artigo aqui...")
        self.campo_descricao.setMinimumHeight(115)
        layout_cartao.addWidget(self.campo_descricao)

        rotulo_acao = QLabel("Ação:")
        rotulo_acao.setObjectName("rotulo")
        layout_cartao.addWidget(rotulo_acao)

        self.seletor_acao = QComboBox()
        self.seletor_acao.setObjectName("seletorAcao")
        self.seletor_acao.addItem("Selecionar ação")
        layout_cartao.addWidget(self.seletor_acao)

        rotulo_url = QLabel("Comprovante URL:")
        rotulo_url.setObjectName("rotulo")
        layout_cartao.addWidget(rotulo_url)

        self.campo_url = QLineEdit()
        self.campo_url.setObjectName("campoUrl")
        self.campo_url.setPlaceholderText("Digite a URL do seu link...")
        layout_cartao.addWidget(self.campo_url)

        rotulo_comprovantes = QLabel("Comprovantes:")
        rotulo_comprovantes.setObjectName("rotulo")
        layout_cartao.addWidget(rotulo_comprovantes)

        area_upload = QFrame()
        area_upload.setObjectName("areaUpload")
        area_upload.setMinimumHeight(90)

        layout_upload = QHBoxLayout(area_upload)
        layout_upload.setContentsMargins(20, 0, 20, 0)
        layout_upload.setSpacing(8)
        layout_upload.setAlignment(Qt.AlignCenter)

        icone_upload = QLabel()
        icone_upload.setObjectName("iconeUpload")
        icone_upload.setAlignment(Qt.AlignCenter)
        imagem_upload = QPixmap(str(CAMINHO_ICONE_UPLOAD))
        imagem_upload = imagem_upload.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icone_upload.setPixmap(imagem_upload)
        layout_upload.addWidget(icone_upload)

        texto_upload = QLabel("<b>Arraste seus arquivos aqui ou clique para fazer Upload</b> " "(PDF, DOCX, Imagens...)")
        texto_upload.setObjectName("textoUpload")
        texto_upload.setAlignment(Qt.AlignCenter)
        layout_upload.addWidget(texto_upload)

        layout_cartao.addWidget(area_upload)

        linha_botoes = QHBoxLayout()
        linha_botoes.setContentsMargins(0, 8, 0, 0)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("botaoCancelar")
        botao_cancelar.setFixedSize(137, 32)
        linha_botoes.addWidget(botao_cancelar)

        linha_botoes.addStretch()

        texto_aviso = QLabel("Sua postagem será revisada em breve")
        texto_aviso.setObjectName("textoAviso")
        texto_aviso.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        linha_botoes.addWidget(texto_aviso)

        botao_postar = QPushButton("Postar")
        botao_postar.setObjectName("botaoPostar")
        botao_postar.setFixedSize(137, 32)
        linha_botoes.addWidget(botao_postar)

        layout_cartao.addLayout(linha_botoes)


if __name__ == "__main__":
    aplicativo = QApplication(sys.argv)
    janela = TelaCriarAcao()
    janela.show()
    sys.exit(aplicativo.exec())