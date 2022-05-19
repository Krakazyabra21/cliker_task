import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_game import MainGame

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Игрушка")
        self.setGeometry(300, 250, 800, 600)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Кликомания")
        self.main_text.setFont(QtGui.QFont("Times", 32, QtGui.QFont.Bold))
        self.main_text.move(250, 100)
        self.main_text.adjustSize()

        self.btn_startplay = QtWidgets.QPushButton(self)
        self.btn_startplay.move(300, 200)
        self.btn_startplay.setText("Мяу")
        self.btn_startplay.setFixedWidth(200)
        self.btn_startplay.clicked.connect(self.play_but)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.move(300, 250)
        self.btn_exit.setText("Exit")
        self.btn_exit.clicked.connect(self.exit_main)
        self.btn_exit.setFixedWidth(200)

    def exit_main(self):
       sys.exit()

    def play_but(self):
        self.setVisible(False)
        self.mainWindow = MainGame()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
    #123