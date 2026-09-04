import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup,
    QGridLayout, QProgressBar
)

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")


def btn_layout(icone_path, texto):
    btn = QPushButton(texto)
    btn.setFixedHeight(50)
    btn.setStyleSheet("""
        QPushButton {
            background-color: transparent;
            color: white;
            text-align: left;
            padding-left: 20px;
            font-size: 16px;
            border: none;
        }
        QPushButton:hover {
            background-color: #2b5078;
        }
    """)
    return btn


class StatCard(QFrame):

    def __init__(
        self,
        titulo,
        valor,
        percentual,
        cor,
        icone="✓",
        mostrar_barra=True
    ):
        super().__init__()

        self.setFixedSize(220, 150)

        self.setStyleSheet(f"""
        QFrame {{
            background: {cor};
            border-radius: 15px;
        }}

        QLabel {{
            color: white;
            border: none;
        }}
        """)

        layout = QVBoxLayout(self)

        top = QHBoxLayout()

        lbl_icone = QLabel(icone)
        lbl_icone.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("""
            font-size:18px;
        """)

        top.addWidget(lbl_icone)
        top.addWidget(lbl_titulo)
        top.addStretch()

        
        lbl_valor = QLabel(str(valor))
        lbl_valor.setAlignment(Qt.AlignCenter)

        lbl_valor.setStyleSheet("""
            font-size:38px;
            font-weight:bold;
        """)

        # %
        lbl_percentual = QLabel(f"{percentual}%")
        lbl_percentual.setAlignment(Qt.AlignCenter)

        lbl_percentual.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
        """)

        # Barra
        barra = QProgressBar()

        barra.setValue(percentual)
        barra.setTextVisible(False)
        barra.setFixedHeight(12)

        barra.setStyleSheet("""
        QProgressBar {
            background:#ffffff80;
            border:none;
            border-radius:6px;
        }

        QProgressBar::chunk {
            background:white;
            border-radius:6px;
        }
        """)

        layout.addWidget(lbl_valor)
        layout.addWidget(lbl_percentual)
        if mostrar_barra:
            layout.addWidget(barra)


class DonutChart(FigureCanvasQTAgg):

    def __init__(self):
        fig = Figure(facecolor="#ffffff")
        super().__init__(fig)

        ax = fig.add_subplot(111)

        valores = [110, 55, 55]
        cores = [
            "#0AA629",
            "#1885F2",
            "#F57C00"
        ]

        ax.pie(
            valores,
            colors=cores,
            startangle=120,
            autopct='%1.0f%%',
            pctdistance=0.80,  
            wedgeprops=dict(
                width=0.38,
                edgecolor='white'
            ),
            textprops=dict(
                color='white',
                fontsize=12,
                weight='bold'
            )
        )

        ax.text(
            0,
            0,
            "220\nAções",
            ha='center',
            va='center',
            fontsize=18,
            fontweight='bold'
        )

        ax.set_title(
            "Distribuição das Ações",
            fontsize=14,
            weight='bold'
        )

        self.figure.tight_layout()


class SummaryCard(QFrame):

    def __init__(self, titulo, texto, cor):
        super().__init__()

        self.setStyleSheet(f"""
        QFrame {{
            background:white;
            border:1px solid #d6d6d6;
            border-radius:10px;
        }}
        """)

        layout = QHBoxLayout(self)

        icone = QFrame()
        icone.setFixedSize(40,40)

        icone.setStyleSheet(f"""
        background:{cor};
        border-radius:8px;
        """)

        layout_text = QVBoxLayout()

        titulo_lbl = QLabel(titulo)

        titulo_lbl.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
            border:none;
        """)

        texto_lbl = QLabel(texto)
        texto_lbl.setStyleSheet("border: none; color: #333333;")

        layout_text.addWidget(titulo_lbl)
        layout_text.addWidget(texto_lbl)

        layout.addWidget(icone)
        layout.addLayout(layout_text)
        

