import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_game import MainGame

class Window(QMainWindow):
    def __init__(self):
        x_main = 800
        y_main = 600
        super(Window, self).__init__()
        self.setWindowTitle("Игрушка")
        self.setFixedSize(x_main, y_main)
       #self.setGeometry(300, 250, x_main, y_main)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Кликомания")
        self.main_text.setFont(QtGui.QFont("Times", 32, QtGui.QFont.Bold))
        self.main_text.move(250, 100)
        self.main_text.adjustSize()

        self.btn_startplay = QtWidgets.QPushButton(self)
        self.btn_startplay.move(x_main//2 - 100, y_main//2 - 100)
        self.btn_startplay.setText("Играть")
        self.btn_startplay.setFixedWidth(200)
        self.btn_startplay.setFixedHeight(50)
        self.btn_startplay.clicked.connect(self.play_main)

        self.btn_opt = QtWidgets.QPushButton(self)
        self.btn_opt.move(x_main // 2 - 100, y_main // 2 - 50)
        self.btn_opt.setText("Настройки")
        #self.btn_opt.clicked.connect(self.opt_main)
        self.btn_opt.setFixedWidth(200)
        self.btn_opt.setFixedHeight(50)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.move(x_main//2 - 100, y_main//2)
        self.btn_exit.setText("Выход")
        self.btn_exit.clicked.connect(self.exit_main)
        self.btn_exit.setFixedWidth(200)

    def exit_main(self):
       sys.exit()

    def play_main(self):
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