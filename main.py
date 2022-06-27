import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_game import MainGame

class Window(QMainWindow):
    def __init__(self):
        self.list_mas = [' ', '640x480', '800x600', '1280x800']
        self.x_main = 640
        self.y_main = 480
        super(Window, self).__init__()
        self.setWindowTitle("Игрушка")
        self.setFixedSize(self.x_main, self.y_main)
       #self.setGeometry(300, 250, x_main, y_main)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Кликомания")
        self.main_text.setFont(QtGui.QFont("Times", 32, QtGui.QFont.Bold))
        self.main_text.move(self.x_main//2-140, 75)
        self.main_text.adjustSize()

        self.btn_startplay = QtWidgets.QPushButton(self)
        self.btn_startplay.move(self.x_main//2 - 100, self.y_main//2 - 100)
        self.btn_startplay.setText("Играть")
        self.btn_startplay.setFixedWidth(200)
        self.btn_startplay.setFixedHeight(50)
        self.btn_startplay.clicked.connect(self.play_main)

        self.btn_opt = QtWidgets.QPushButton(self)
        self.btn_opt.move(self.x_main // 2 - 100, self.y_main // 2 - 50)
        self.btn_opt.setText("Настройки")
        self.btn_opt.clicked.connect(self.opt_main)
        self.btn_opt.setFixedWidth(200)
        self.btn_opt.setFixedHeight(50)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.move(self.x_main//2 - 100, self.y_main//2)
        self.btn_exit.setText("Выход")
        self.btn_exit.clicked.connect(self.exit_main)
        self.btn_exit.setFixedWidth(200)

        self.btn_bmenu = QtWidgets.QPushButton(self)
        self.btn_bmenu.move(self.x_main - 150, self.y_main - 50)
        self.btn_bmenu.setText("В меню")
        self.btn_bmenu.clicked.connect(self.b_menu)
        self.btn_bmenu.setVisible(False)

        self.comb_s = QtWidgets.QComboBox(self)
        self.comb_s.setVisible(False)
        self.comb_s.setFixedSize(200, 30)
        self.comb_s.move(self.x_main//2 - 100, self.y_main//2 - 30)
        self.comb_s.addItems(self.list_mas)
        self.lab_comb = QtWidgets.QLabel(self)
        self.lab_comb.move(self.x_main//2 - 100, self.y_main//2 - 50)
        self.lab_comb.setText("Выберите разрешение экрана:")
        self.lab_comb.adjustSize()
        self.lab_comb.setVisible(False)

        self.btn_acc = QtWidgets.QPushButton(self)
        self.btn_acc.move(self.x_main//2, self.y_main - 50)
        self.btn_acc.setText("Принять")
        self.btn_acc.setVisible(False)
        self.btn_acc.clicked.connect(self.change_size)

    def change_size(self):
        id_list = self.comb_s.currentIndex()
        if id_list == 1:
            self.x_main = 640
            self.y_main = 480
            self.setFixedSize(self.x_main, self.y_main)
        if id_list == 2:
            self.x_main = 800
            self.y_main = 600
            self.setFixedSize(self.x_main, self.y_main)
        if id_list == 3:
            self.x_main = 1280
            self.y_main = 800
            self.setFixedSize(self.x_main, self.y_main)
        self.main_text.move(self.x_main // 2 - 140, 75)
        self.btn_startplay.move(self.x_main // 2 - 100, self.y_main // 2 - 100)
        self.btn_opt.move(self.x_main // 2 - 100, self.y_main // 2 - 50)
        self.btn_exit.move(self.x_main // 2 - 100, self.y_main // 2)
        self.btn_bmenu.move(self.x_main - 150, self.y_main - 50)
        self.comb_s.move(self.x_main // 2 - 100, self.y_main // 2 - 30)
        self.lab_comb.move(self.x_main // 2 - 100, self.y_main // 2 - 50)
        self.btn_acc.move(self.x_main//2, self.y_main - 50)

    def play_main(self):
        self.setVisible(False)
        self.mainWindow = MainGame(self)

    def exit_main(self):
       sys.exit()

    def opt_main(self):
        self.main_text.setVisible(False)
        self.btn_startplay.setVisible(False)
        self.btn_opt.setVisible(False)
        self.btn_exit.setVisible(False)
        self.lab_comb.setVisible(True)
        self.btn_bmenu.setVisible(True)
        self.comb_s.setVisible(True)
        self.btn_acc.setVisible(True)

    def b_menu(self):
        self.setVisible(True)
        self.main_text.setVisible(True)
        self.btn_startplay.setVisible(True)
        self.btn_opt.setVisible(True)
        self.btn_exit.setVisible(True)
        self.lab_comb.setVisible(False)
        self.btn_bmenu.setVisible(False)
        self.comb_s.setVisible(False)
        self.btn_acc.setVisible(False)

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()