from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QFrame,QComboBox,QGridLayout,QTableWidget,QTableWidgetItem,QHeaderView,QAbstractItemView,QToolButton
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtCore import Qt,QSize
import sys
from style import QSS

DROPDOWN = "Imagens/Vector_dropdown.png"

class popup_editar_ano(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(750,500)
        self.setWindowTitle("Editar ano")


        self.layout_vertical = QVBoxLayout()
        

        self.setLayout(self.layout_vertical)

        background_gaveta = QFrame()

        background_gaveta.setStyleSheet(QSS)

        background_gaveta.setObjectName("background_gaveta")

        self.layout_vertical.addWidget(background_gaveta)
        
        self.layout_gaveta = QHBoxLayout()  

        self.layout_gaveta_interna = QHBoxLayout()

        background_gaveta_branco = QComboBox()


        background_gaveta_branco.setLayout(self.layout_gaveta_interna)
 

        background_gaveta_branco.setStyleSheet(QSS)
        background_gaveta_branco.setObjectName("fundo_branco")
        self.layout_gaveta.addWidget(background_gaveta_branco)
        

        background_gaveta.setLayout(self.layout_gaveta)

        acoe = acoes()
        grade = tabela()

        self.layout_vertical.addWidget(acoe)
        self.layout_vertical.setSpacing(20)
        

        acoes_add = QLabel("Ações adicionadas para o ano")
        acoes_add.setContentsMargins(0,10,0,0)
        acoes_add.setStyleSheet("""color: #00409A;
            font-size:18px;
            font-weight: bold;""")
        
        

        self.layout_vertical.addWidget(acoes_add,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_vertical.addLayout(grade)
        
        self.layout_vertical.addStretch(1)

        
        


class acoes(QFrame):
    def __init__(self):
        super().__init__()
        self.layout_vertical = QVBoxLayout()
        self.setStyleSheet(QSS)
        self.setObjectName("aiai")
        self.layout_txt_acoes = QHBoxLayout()
        self.layout_acoes = QHBoxLayout()
        self.layout_vertical_organizador = QVBoxLayout()
        gaveta_acoes = QComboBox()
        gaveta_acoes.setObjectName("acoes")
        limite = QLineEdit()
        limite.setObjectName("input")
        peso = QLineEdit()
        peso.setObjectName("input")
        self.layout_acoes.addWidget(gaveta_acoes)
        self.layout_acoes.addWidget(limite)
        self.layout_acoes.addWidget(peso)
        txt_acoes = QLabel("Ações*")
        txt_acoes.setStyleSheet("""color: #00409A;
            font-size:12px;
            font-weight: bold;""")
        txt_limite = QLabel("Limite*")
        txt_limite.setStyleSheet("""color: #00409A;
            font-size:12px;
            font-weight: bold;""")
        txt_peso = QLabel("Peso*")
        txt_peso.setStyleSheet("""color: #00409A;
            font-size:12px;
            font-weight: bold;""")
        self.layout_txt_acoes.addStretch(1)
        self.layout_txt_acoes.addWidget(txt_acoes)
        self.layout_txt_acoes.addWidget(txt_limite)
        self.layout_txt_acoes.addWidget(txt_peso)
        self.layout_vertical_organizador.addLayout(self.layout_txt_acoes)
        self.layout_vertical_organizador.addLayout(self.layout_acoes)
        self.setLayout(self.layout_vertical_organizador)
        self.layout_txt_acoes.addStretch(1)
        txt_acoes.setContentsMargins(0,0,180,0)
        txt_limite.setContentsMargins(0,0,180,0)
        txt_peso.setContentsMargins(0,0,0,0)


class tabela(QGridLayout):
    def __init__(self):
        super().__init__()
        Colunas = [
            ("Ações",0,0), ("Limite",0,1),
            ("Peso",0,2), ("Opções",0,3)
        ]
        for texto,colona,linha in Colunas:
            label = QLabel(texto)
            label.setStyleSheet("""color: #00409A;
                font-size:15px;
                font-weight: bold;""")
            self.addWidget(label,colona,linha)
            label.setContentsMargins(45,0,0,0)
        


        tab = QTableWidget()
        tab.setColumnCount(4)
        # Deletar dados ao começar back end
        dados = [("aiaiai","3","4"),("aiaiai","3","4"),("aiaiai","3","4"),
                 ("aiaiai","3","4"),("aiaiai","3","4"),("aiaiai", "3","4")] 
        

        tab.setRowCount(len(dados))
        for linha,(acao,limite,peso) in enumerate(dados):
        
            tab.setItem(linha,0,QTableWidgetItem(acao))
            tab.setItem(linha,1,QTableWidgetItem(limite))
            tab.setItem(linha,2,QTableWidgetItem(peso))
            tab.setCellWidget(linha,3,self.criar_botao())
            
        self.addWidget(tab, 1, 0, 1, 4)
        tab.horizontalHeader().setVisible(False)
        tab.verticalHeader().setVisible(False)
        tab.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) 
        tab.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        tab.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        tab.setColumnWidth(0, 150) 
        tab.setColumnWidth(1, 200) 
        tab.setColumnWidth(2, 150)         
        tab.setColumnWidth(3, 200)
        


    def criar_botao(self):
        btn_editar = QToolButton()
        btn_editar.setIcon(QIcon("Imagens/vector_lapis.png"))
        btn_editar.setIconSize(QSize(20,20))
        btn_editar.setAutoRaise(True)
        
    
        
        btn_excluir = QToolButton()
        btn_excluir.setIcon(QIcon("Imagens/vector_deletar.png"))
        btn_excluir.setIconSize(QSize(20,20))
        btn_editar.setAutoRaise(True)

        

        caixa = QWidget()
        hori_layout = QHBoxLayout(caixa)
        hori_layout.addWidget(caixa)
        hori_layout.addWidget(btn_editar)
        hori_layout.addWidget(btn_excluir)
        hori_layout.setContentsMargins(10,0,10,0)
        hori_layout.setSpacing(10)
        return caixa





    

        

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = popup_editar_ano()
    janela.show()
    sys.exit(app.exec())