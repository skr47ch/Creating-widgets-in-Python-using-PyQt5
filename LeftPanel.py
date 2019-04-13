from PyQt5.QtWidgets import QFrame, QApplication, QWidget, QDesktopWidget

RIBBON_HEIGHT = 50
PANEL_WIDTH = 175

class LeftPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1600, 1200)
        window_size = QDesktopWidget().screenGeometry(-1)

        # Top Ribbon
        ribbon = QFrame(self)
        ribbon.resize(window_size.width(), RIBBON_HEIGHT)
        ribbon.setStyleSheet('background-color: green')

        # Left Pane
        left = QFrame(self)
        left.resize(PANEL_WIDTH, window_size.height())
        left.setStyleSheet('background-color: yellow')


def main():
    app = QApplication([])
    panel = LeftPanel()
    panel.show()
    app.exec_()


if __name__ == '__main__':
    main()
