import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, qApp, QAction, QFileDialog)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NiseTaiga - skr47ch")
        self.statusBar().showMessage("This is a status bar")
        self.setGeometry(50, 50, 400, 200)
        self.create_menu()

    def create_menu(self):
        """Creates the menu bar and its  sub-menus"""

        menu_bar = self.menuBar()

        # Main menu items
        file_menu = menu_bar.addMenu('File')
        services_menu = menu_bar.addMenu('Services')
        tool_menu = menu_bar.addMenu('Tool')
        view_menu = menu_bar.addMenu('View')
        help_menu = menu_bar.addMenu('Help')

        # File menu items
        lib_folders = file_menu.addMenu('Library Folders')
        new_folder = QAction('Add new folder...', self)
        new_folder.triggered.connect(self.show_dialogue)
        lib_folders.addAction(new_folder)

        file_menu.addAction('Scan available episodes')

        file_menu.addSeparator()

        next_episode = QAction('Play next episode', self)
        next_episode.setShortcut('Ctrl+N')
        file_menu.addAction(next_episode)

        random_anime = QAction('Play random anime',  self)
        random_anime.setShortcut('Ctrl+R')
        file_menu.addAction(random_anime)

        file_menu.addSeparator()

        exit_action = QAction('Exit', self)
        exit_action.setStatusTip('Exit  Program')
        exit_action.triggered.connect(qApp.quit)

        file_menu.addAction(exit_action)

    def show_dialogue(self):
        QFileDialog.getOpenFileName(self, 'Add a library folder', 'C:/Users/skr47ch/Documents')


if __name__ == "__main__":
    app = QApplication([])
    window = Example()
    window.show()
    sys.exit(app.exec_())
