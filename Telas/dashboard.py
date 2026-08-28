import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QComboBox,
    QHBoxLayout,
    QProgressBar
)

from PySide6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


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
    pctdistance=0.80,  # controla a posição da %
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

        layout_text.addWidget(titulo_lbl)
        layout_text.addWidget(texto_lbl)

        layout.addWidget(icone)
        layout.addLayout(layout_text)
        

class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dashboard Administrativo")
        self.resize(1400, 850)

        self.setStyleSheet("""
        QWidget{
            background:#F2F4F7;
            font-family: Segoe UI;
        }
        """)

        main_layout = QVBoxLayout(self)

        header = QFrame()

        header.setStyleSheet("""
        QFrame{
            background:#305F91;
            border-radius:12px;
        }
        """)

        header_layout = QHBoxLayout(header)

        info_usuario = QLabel(
            "Fulano da Silva Rodrigues | Administrador"
        )

        info_usuario.setStyleSheet("""
            color:white;
            font-size:16px;
            font-weight:bold;
            background:transparent;
        """)

        titulo = QLabel("Painel Principal")

        titulo.setStyleSheet("""
            color:white;
            font-size:15px;
            background:transparent;
        """)

        logout = QPushButton("Logout")

        logout.setStyleSheet("""
        QPushButton{
            background:white;
            color:#305F91;
            font-weight:bold;
            border-radius:15px;
            padding:8px 20px;
        }

        QPushButton:hover{
            background:#e7edf5;
        }
        """)

        header_layout.addWidget(info_usuario)
        header_layout.addStretch()
        header_layout.addWidget(titulo)
        header_layout.addStretch()
        header_layout.addWidget(logout)

        main_layout.addWidget(header)

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

        cards.addWidget(total)
        cards.addWidget(aprovadas,0,1)
        cards.addWidget(analise,0,2)
        cards.addWidget(negadas,0,3)

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

    window = Dashboard()
    window.show()

    sys.exit(app.exec())