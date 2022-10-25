from views.quit_view import QuitView

from controllers.base_controller import BaseController

class QuitController():

    
    def __init__(self):
        self.view = QuitView()
        
    def run(self):
        self.view.show_quit()
        return True
        
        

