
from typing import List
from models.player import Player
from models.tournament import Tournament

from views.tournament_view import TournamentView
 
from const import *

class ManageTournament:

    def __init__(self):
        # models
        self.tournament: List[Player] = []
        # views
        self.view = TournamentView()
        self.parent_controller = None
        
        self.update_menu_option()
                

    def update_menu_option(self):
        self.menu_options={1:[None,'Créer un tournoi'],
                                2:[None,'Charger un tournoi'],
                                3:[None,'Voir un tournoi'],
                                4:[None,'Supprimer un tournoi'],
                                5:[self.parent_controller,'Revenir au menu principal'],
                            }    
    def get_players(self):
        while len(self.players) < NB_MAX_JOUEUR:  # nombre magique
            family_name,first_name,birth_date,gender,rank = self.view.prompt_for_player(len(self.players)+1)
            player = Player(family_name,first_name,birth_date,gender,rank)
            self.players.append(player)


    def run(self,parent_controller):
        self.parent_controller = parent_controller
        self.update_menu_option()
        choix_menu = self.view.show_menu(self.menu_options)
        next_step = self.menu_options[choix_menu][0] #choix_menu est un controller qui sera appelé ensuite
        next_step.run(self)