class ModeloTelaAdministrador(QMainWindow):

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

        menu_lateral = QWidget(self)
        menu_lateral.setGeometry(0, 0, 280, 1080)
        menu_lateral.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)

        self.btn_home = btn_layout(os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_calendario = btn_layout(os.path.join(BASE, "Imagens/Calendario-Icone.png"), "Calendário")
        self.btn_acoes = btn_layout(os.path.join(BASE, "Imagens/Ações-Icone.png"), "Ações")
        self.btn_empregados = btn_layout(os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Empregados")
        self.btn_validadores = btn_layout(os.path.join(BASE, "Imagens/Validadores-Icone.png"), "Validadores")

        logo_label = QLabel()
        logo = QPixmap(LOGO)
        logo_certa = logo.scaled(220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_certa)
        logo_label.setAlignment(Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_calendario)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_acoes)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_empregados)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_validadores)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_calendario)
        self.grupo_botoes.addButton(self.btn_acoes)
        self.grupo_botoes.addButton(self.btn_empregados)
        self.grupo_botoes.addButton(self.btn_validadores)
        
        menu_lateral_layout.addStretch()

        cabecalho = QWidget(self)
        cabecalho.setGeometry(280, 0, 1640, 70)
        cabecalho.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        nome_empregado = QLabel("Fulano da Silva Rodrigues", cabecalho)
        nome_empregado.setGeometry(35, 22, 400, 30)
        nome_empregado.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }
        """)

        separador = QLabel("|", cabecalho)
        separador.setGeometry(420, 22, 5, 30)
        separador.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }
        """)

        funcao_empregado = QLabel("Administrador", cabecalho)
        funcao_empregado.setGeometry(470, 22, 200, 30)
        funcao_empregado.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 24px
            }
        """)

        nome_tela = QLabel("Página principal", cabecalho)
        nome_tela.setGeometry(1000, 22, 300, 30)
        nome_tela.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter
            }
        """)

        botao_logout = QPushButton("Logout", cabecalho)
        botao_logout.setGeometry(1450, 15, 150, 40)
        botao_logout.setStyleSheet("""
            QPushButton{
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }
        """)

        paginaprincipal = QFrame(self)
        paginaprincipal.setGeometry(280, 70, 1600, 1010)
        paginaprincipal.setStyleSheet("""
            QFrame{
                background-color: #F2F4F7;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px
            }
        """)

        main_layout = QVBoxLayout(paginaprincipal)
        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(50)

        top = QHBoxLayout()

        title_lbl = QLabel("Dashboard")

        title_lbl.setStyleSheet("""
        font-size:30px;
        font-weight:bold;
        """)

        ano = QComboBox()

        ano.addItems([
            "2026",
            "2025",
            "2024"
        ])

        ano.setFixedWidth(120)

        top.addStretch()
        top.addWidget(title_lbl)
        top.addStretch()
        top.addWidget(ano)

        main_layout.addLayout(top)

        cards = QGridLayout()

        total = StatCard(
            "Total de ações",
            220,
            100,
            "#0A377B",
            "📋",
            mostrar_barra=False
        )

        aprovadas = StatCard(
            "Aprovadas",
            110,
            50,
            "#009B14",
            "✓"
        )

        analise = StatCard(
            "Em análise",
            55,
            25,
            "#1885F2",
            "◔"
        )

        negadas = StatCard(
            "Negadas",
            55,
            25,
            "#F57C00",
            "✕"
        )

        cards.addWidget(total, 0, 0)
        cards.addWidget(aprovadas, 0, 1)
        cards.addWidget(analise, 0, 2)
        cards.addWidget(negadas, 0, 3)

        main_layout.addLayout(cards)

        content = QHBoxLayout()

        chart_frame = QFrame()

        chart_frame.setStyleSheet("""
        QFrame{
            background:white;
            border-radius:12px;
        }
        """)

        chart_layout = QVBoxLayout(chart_frame)

        chart = DonutChart()
        chart_layout.addWidget(chart)

        summary = QFrame()

        summary.setStyleSheet("""
        QFrame{
            background:white;
            border-radius:12px;
        }
        """)

        summary_layout = QVBoxLayout(summary)

        titulo_resumo = QLabel("Resumo Rápido")

        titulo_resumo.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        """)

        summary_layout.addWidget(titulo_resumo)

        summary_layout.addWidget(
            SummaryCard(
                "Maior Volume",
                "Março/2026\n28 ações",
                "#7BD66A"
            )
        )

        summary_layout.addWidget(
            SummaryCard(
                "Menor Volume",
                "Julho/2026\n12 ações",
                "#FFB85A"
            )
        )

        summary_layout.addWidget(
            SummaryCard(
                "Comparação",
                "Aumento de 12%\nem relação ao mês anterior",
                "#8BC3FF"
            )
        )

        summary_layout.addStretch()

        content.addWidget(chart_frame, 2)
        content.addWidget(summary, 1)

        main_layout.addLayout(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaAdministrador()
    window.show()
    sys.exit(app.exec())