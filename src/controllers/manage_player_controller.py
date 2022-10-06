"""Define the main controller."""

from typing import List
from models.player import Player
from models.tournament import Tournament

from views.player_view import PlayerView


from const import *

class ManagePlayer:
    """Main controller."""

    
    def __init__(self):       
        # models
        self.players: List[Player] = []
        # views
        self.view = PlayerView()
        
        
        self.parent_controller = None
        self.update_menu_option()                    
        
    def update_menu_option(self): #[controller, texte à afficher]
        self.menu_options={1:[None,'Créer un joueur'],
                        2:[None,'Voir un joueur'],
                        3:[None,'Supprimer un joueur'],
                        4:[self.parent_controller,'Revenir au meun précedent'],
                    }

    def get_players(self):
        while len(self.players) < NB_MAX_JOUEUR:  # nombre magique
            family_name,first_name,birth_date,gender,rank = self.view.prompt_for_player(len(self.players)+1)
            player = Player(family_name,first_name,birth_date,gender,rank)
            self.players.append(player)


    def run(self, parent_controller):
        self.parent_controller = parent_controller
        self.update_menu_option() #pkoi cette ligne
        choix_menu = self.view.show_menu(self.menu_options)
        next_step = self.menu_options[choix_menu][0] #choix_menu est un controller qui sera appelé ensuite
        next_step.run(self)