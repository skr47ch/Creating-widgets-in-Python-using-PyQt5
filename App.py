import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import Menubar
# import LeftPanel as panel


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Nise Taiga - username"
        self.left = 20
        self.top = 60
        self.width = 640
        self.height = 400
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.menu_bar = self.menuBar()
        Menubar.create_menu(self.menu_bar)


def main():
    app = QApplication([sys.argv])
    root = App()
    root.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
