from main_form import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from my_button import MyButton
import random

class MainGame(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.firstSpacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding,
                                                 QtWidgets.QSizePolicy.Expanding)
        colorList = ['red', 'green', 'white', 'black', 'blue']
        self.buttons = {}
        for i in range(1, 9):
            for j in range(1, 9):
                #number += 1
                color = colorList[random.randrange(0, 5)]
                but_cl = False
                button_ij = MyButton(i, j, color, but_cl, self)
                #button_ij.setText(str(i))
                button_ij.setFixedWidth(50)
                button_ij.setFixedHeight(50)
                button_ij.setStyleSheet('background-color:'+color)
                button_ij.clicked.connect(self.buttonIJClick)
                #button_ij_id = str(i) + '_' + str(j)
                self.__ui.gridLayout_4.addWidget(button_ij, i, j)
                self.buttons[i, j] = button_ij

        self.__ui.gridLayout_4.addItem(self.firstSpacer, 0, 0, 1, 1)
        # button1 = QtWidgets.QPushButton("1", self)
        # self.__ui.gridLayout_4.addWidget(button1, 1, 1)
        # button2 = QtWidgets.QPushButton("2", self)
        # self.__ui.gridLayout_4.addWidget(button2, 2, 2)

        self.lastSpacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding,
                                                QtWidgets.QSizePolicy.Expanding)
        self.__ui.gridLayout_4.addItem(self.lastSpacer, 10, 10, 1, 1)

        self.show()

    def buttonIJClick(self):
        #print(self.sender().x, self.sender().y)
        x = self.sender().x
        y = self.sender().y
        color = self.sender().color

        if (x > 1):
            b = self.buttons[x-1, y]
            print(self.sender().x, self.sender().y)
            if color == b.color:
                self.sender().but_cl = True
                '''
                if d not in press:
                    press[H_press] = {d: {b.x, b.y}}
                    H_press += 1
                    d += 1
                    #b.click()
                    print(press)
                
                '''
        '''
        if (y > 1):
            b = self.buttons[x, y - 1]
            if color == b.color:
                b.click()

        if (x < 8):
            b = self.buttons[x + 1, y]
            if color == b.color:
                b.click()

        if (y < 8):
            b = self.buttons[x, y + 1]
            if color == b.color:
                b.click()
        '''
        #'''
        for i in range(1, 9):
            for j in range(1,9):
               # print(i, j)
                if self.sender().but_cl == True:
                     self.__ui.gridLayout_4.removeWidget(self)
                     del self.buttons[i, j]
            #print('Удалён: ' + self.sender().color)
       # for i in range(1, 9):
       #     for j in range(1, 9):
#'''

