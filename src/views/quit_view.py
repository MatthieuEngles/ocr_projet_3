import os
from datetime import datetime
clear = lambda: os.system('clear')


class QuitView:

    def show_quit(self):
        clear()
        print('Merci et au revoir')
    