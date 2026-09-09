import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
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
    QButtonGroup
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")


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
            "Nome da Tela",
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

        card1 = QLabel(paginaprincipal)
        card1.setFixedSize(300, 238)
        card1.move(50, 100)

        card1.setText(
            "Total de ações\n\n"
            "realizadas:\n\n"
            "50"
        )

        card1.setAlignment(Qt.AlignCenter)

        card1.setStyleSheet("""
            QLabel {
                background-color: #013171;
                color: white;
                border-radius: 20px;
                font-size: 24px;
                font-family: Verdana;
            }
        """)

        card2 = QLabel(paginaprincipal)
        card2.setFixedSize(300, 238)
        card2.move(450, 100)

        card2.setText(
            "Aprovadas\n\n"
            "10"
        )

        card2.setAlignment(Qt.AlignCenter)

        card2.setStyleSheet("""
            QLabel {
                background-color: #058914;
                color: white;
                border-radius: 20px;
                font-size: 24px;
                font-family: Verdana;
            }
        """)

        card3 = QLabel(paginaprincipal)
        card3.setFixedSize(300, 238)
        card3.move(850, 100)

        card3.setText(
            "Em análise\n\n"
            "30"
        )

        card3.setAlignment(Qt.AlignCenter)

        card3.setStyleSheet("""
            QLabel {
                background-color: #0088FF;
                color: white;
                border-radius: 20px;
                font-size: 24px;
                font-family: Verdana;
            }
        """)

        card4 = QLabel(paginaprincipal)
        card4.setFixedSize(300, 238)
        card4.move(1250, 100)

        card4.setText(
            "Negadas\n\n"
            "10"
        )

        card4.setAlignment(Qt.AlignCenter)

        card4.setStyleSheet("""
            QLabel {
                background-color: #FD7B01;
                color: white;
                border-radius: 20px;
                font-size: 24px;
                font-family: Verdana;
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