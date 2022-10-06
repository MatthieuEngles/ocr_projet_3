"""Define the main controller."""

from typing import List
from models.player import Player
from models.tournament import Tournament
from models.main import Main
from views.main_menu_view import MainMenuView


from controllers.manage_tournament_controller import ManageTournament
from controllers.manage_player_controller import ManagePlayer
from controllers.quit_controller import QuitController

from const import *

class MainController:
    """Main controller."""

    
    def __init__(self):
        """Has a deck, a list of players and a view."""
        
        #manage database
        
        # models
        self.players: List[Player] = [] # a mettre dans le modèle
        self.tournament: List[Player] = [] # a mettre dans le modèle
        # views
        self.view = MainMenuView()
        self.management_tournament_controller = ManageTournament()
        self.manage_player_controller = ManagePlayer()
        self.quit_controller = QuitController()

        
        #Coder les méthodes
        self.menu_options={1: [self.management_tournament_controller,'Gérer les tournois'],#'Gérer les tournois', #mettre le nom de la méthode !! 
                           2: [self.manage_player_controller,'Gérer les joueurs'],
                           3:[self.quit_controller,'Quitter'],
                           }

        
        # systeme de génération de paires
        # self.generate_pairs_algorythm = generate_pairs_algorythm

    def get_players(self):
        while len(self.players) < NB_MAX_JOUEUR:  # nombre magique
            family_name,first_name,birth_date,gender,rank = self.view.prompt_for_player(len(self.players)+1)
            player = Player(family_name,first_name,birth_date,gender,rank)
            self.players.append(player)


    def run(self,parent_controller = None):
        choix_menu = None 
        choix_menu = self.view.show_menu(self.menu_options)
        next_step = self.menu_options[choix_menu][0] #choix_menu est un controller qui sera appelé ensuite
        next_step.run(self) #faire appel avec une référence à self, 
            
