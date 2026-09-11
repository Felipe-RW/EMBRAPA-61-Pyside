import sys

from PySide6.QtWidgets import QApplication

from popup_relatorio import PopupRelatorio


from PySide6.QtWidgets import QLineEdit

app = QApplication(sys.argv)

popup = PopupRelatorio()
popup.show()

sys.exit(app.exec())