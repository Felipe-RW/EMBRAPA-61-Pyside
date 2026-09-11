import sys
from PySide6.QtWidgets import QApplication
from Telas.modelo_tela_administrador_painel_principal import ModeloTelaAdministrador

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ModeloTelaAdministrador()
    janela.showMaximized()
    sys.exit(app.exec())
