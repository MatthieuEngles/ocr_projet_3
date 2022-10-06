from views.menu_view import MenuView
import os
clear = lambda: os.system('clear')


class MainMenuView(MenuView):
    
    def __init__(self):
        super().__init__()    
    