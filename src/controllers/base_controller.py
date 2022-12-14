class BaseController:

    def __init__(self, menu_options=None, view=None):
        self.menu_options = menu_options
        self.view = view

    def run(self):
        choix_menu = self.view.show_menu(self.menu_options)  # la vue doit avoir une méthode show_menu
        # choix_menu.run est la méthode de d'appel d'un controller qui sera appelé ensuite
        next_step = self.menu_options[choix_menu][0]
        next_step()
