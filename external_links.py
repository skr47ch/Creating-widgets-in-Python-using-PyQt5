import webbrowser

link_dict = {'hibari': 'https://hibari.moe/',
             'malgraph': 'http://graph.anime.plus/',
             'anichart': 'https://anichart.net/airing',
             'monthly_moe': 'https://www.monthly.moe/weekly',
             'senpai_anime_charts': 'http://www.senpai.moe/?mode=calendar',
             'anime_streaming_search_engine': 'https://because.moe/',
             'the_fansub_database': 'https://fansubdb.com/',
             'help_support': 'https://taiga.moe/#support'
             }


class OpenLink:
    def __init__(self, exlink):
        # print(link_dict[exlink])
        webbrowser.open(link_dict[exlink], new=2)


if __name__ == '__main__':
    link = OpenLink('malgraph')
