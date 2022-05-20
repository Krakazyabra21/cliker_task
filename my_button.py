from PyQt5.QtWidgets import QPushButton

class MyButton(QPushButton):
    def __init__(self, x, y, color, but_cl, parent):
        super(MyButton, self).__init__(parent)
        self.x = x
        self.y = y
        self.color = color
        self.but_cl = but_cl

