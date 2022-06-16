from main_form import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from my_button import MyButton
import random


class MainGame(QMainWindow):

    def __init__(self, parent):
        super().__init__()
        self.clickButton = None
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.parent = parent
        self.firstSpacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding,
                                                 QtWidgets.QSizePolicy.Expanding)
        self.colorList = ['red', 'green', 'white', 'black', 'blue']
        self.labelScore = {}
        i = 0
        for i in range(len(self.colorList)):
            self.labelScore[self.colorList[i]] = 0
        #labellist = ['label_black_score','label_green_score','label_white_score','']
        self.__ui.label_red_score.setText('x' + str(0) + ' Красный')
        self.__ui.label_white_score.setText('x' + str(0) + '  Белый')
        self.__ui.label_black_score.setText('x' + str(0) + ' Чёрный')
        self.__ui.label_blue_score.setText('x' + str(0) + ' Синий')
        self.__ui.label_green_score.setText('x' + str(0) + ' Зелёный')
        count_red = 0
        count_white = 0
        count_black = 0
        count_blue = 0

        #self.label_yellow_score.setText =
        self.score = 0
        self.mult = 1
        self.but_del = 0
        self.end = False
        self.buttons = {}
        self.endClick = False
        self.maxRange = 10
        for i in range(1, self.maxRange):
            label1 = QtWidgets.QLabel('')
            label2 = QtWidgets.QLabel('')
            self.__ui.gridLayout_4.addWidget(label1, 10, i)
            self.__ui.gridLayout_4.addWidget(label2, i, 10)
            for j in range(1, self.maxRange):
                color = self.colorList[random.randrange(len(self.colorList))]
                but_cl = False
                button_ij = MyButton(i, j, color, but_cl, self)
                #button_ij.setText(str(i) + str(j))
                button_ij.setFixedWidth(50)
                button_ij.setFixedHeight(50)
                button_ij.setStyleSheet('background-color:' + color)
                button_ij.clicked.connect(self.buttonIJClick)
                #button_ij_id = str(i) + '_' + str(j)
                self.__ui.gridLayout_4.addWidget(button_ij, i, j)
                self.buttons[i, j] = button_ij

        self.__ui.gridLayout_4.addItem(self.firstSpacer, 0, 0, 1, 1)
        #button1 = QtWidgets.QPushButton("1", self)
        #self.__ui.gridLayout_4.addWidget(button1, 1, 1)
        #button2 = QtWidgets.QPushButton("2", self)
        #self.__ui.gridLayout_4.addWidget(button2, 2, 2)

        self.lastSpacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding,
                                                QtWidgets.QSizePolicy.Expanding)
        self.__ui.gridLayout_4.addItem(self.lastSpacer, 10, 10, 1, 1)
        self.startButton = (1,2)
        self.isStart = False
        self.show()

    def buttonIJClick(self):
        # print(self.sender().x, self.sender().y)
        #self.but_del += 1
        x = self.sender().x
        y = self.sender().y
        if self.isStart == False:
            self.startButton = (x, y)
            self.isStart = True
        if self.endClick == False:
            self.clickButton = (x, y)
            self.endClick = True

        color = self.sender().color
        self.sender().but_cl = True
        if (x - 1, y) in self.buttons:
            b = self.buttons[x - 1, y]
            print(self.sender().x, self.sender().y)
            if (color == b.color) and (b.but_cl == False):
                self.but_del += 1
                b.click()
                self.mult += 1.5


        if (x, y - 1) in self.buttons:
            b = self.buttons[x, y - 1]
            print(self.sender().x, self.sender().y)
            if (color == b.color) and (b.but_cl == False):
                self.but_del += 1
                self.mult += 1.5
                b.click()

        if (x + 1, y) in self.buttons:
            b = self.buttons[x + 1, y]
            print(self.sender().x, self.sender().y)
            if (color == b.color) and (b.but_cl == False):
                self.but_del += 1
                self.mult += 1.5
                b.click()

        if (x, y + 1) in self.buttons:
            b = self.buttons[x, y + 1]
            print(self.sender().x, self.sender().y)
            if (color == b.color) and (b.but_cl == False):
                self.but_del += 1
                self.mult += 1.5
                b.click()

        self.labelScore[self.sender().color] += 1
        if self.but_del >= 1:
            print('Удалён: ' + self.sender().color)
            self.__ui.gridLayout_4.removeWidget(self.sender())
            del self.buttons[self.sender().x, self.sender().y]


        if self.clickButton == (x, y):
            self.endClick = False

            for k in range(1, self.maxRange*2):
                for i in range(1, self.maxRange - 1):
                    for j in range(1, self.maxRange):
                        if ((i, j) in self.buttons) and ((i+1, j) not in self.buttons):
                            self.buttons[i+1, j] = self.buttons[i, j]
                            self.buttons[i + 1, j].x += 1
                            self.__ui.gridLayout_4.addWidget(self.buttons[i + 1, j], i + 1, j)
                            #self.__ui.gridLayout_4.removeWidget(self.buttons[i, j])
                            del self.buttons[i, j]

            isColumn = {}
            for i in range(1, self.maxRange):
                for j in range(1, self.maxRange):
                    if (i, j) in self.buttons:
                        isColumn[j] = True
            for i in range(1, self.maxRange):
                for j in range(1, self.maxRange):
                    if (i, j) in self.buttons:
                        l = 0
                        for k in range(1, j):
                            if k not in isColumn:
                                l += 1
                        if l > 0:
                            self.buttons[i, j - l] = self.buttons[i, j]
                            self.buttons[i, j - l].y -= l
                            self.__ui.gridLayout_4.addWidget(self.buttons[i, j - l], i, j-l)
                            del self.buttons[i, j]
            if self.but_del >= 1:
                self.labelScoreUpdate()
            self.but_del = 0
            self.mult = 1
            if (x, y) in self.buttons:
                self.buttons[x, y].but_cl = False
            if (self.startButton==(x, y)):
                if len(self.buttons) == 0:
                    self.msbox_end()
                self.zero_click()
                self.isStart = False

                        #self.__ui.gridLayout_4.addItem(self.__ui.gridLayout_4.itemAtPosition(i, j), i + 1, j)
                    #    self.__ui.gridLayout_4.removeItem(self.__ui.gridLayout_4.itemAtPosition(i, j))

    def zero_click(self):
        self.end = False
        for but_key in self.buttons:
            but = self.buttons[but_key]
            x = but.x
            y = but.y
            color = but.color
            if (x - 1, y) in self.buttons:
                b = self.buttons[x - 1, y]
                if color == b.color:
                    self.end = True

            if (x, y - 1) in self.buttons:
                b = self.buttons[x, y - 1]
                if color == b.color:
                    self.end = True

            if (x + 1, y) in self.buttons:
                b = self.buttons[x + 1, y]
                if color == b.color:
                    self.end = True

            if (x, y + 1) in self.buttons:
                b = self.buttons[x, y + 1]
                if color == b.color:
                    self.end = True

        if self.end == False:
            self.msbox_end()

    def msbox_end(self):

            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Игра закончена. Попробовать снова?")
            msgBox.setWindowTitle("Конец игры.")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            # msgBox.buttonClicked.connect(self.msgButtonClick)

            returnValue = msgBox.exec()
            if returnValue == QtWidgets.QMessageBox.Yes:
                self.reset()
            else:
                #self.Ui_MainWindow.setVisible(True)
                self.parent.show()
                self.close()

    def reset(self):
        for but in self.buttons:
            self.__ui.gridLayout_4.removeWidget(self.buttons[but])
        self.buttons.clear()
        for i in range(1, self.maxRange):
            for j in range(1, self.maxRange):
                # number += 1
                color = self.colorList[random.randrange(len(self.colorList))]
                but_cl = False
                button_ij = MyButton(i, j, color, but_cl, self)
                # button_ij.setText(str(i))
                button_ij.setFixedWidth(50)
                button_ij.setFixedHeight(50)
                button_ij.setStyleSheet('background-color:' + color)
                button_ij.clicked.connect(self.buttonIJClick)
                # button_ij_id = str(i) + '_' + str(j)
                self.__ui.gridLayout_4.addWidget(button_ij, i, j)
                self.buttons[i, j] = button_ij

                self.__ui.label_red_score.setText('x' + str(0) + ' Красный')
                self.__ui.label_white_score.setText('x' + str(0) + '  Белый')
                self.__ui.label_black_score.setText('x' + str(0) + ' Чёрный')
                self.__ui.label_blue_score.setText('x' + str(0) + ' Синий')
                self.score = 0
                self.__ui.label_score.setText(str(self.score))

    def labelScoreUpdate(self):
        self.score += 100 * self.mult
        self.__ui.label_score.setText(str(self.score))
        #'''
        if self.labelScore["red"] != 0:
            self.__ui.label_red_score.setText('x' + str(self.labelScore["red"]) + ' Красный')
        if self.labelScore["white"] != 0:
            self.__ui.label_white_score.setText('x' + str(self.labelScore["white"]) + ' Белый')
        if self.labelScore["black"] != 0:
            self.__ui.label_black_score.setText('x' + str(self.labelScore["black"]) + ' Чёрный')
        if self.labelScore["blue"] != 0:
            self.__ui.label_blue_score.setText('x' + str(self.labelScore["blue"]) + ' Синий')
        if self.labelScore["green"] != 0:
            self.__ui.label_green_score.setText('x' + str(self.labelScore["green"]) + ' Зелёный')


# '''
