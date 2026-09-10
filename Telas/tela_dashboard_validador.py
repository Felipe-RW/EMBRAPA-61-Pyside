import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QPainter
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QFrame,
    QFileDialog,
    QListView,
    QMainWindow,
    QButtonGroup,
    QProgressBar
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")


def icone_branco(caminho, tamanho):
    pixmap = QPixmap(caminho).scaled(
        tamanho,
        tamanho,
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )

    resultado = QPixmap(pixmap.size())
    resultado.fill(Qt.transparent)

    painter = QPainter(resultado)
    painter.drawPixmap(0, 0, pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(resultado.rect(), Qt.white)
    painter.end()

    return resultado


class ModeloTelaValidador(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Criar ação")
        self.setFixedSize(1920, 1080)

        self.setStyleSheet("""
            QWidget {
                font-family: Verdana;
                font-weight: bold;
                background-color: #356394;
            }
        """)

        menu_lateral = QWidget(self)
        menu_lateral.setGeometry(0, 0, 280, 1080)

        menu_lateral.setStyleSheet("""
            QWidget {
                background-color: #356394;
            }
        """)

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)
        menu_lateral_layout.setSpacing(5)

        self.btn_home = btn_layout(
            os.path.join(BASE, "Imagens", "Painel-Principal-Icone.png"),
            "Painel Principal"
        )

        self.btn_acoes = btn_layout(
            os.path.join(BASE, "Imagens", "Validações-Icone.png"),
            "Validações"
        )

        logo_label = QLabel()

        logo = QPixmap(LOGO)

        logo_certa = logo.scaled(
            220,
            190,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        logo_label.setPixmap(logo_certa)
        logo_label.setAlignment(Qt.AlignLeft)

        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.addWidget(self.btn_acoes)

        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_acoes)

        menu_lateral_layout.addStretch()

        cabecalho = QWidget(self)
        cabecalho.setGeometry(280, 0, 1640, 70)

        cabecalho.setStyleSheet("""
            QWidget {
                background-color: #356394;
            }
        """)

        nome_empregado = QLabel(
            "Fulano da Silva Rodrigues",
            cabecalho
        )

        nome_empregado.setGeometry(35, 22, 400, 30)

        nome_empregado.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #ffffff;
            }
        """)

        separador = QLabel("|", cabecalho)
        separador.setGeometry(420, 22, 5, 30)

        separador.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #ffffff;
            }
        """)

        funcao_empregado = QLabel(
            "Validador",
            cabecalho
        )

        funcao_empregado.setGeometry(470, 22, 200, 30)

        funcao_empregado.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 24px;
            }
        """)

        nome_tela = QLabel(
            "Painel Principal",
            cabecalho
        )

        nome_tela.setGeometry(1000, 22, 300, 30)

        nome_tela.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter;
            }
        """)

        botao_logout = QPushButton(
            "Logout",
            cabecalho
        )

        botao_logout.setGeometry(1450, 15, 150, 40)

        botao_logout.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: none;
                border-radius: 10px;
            }
        """)

        paginaprincipal = QFrame(self)

        paginaprincipal.setGeometry(
            280,
            70,
            1600,
            1010
        )

        paginaprincipal.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
            }
        """)

        titulo = QLabel(
            "DashBoard",
            paginaprincipal
        )

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setGeometry(
            700,
            30,
            250,
            70
        )

        titulo.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: #000000;
                font-size: 36px;
            }
        """)

        card_realizadas = QLabel(paginaprincipal)
        card_realizadas.setFixedSize(300, 238)
        card_realizadas.move(50, 100)
        card_realizadas.setStyleSheet("""
            QLabel {
                background-color: #013171;
                border-radius: 20px;
            }
        """)

        card_realizadas_texto = QLabel(card_realizadas)
        card_realizadas_texto.setText("Total de ações\n   realizadas:")
        card_realizadas_texto.setFixedSize(300, 80)
        card_realizadas_texto.move(0, 10)
        card_realizadas_texto.setAlignment(Qt.AlignCenter)
        card_realizadas_texto.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 24px;
                font-family: Verdana;
                font-weight: normal;
            }
        """)

        card_realizadas_numero = QLabel(card_realizadas)
        card_realizadas_numero.setText("35")
        card_realizadas_numero.setFixedSize(300, 90)
        card_realizadas_numero.move(0, 80)
        card_realizadas_numero.setAlignment(Qt.AlignCenter)
        card_realizadas_numero.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 50px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        card_aprovadas = QLabel(paginaprincipal)
        card_aprovadas.setFixedSize(300, 238)
        card_aprovadas.move(450, 100)
        card_aprovadas.setStyleSheet("""
            QLabel {
                background-color: #058914;
                border-radius: 20px;
            }
        """)

        icone_aprovadas = QLabel(card_aprovadas)
        icone_aprovadas.setFixedSize(35, 35)
        icone_aprovadas.move(25, 18)

        icone_aprovadas.setPixmap(
            icone_branco(
                os.path.join(BASE, "Imagens", "check.png"),
                30
            )
        )

        icone_aprovadas.setStyleSheet("""
            QLabel {
                background-color: transparent;
            }
        """)

        card_aprovadas_texto = QLabel(card_aprovadas)
        card_aprovadas_texto.setText("Aprovadas:")
        card_aprovadas_texto.setFixedSize(300, 40)
        card_aprovadas_texto.move(0, 10)
        card_aprovadas_texto.setAlignment(Qt.AlignCenter)
        card_aprovadas_texto.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 24px;
                font-family: Verdana;
                font-weight: normal;
            }
        """)

        card_aprovadas_numero = QLabel(card_aprovadas)
        card_aprovadas_numero.setText("15")
        card_aprovadas_numero.setFixedSize(300, 70)
        card_aprovadas_numero.move(0, 80)
        card_aprovadas_numero.setAlignment(Qt.AlignCenter)
        card_aprovadas_numero.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 50px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        card_aprovadas_pct = QLabel(card_aprovadas)
        card_aprovadas_pct.setText("42%")
        card_aprovadas_pct.setFixedSize(300, 30)
        card_aprovadas_pct.move(0, 165)
        card_aprovadas_pct.setAlignment(Qt.AlignCenter)
        card_aprovadas_pct.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 20px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        card_aprovadas_barra = QProgressBar(card_aprovadas)
        card_aprovadas_barra.setGeometry(50, 200, 200, 12)
        card_aprovadas_barra.setValue(42)
        card_aprovadas_barra.setTextVisible(False)
        card_aprovadas_barra.setStyleSheet("""
            QProgressBar {
                background-color: #2e6033;
                border-radius: 6px;
                border: none;
            }
            QProgressBar::chunk {
                background-color: #ffffff;
                border-radius: 6px;
            }
        """)

        card_analise = QLabel(paginaprincipal)
        card_analise.setFixedSize(300, 238)
        card_analise.move(850, 100)
        card_analise.setStyleSheet("""
            QLabel {
                background-color: #0088FF;
                border-radius: 20px;
            }
        """)

        icone_analise = QLabel(card_analise)
        icone_analise.setFixedSize(35, 35)
        icone_analise.move(25, 18)

        icone_analise.setPixmap(
            icone_branco(
                os.path.join(BASE, "Imagens", "relogio.png"),
                35
            )
        )

        icone_analise.setStyleSheet("""
            QLabel {
                background-color: transparent;
            }
        """)

        card_analise_texto = QLabel(card_analise)
        card_analise_texto.setText("Em análise:")
        card_analise_texto.setFixedSize(300, 40)
        card_analise_texto.move(0, 10)
        card_analise_texto.setAlignment(Qt.AlignCenter)
        card_analise_texto.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 24px;
                font-family: Verdana;
                font-weight: normal;
            }
        """)

        card_analise_numero = QLabel(card_analise)
        card_analise_numero.setText("15")
        card_analise_numero.setFixedSize(300, 70)
        card_analise_numero.move(0, 80)
        card_analise_numero.setAlignment(Qt.AlignCenter)
        card_analise_numero.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 50px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        card_analise_pct = QLabel(card_analise)
        card_analise_pct.setText("42%")
        card_analise_pct.setFixedSize(300, 30)
        card_analise_pct.move(0, 165)
        card_analise_pct.setAlignment(Qt.AlignCenter)
        card_analise_pct.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 20px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        card_analise_barra = QProgressBar(card_analise)
        card_analise_barra.setGeometry(50, 200, 200, 12)
        card_analise_barra.setValue(42)
        card_analise_barra.setTextVisible(False)
        card_analise_barra.setStyleSheet("""
            QProgressBar {
                background-color: #55a8f5;
                border-radius: 6px;
                border: none;
            }
            QProgressBar::chunk {
                background-color: #ffffff;
                border-radius: 6px;
            }
        """)

        card_negadas = QLabel(paginaprincipal)
        card_negadas.setFixedSize(300, 238)
        card_negadas.move(1250, 100)
        card_negadas.setStyleSheet("""
            QLabel {
                background-color: #FD7B01;
                border-radius: 20px;
            }
        """)

        icone_negadas = QLabel(card_negadas)
        icone_negadas.setFixedSize(35, 35)
        icone_negadas.move(25, 18)

        icone_negadas.setPixmap(
            icone_branco(
                os.path.join(BASE, "Imagens", "cruz.png"),
                30
            )
        )

        icone_negadas.setStyleSheet("""
            QLabel {
                background-color: transparent;
            }
        """)

        card_negadas_texto = QLabel(card_negadas)
        card_negadas_texto.setText("Negadas:")
        card_negadas_texto.setFixedSize(300, 40)
        card_negadas_texto.move(0, 10)
        card_negadas_texto.setAlignment(Qt.AlignCenter)
        card_negadas_texto.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 24px;
                font-family: Verdana;
                font-weight: normal;
            }
        """)

        card_negadas_numero = QLabel(card_negadas)
        card_negadas_numero.setText("5")
        card_negadas_numero.setFixedSize(300, 70)
        card_negadas_numero.move(0, 80)
        card_negadas_numero.setAlignment(Qt.AlignCenter)
        card_negadas_numero.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 50px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        card_negadas_pct = QLabel(card_negadas)
        card_negadas_pct.setText("15%")
        card_negadas_pct.setFixedSize(300, 30)
        card_negadas_pct.move(0, 165)
        card_negadas_pct.setAlignment(Qt.AlignCenter)
        card_negadas_pct.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-size: 20px;
                font-family: Verdana;
                font-weight: bold;
            }
        """)

        card_negadas_barra = QProgressBar(card_negadas)
        card_negadas_barra.setGeometry(50, 200, 200, 12)
        card_negadas_barra.setValue(15)
        card_negadas_barra.setTextVisible(False)
        card_negadas_barra.setStyleSheet("""
            QProgressBar {
                background-color: #f7a052;
                border-radius: 6px;
                border: none;
            }
            QProgressBar::chunk {
                background-color: #ffffff;
                border-radius: 6px;
            }
        """)

        quadro_grafico = QLabel(paginaprincipal)
        quadro_grafico.setFixedSize(700, 500)
        quadro_grafico.move(50, 400)

        quadro_grafico.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #C3C3C3;
                border-radius: 10px;
            }
        """)

        circulo_status_aprovadas = QLabel(paginaprincipal)
        circulo_status_aprovadas.setGeometry(540, 550, 16, 16)
        circulo_status_aprovadas.setStyleSheet("""
            QLabel {
                border-radius: 8px;
                background-color: #058914;
            }
        """)

        texto_aprovadas = QLabel(paginaprincipal)
        texto_aprovadas.setText("Aprovadas")
        texto_aprovadas.move(570, 550)
        texto_aprovadas.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        subtitulo_aprovadas = QLabel(paginaprincipal)
        subtitulo_aprovadas.setText("10 (20%)")
        subtitulo_aprovadas.move(575, 570)
        subtitulo_aprovadas.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        circulo_status_analise = QLabel(paginaprincipal)
        circulo_status_analise.setGeometry(540, 650, 16, 16)
        circulo_status_analise.setStyleSheet("""
            QLabel {
                border-radius: 8px;
                background-color: #0088FF;
            }
        """)

        texto_analise = QLabel(paginaprincipal)
        texto_analise.setText("Em análise")
        texto_analise.move(570, 650)
        texto_analise.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        subtitulo_analise = QLabel(paginaprincipal)
        subtitulo_analise.setText("15 (42%)")
        subtitulo_analise.move(575, 670)
        subtitulo_analise.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        circulo_status_reprovadas = QLabel(paginaprincipal)
        circulo_status_reprovadas.setGeometry(540, 750, 16, 16)
        circulo_status_reprovadas.setStyleSheet("""
            QLabel {
                border-radius: 8px;
                background-color: #FD7B01;
            }
        """)

        texto_negadas = QLabel(paginaprincipal)
        texto_negadas.setText("Negadas")
        texto_negadas.move(570, 750)
        texto_negadas.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        subtitulo_negadas = QLabel(paginaprincipal)
        subtitulo_negadas.setText("10 (20%)")
        subtitulo_negadas.move(570, 770)
        subtitulo_negadas.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        quadro_resumo = QLabel(paginaprincipal)
        quadro_resumo.setFixedSize(700, 500)
        quadro_resumo.move(858, 400)

        quadro_resumo.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #C3C3C3;
                border-radius: 10px;
            }
        """)

        texto_resumo = QLabel(paginaprincipal)
        texto_resumo.setText("Resumo rápido")
        texto_resumo.move(1100, 430)
        texto_resumo.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        quadro_maior_resumo = QLabel(paginaprincipal)
        quadro_maior_resumo.setFixedSize(657, 108)
        quadro_maior_resumo.move(880, 500)

        quadro_maior_resumo.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #C3C3C3;
                border-radius: 10px;
            }
        """)

        maior_volume_icone = QLabel(paginaprincipal)
        maior_volume_icone.setFixedSize(80, 80)
        maior_volume_icone.move(890, 515)
        maior_volume_icone.setStyleSheet("""
            QLabel {
                background-color: #6EC178;
                border-radius: 10px;
            }
        """)

        texto_maior_resumo = QLabel(paginaprincipal)
        texto_maior_resumo.setText("Maior volume")
        texto_maior_resumo.move(1000, 515)
        texto_maior_resumo.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 18px;
                font-family: Verdana;
                font-style: bold;
            }
        """)

        subtitulo_maior_volume = QLabel(paginaprincipal)
        subtitulo_maior_volume.setText("Março/2026 \n 28 Ações")
        subtitulo_maior_volume.move(1000, 545)

        quadro_menor_resumo = QLabel(paginaprincipal)
        quadro_menor_resumo.setFixedSize(657, 108)
        quadro_menor_resumo.move(880, 630)

        quadro_menor_resumo.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #C3C3C3;
                border-radius: 10px;
            }
        """)

        menor_volume_icone = QLabel(paginaprincipal)
        menor_volume_icone.setFixedSize(80, 80)
        menor_volume_icone.move(890, 645)
        menor_volume_icone.setStyleSheet("""
             QLabel {
                background-color: #FFB570;
                border-radius: 10px;
             }
        """)

        texto_menor_resumo = QLabel(paginaprincipal)
        texto_menor_resumo.setText("Menor volume")
        texto_menor_resumo.move(1000, 645)
        texto_menor_resumo.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 18px;
                font-family: Verdana;
                font-style: bold;
             }
        """)

        subtitulo_menor_volume = QLabel(paginaprincipal)
        subtitulo_menor_volume.setText("Julho/2026 \n 12 Ações")
        subtitulo_menor_volume.move(1000, 675)

        quadro_comparacao = QLabel(paginaprincipal)
        quadro_comparacao.setFixedSize(657, 108)
        quadro_comparacao.move(880, 760)
        quadro_comparacao.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #C3C3C3;
                border-radius: 10px;
            }
        """)

        comparacao_icone = QLabel(paginaprincipal)
        comparacao_icone.setFixedSize(80, 80)
        comparacao_icone.move(890, 775)
        comparacao_icone.setStyleSheet("""
            QLabel {
                background-color: #89BFEF;
                border-radius: 10px;
             }
        """)

        texto_comparacao = QLabel(paginaprincipal)
        texto_comparacao.setText("Comparação")
        texto_comparacao.move(1000, 775)
        texto_comparacao.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 18px;
                font-family: Verdana;
                font-style: bold;
             }
        """)

        subtitulo_comparacao = QLabel(paginaprincipal)
        subtitulo_comparacao.setText("Aumento de 12%\nem relação ao mês anterior")
        subtitulo_comparacao.move(1000, 805)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ModeloTelaValidador()
    window.show()

    sys.exit(app.exec())