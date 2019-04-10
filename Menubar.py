import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             qApp, QAction, QFileDialog,
                             QActionGroup, QDialog)


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

        # Services menu items
        synchronize = QAction('Synchronize list', self)
        synchronize.setShortcut('Ctrl+S')
        services_menu.addAction(synchronize)
        services_menu.addSeparator()
        anilist = services_menu.addMenu('Anilist')
        anilist.addAction('Go to my profile')
        anilist.addAction('Go to my stats')
        kitsu = services_menu.addMenu('Kitsu')
        kitsu.addAction('Go to my feed')
        kitsu.addAction('Go to my library')
        kitsu.addAction('Go to my profile')
        mal = services_menu.addMenu('MyAnimeList')
        mal.addAction('Go to my panel')
        mal.addAction('Go to my profile')
        mal.addAction('Go to my history')

        # Tools menu items
        export_anime = tool_menu.addMenu('Export anime list')
        export_anime.addAction('Export as markdown')
        export_anime.addAction('Export as MyAnimeList XML...')
        ext_links = tool_menu.addMenu('External links')
        ext_links.addAction('Hibari')
        ext_links.addAction('MALgraph')
        ext_links.addSeparator()
        ext_links.addAction('Anichart')
        ext_links.addAction('Monthly.moe')
        ext_links.addAction('Senpai Anime Charts')
        ext_links.addSeparator()
        ext_links.addAction('Anime Streaming Search Engine')
        ext_links.addAction('The Fansub Database')
        tool_menu.addSeparator()
        enable_recognition = QAction('Enable anime recognition', self)
        enable_recognition.setCheckable(True)
        tool_menu.addAction(enable_recognition)
        enable_sharing = QAction('Enable auto sharing', self)
        enable_sharing.setCheckable(True)
        tool_menu.addAction(enable_sharing)
        enable_sync = QAction('Enable auto synchronization', self)
        enable_sync.setCheckable(True)
        tool_menu.addAction(enable_sync)
        tool_menu.addSeparator()
        tool_menu.addAction('Settings')

        # View menu items
        view_radio_group = QActionGroup(self)
        view_radio_group.setExclusive(True)
        view_now_playing = view_radio_group.addAction('Now Playing')
        view_now_playing.setCheckable(True)
        view_now_playing.setChecked(True)
        view_menu.addAction(view_now_playing)
        view_animelist = view_radio_group.addAction('Anime List')
        view_animelist.setCheckable(True)
        view_menu.addAction(view_animelist)
        view_history = view_radio_group.addAction('History')
        view_history.setCheckable(True)
        view_menu.addAction(view_history)
        view_statistics = view_radio_group.addAction('Statistics')
        view_statistics.setCheckable(True)
        view_menu.addAction(view_statistics)
        view_search = view_radio_group.addAction('Search')
        view_search.setCheckable(True)
        view_menu.addAction(view_search)
        view_seasons = view_radio_group.addAction('Seasons')
        view_seasons.setCheckable(True)
        view_menu.addAction(view_seasons)
        view_torrents = view_radio_group.addAction('Torrents')
        view_torrents.setCheckable(True)
        view_menu.addAction(view_torrents)
        view_menu.addSeparator()
        view_sidebar = QAction('Show sidebar', self)
        view_sidebar.setCheckable(True)
        view_sidebar.setChecked(True)
        view_menu.addAction(view_sidebar)

        # Help menu items
        about = QAction('About Taiga', self)
        about.triggered.connect(self.show_about_page)
        help_menu.addAction(about)
        help_menu.addAction('Support')
        help_menu.addSeparator()
        help_menu.addAction('Check for updates')

    def show_dialogue(self):
        """Opens a file dialogue to browse to a file location"""
        QFileDialog.getOpenFileName(self, 'Add a library folder', 'C:/Users/skr47ch/Documents')

    @staticmethod
    def show_about_page():
        """About Page for the application"""
        about_page = QDialog()
        about_page.setWindowTitle('About Taiga')
        about_page.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = Example()
    window.show()
    sys.exit(app.exec_())
