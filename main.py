import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Игрушка")
    window.setGeometry(300, 250, 800, 600)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Кликомания")
    main_text.move(400, 300)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
    #123