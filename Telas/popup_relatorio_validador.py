import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QDialog, QLabel,
    QPushButton, QCheckBox, QLineEdit
)


class PopupRelatorio(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.estilo = """
        QWidget#fundo {
            background: #F8F8F8;
            border-radius: 20px;
        }

        QWidget#area {
            background: #DFDFDF;
        }

        QLabel#titulo {
            font: bold 32px Verdana;
            color: black;
        }

        QLabel#secao {
            font: bold 20px Verdana;
            color: black;
        }

        QPushButton {
            border: none;
            font: bold 13px Verdana;
        }

        QPushButton#azul {
            background: #356394;
            color: white;
            border-radius: 12px;
        }

        QPushButton#branco {
            background: white;
            color: black;
            border-radius: 12px;
        }

        QPushButton#gerar {
            background: #14298A;
            color: white;
            border-radius: 17px;
        }

        QPushButton#fechar {
            background: transparent;
            color: black;
            font: bold 30px Arial;
        }

        QCheckBox {
            font: 14px Verdana;
            color: #202020;
            spacing: 12px;
        }

        QCheckBox::indicator {
            width: 23px;
            height: 23px;
            background: #F8F8F8;
            border: 1px solid #72937A;
            border-radius: 8px;
        }

        QCheckBox::indicator:checked {
            background: #356394;
        }

        QLineEdit {
            background: white;
            border: 1px solid #8D8D8D;
            border-radius: 10px;
            font: italic 16px Verdana;
            padding-left: 12px;
        }
        """

        self.setFixedSize(1504, 639)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet(self.estilo)

        self.fundo = QWidget(self)
        self.fundo.setObjectName("fundo")
        self.fundo.setGeometry(0, 0, 1504, 639)

        self.criarLabel(
            "Relatório", 670, 37, 164, 45,
            "titulo", self.fundo, True
        )

        self.btnFechar = self.criarBtn(
            "X", 1420, 15, 60, 50,
            "fechar", self.fundo
        )
        self.btnFechar.clicked.connect(self.close)

        self.btnRelatorio = self.criarBtn(
            "Relatório de Pesquisas",
            54, 149, 303, 39,
            "azul", self.fundo
        )

        self.area = QWidget(self.fundo)
        self.area.setObjectName("area")
        self.area.setGeometry(54, 208, 1395, 354)

        self.criarDados()
        self.criarAnos()
        self.criarPesquisadores()

        self.btnGerar = self.criarBtn(
            "Gerar Relatório",
            1180, 575, 269, 34,
            "gerar", self.fundo
        )

    def criarLabel(self, texto, x, y, largura, altura, nome, pai, centro=False):
        label = QLabel(texto, pai)
        label.setObjectName(nome)
        label.setGeometry(x, y, largura, altura)

        if centro:
            label.setAlignment(Qt.AlignCenter)

        return label

    def criarBtn(self, texto, x, y, largura, altura, nome, pai):
        btn = QPushButton(texto, pai)
        btn.setObjectName(nome)
        btn.setGeometry(x, y, largura, altura)
        return btn

    def criarCheck(self, texto, x, y):
        checkBox = QCheckBox(texto, self.area)
        checkBox.setGeometry(x, y, 300, 30)
        return checkBox

    def criarLinha(self, x):
        linha = QWidget(self.area)
        linha.setGeometry(x, 20, 1, 280)
        linha.setStyleSheet("background: #707070;")

    def criarDados(self):
        self.criarLabel(
            "Dados do Relatório",
            40, 30, 300, 30,
            "secao", self.area
        )

        dados = [
            "Categoria de Ação",
            "Data de Postagem",
            "Status",
            "Pesquisador",
            "Setor"
        ]

        posicoesY = [70, 105, 140, 175, 210]

        for texto, posicaoY in zip(dados, posicoesY):
            self.criarCheck(texto, 40, posicaoY)

        self.criarLinha(465)

    def criarAnos(self):
        self.criarLabel(
            "Anos",
            500, 30, 200, 30,
            "secao", self.area
        )

        self.btnSelecionarAnos = self.criarBtn(
            "Selecionar anos",
            500, 70, 190, 24,
            "azul", self.area
        )

        self.btnTodosAnos = self.criarBtn(
            "Todos os anos",
            700, 70, 190, 24,
            "branco", self.area
        )

        anos = ["2022", "2023", "2024", "2025", "2026"]
        posicoesY = [115, 155, 195, 235, 275]

        for ano, posicaoY in zip(anos, posicoesY):
            self.criarCheck(ano, 500, posicaoY)

        self.criarLinha(930)

    def criarPesquisadores(self):
        self.criarLabel(
            "Pesquisadores",
            965, 30, 250, 30,
            "secao", self.area
        )

        self.btnSelecionarPesquisadores = self.criarBtn(
            "Selecionar pesquisadores",
            965, 70, 190, 24,
            "azul", self.area
        )

        self.btnTodosPesquisadores = self.criarBtn(
            "Todos os pesquisadores",
            1170, 70, 190, 24,
            "branco", self.area
        )

        self.campoPesquisa = QLineEdit(self.area)
        self.campoPesquisa.setPlaceholderText("Pesquise...")
        self.campoPesquisa.setGeometry(1012, 105, 300, 42)

        pesquisadores = [
            "Fulano da Silva",
            "Ciclano da Silva",
            "Beltrano da Silva"
        ]

        posicoesY = [155, 195, 235]

        for nome, posicaoY in zip(pesquisadores, posicoesY):
            self.criarCheck(nome, 970, posicaoY)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    popup = PopupRelatorio()
    popup.exec()

    sys.exit(app.exec())