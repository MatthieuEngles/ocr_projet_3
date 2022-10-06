from views.quit_view import QuitView


class QuitController:

    
    def __init__(self):
        self.text = 'Quitter'
        self.view = QuitView()
        
    def run(self,parent_controller):
        self.view.show_quit()
  
        
        

