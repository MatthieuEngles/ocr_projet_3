"""Define the main controller."""

from typing import List
from models.player import Player
from views.player_view import PlayerView
from views.main_view import MainView

from const import *

class MainController:
    """Main controller."""

    
    def __init__(self):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        
        # views
        self.player_view = PlayerView()
        self.main_view = MainView()
        
        
            #Coder les méthodes
        menu_principal_options={1:manage_tournament_controller,#'Gérer les tournois', #mettre le nom de la méthode
                           2:'Gérer les joueurs',
                           3:'Quitter'
                           }
        
        
        
        # systeme de génération de paires
        # self.generate_pairs_algorythm = generate_pairs_algorythm

    def get_players(self):
        while len(self.players) < NB_MAX_JOUEUR:  # nombre magique
            family_name,first_name,birth_date,gender,rank = self.view.prompt_for_player(len(self.players)+1)
            player = Player(family_name,first_name,birth_date,gender,rank)
            self.players.append(player)


    def run(self):
        choix_menu = None 
        while choix_menu != 8: #quitter
            choix_menu = menu_principal_options[self.main_view.show_main_menu()] #choix_menu est un controller qui sera appelé ensuite
            choix_menu.show_menu()
            
            #faire un controller pour chaque item
            if choix_menu == 5:
                #ajout d'un joueur
                data = self.player_view.prompt_player()
                player = Player(*data)
                self.players.append(player)
            if choix_menu == 6:
                #vue d'un joueur
                for p in self.players:
                    self.player_view.show_player(p)

    # def run(self):
    #     self.get_players()

    #     running = True
    #     while running:
    #         self.start_game()

    #         for player in self.players:
    #             self.view.show_player_hand(player.name, player.hand)

    #         self.view.prompt_for_flip_cards()

    #         for player in self.players:
    #             for card in player.hand:
    #                 card.is_face_up = True
    #             self.view.show_player_hand(player.name, player.hand)

    #         self.view.show_winner(self.evaluate_game())

    #         running = self.view.prompt_for_new_game()
    #         self.rebuild_deck()
