import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class Window(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Python Menus &amp; Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createMenuBar()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        File = menuBar.addMenu("File")
        menuBar.addMenu(File)
        edit = menuBar.addMenu("Edit")
        menuBar.addMenu(edit)
        helpM =menuBar.addMenu("Help")
        menuBar.addMenu(helpM)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    #123