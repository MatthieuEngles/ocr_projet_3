from views.menu_view import MenuView


class QuitView(MenuView):

    def show_quit(self):
        self.clear()
        print('Merci et au revoir')
