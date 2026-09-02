import sys

from PySide6.QtWidgets import QApplication

from popup_relatorio import PopupRelatorio


app = QApplication(sys.argv)

popup = PopupRelatorio()
popup.show()

sys.exit(app.exec())