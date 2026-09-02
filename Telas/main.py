import sys
from PySide6.QtWidgets import QApplication
from popup_de_aviso_de_ano_criado import PopupDeAvisoDeAnoCriado

def main():
    app = QApplication(sys.argv)
    
    janela = PopupDeAvisoDeAnoCriado()
    janela.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()