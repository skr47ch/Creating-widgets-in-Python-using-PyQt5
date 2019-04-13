import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QDesktopWidget
import Menubar

MENU_HEIGHT = 25
RIBBON_HEIGHT = 40
PANEL_WIDTH = 175

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
        window_size = QDesktopWidget().screenGeometry(-1)

        menu_bar = self.menuBar()
        Menubar.create_menu(menu_bar)

        # Top Ribbon
        ribbon = QFrame(self)
        ribbon.move(0, MENU_HEIGHT)
        ribbon.resize(window_size.width(), RIBBON_HEIGHT)
        ribbon.setStyleSheet('background-color: gray')

        # Left Pane
        left = QFrame(self)
        left.move(0, RIBBON_HEIGHT+MENU_HEIGHT)
        left.resize(PANEL_WIDTH, window_size.height())
        left.setStyleSheet('background-color: yellow')

        # Display Window
        right = QFrame(self)
        right.move(PANEL_WIDTH, RIBBON_HEIGHT+MENU_HEIGHT)
        right.resize(window_size.width(), window_size.height())
        right.setStyleSheet('background-color: pink')

def main():
    app = QApplication([sys.argv])
    root = App()
    root.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
