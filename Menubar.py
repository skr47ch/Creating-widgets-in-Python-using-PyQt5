from functools import partial
import external_links as links
from PyQt5.QtWidgets import (qApp, QAction, QFileDialog,
                             QActionGroup, QDialog)


def create_menu(parent):
    menu_bar = parent
    menu_file(menu_bar)
    menu_services(menu_bar)
    menu_tools(menu_bar)
    menu_view(menu_bar)
    menu_help(menu_bar)


def menu_file(menu_bar):
    file_menu = menu_bar.addMenu('File')

    lib_folders = file_menu.addMenu('Library Folders')
    new_folder = QAction('Add new folder...', menu_bar)
    new_folder.triggered.connect(show_dialogue)
    lib_folders.addAction(new_folder)

    file_menu.addAction('Scan available episodes')

    file_menu.addSeparator()

    next_episode = QAction('Play next episode', menu_bar)
    next_episode.setShortcut('Ctrl+N')
    file_menu.addAction(next_episode)

    random_anime = QAction('Play random anime', menu_bar)
    random_anime.setShortcut('Ctrl+R')
    file_menu.addAction(random_anime)

    file_menu.addSeparator()

    exit_action = QAction('Exit', menu_bar)
    exit_action.setStatusTip('Exit  Program')
    exit_action.triggered.connect(qApp.quit)
    file_menu.addAction(exit_action)


def menu_services(menu_bar):
    services_menu = menu_bar.addMenu('Services')

    synchronize = QAction('Synchronize list', menu_bar)
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


def menu_tools(menu_bar):
    tool_menu = menu_bar.addMenu('Tool')

    export_anime = tool_menu.addMenu('Export anime list')
    export_anime.addAction('Export as markdown')
    export_anime.addAction('Export as MyAnimeList XML...')

    ext_links = tool_menu.addMenu('External links')
    hibari, malgraph, anichart, monthly_moe, senpai_anime_charts, anime_streaming_search_engine, the_fansub_database = None, None, None, None, None, None, None
    var_list = [hibari, malgraph, anichart, monthly_moe, senpai_anime_charts, anime_streaming_search_engine, the_fansub_database]
    var_labels = ['Hibari', 'MALGraph', 'Anichart', 'Monthly.moe', 'Senpai Anime Charts', 'Anime Streaming Search Engine', 'The Fansub Database']
    var_links = ['hibari', 'malgraph', 'anichart', 'monthly_moe', 'senpai_anime_charts', 'anime_streaming_search_engine', 'the_fansub_database']
    for var, label, link in zip(var_list, var_labels, var_links):
        var = QAction(label, menu_bar)
        var.triggered.connect(partial(links.OpenLink, link))
        ext_links.addAction(var)

    for index_ in [2, 6]:
        ext_links.insertSeparator(ext_links.actions()[index_])

    tool_menu.addSeparator()
    enable_recognition = QAction('Enable anime recognition', menu_bar)
    enable_recognition.setCheckable(True)
    tool_menu.addAction(enable_recognition)
    enable_sharing = QAction('Enable auto sharing', menu_bar)
    enable_sharing.setCheckable(True)
    tool_menu.addAction(enable_sharing)
    enable_sync = QAction('Enable auto synchronization', menu_bar)
    enable_sync.setCheckable(True)
    tool_menu.addAction(enable_sync)
    tool_menu.addSeparator()
    tool_menu.addAction('Settings')


def menu_view(menu_bar):
    view_menu = menu_bar.addMenu('View')

    view_radio_group = QActionGroup(menu_bar)
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

    view_sidebar = QAction('Show sidebar', menu_bar)
    view_sidebar.setCheckable(True)
    view_sidebar.setChecked(True)
    view_menu.addAction(view_sidebar)


def menu_help(menu_bar):
    help_menu = menu_bar.addMenu('Help')

    about = QAction('About Taiga', menu_bar)
    about.triggered.connect(show_about_page)
    help_menu.addAction(about)

    help_support = QAction('Support', menu_bar)
    help_support.setShortcut('F1')
    help_menu.addAction(help_support)

    help_menu.addSeparator()

    help_menu.addAction('Check for updates')


def show_dialogue(self):
    """Opens a file dialogue to browse to a file location"""
    QFileDialog.getOpenFileName(self, 'Add a library folder', 'C:/Users/skr47ch/Documents')


def show_about_page():
    """About Page for the application"""
    about_page = QDialog()
    about_page.setWindowTitle('About Taiga')
    about_page.exec_()

