from typing import List
from models.player import Player
# from models.tournament import Tournament
from views.main_menu_view import MainMenuView

from controllers.base_controller import BaseController
from controllers.manage_tournament_controller import ManageTournament
from controllers.manage_player_controller import ManagePlayer
from controllers.quit_controller import QuitController

# from const import *

from tinydb import TinyDB

from os.path import exists


class MainController(BaseController):

    def __init__(self):
        # models
        self.players: List[Player] = []  # a mettre dans le modèle
        self.tournament: List[Player] = []  # a mettre dans le modèle
        self.management_tournament_controller = ManageTournament(self)
        self.manage_player_controller = ManagePlayer(self)
        self.quit_controller = QuitController()

        # Coder les méthodes
        menu_options = {1: [self.management_tournament_controller.run, 'Gérer les tournois'],
                        2: [self.manage_player_controller.run, 'Gérer les joueurs'],
                        3: [self.quit_controller.run, 'Quitter'],
                        }
        super().__init__(menu_options, MainMenuView())

        if not exists('./data/ocr3_db.json'):
            db = TinyDB('./data/ocr3_db.json')
            players_table = db.table('players')
            players_table.truncate()
            tournament_table = db.table('tournaments')
            tournament_table.truncate()
