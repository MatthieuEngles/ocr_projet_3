from models.player import Player
from models.tournament import Tournament
# from models.turn import Turn
# from models.match import Match
from views.tournament_view import TournamentView
# from const import *

from controllers.base_controller import BaseController


class ManageTournament(BaseController):

    def __init__(self, parent_controller):
        # models
        self.tournament_model = Tournament()
        self.player_model = Player()
        # views
        menu_options = {1: [self.add_tournament, 'Créer un tournoi'],
                        2: [self.play_tournament, 'Jouer un tournoi'],
                        3: [self.show_tournament, 'Voir un tournoi'],
                        4: [self.remove_tournament, 'Supprimer un tournoi'],
                        6: [parent_controller.run, 'Revenir au menu principal'],
                        }

        super().__init__(menu_options, TournamentView())

    # def create_turn(self,)

    def add_tournament(self):
        nb_joueur_en_base = self.player_model.get_count()
        if nb_joueur_en_base < 8:
            self.view.prompt_not_enough_player(nb_joueur_en_base)
        else:
            all_player = self.player_model.get_all_player()
            tournament_info = self.view.prompt_tournament(all_player)
            tournament = self.tournament_model.serialize(*tournament_info)
            id = self.tournament_model.add_to_base(tournament)
            self.view.confirm_add_tournament(id)
        self.run()  # on retourne au menu

    # def generate_next_turn(self):

    # def play_random(self,turn)

    def play_tournament(self):
        list_ids = self.tournament_model.get_list_id()
        tournament_id = self.view.select_tournament(list_ids)
        if tournament_id:
            tournament = self.tournament_model.get_tournament_from_id(tournament_id)
            list_players_id = tournament['list_players_id']
        self.run()

    def show_tournament(self):
        self.run()

    def remove_tournament(self):
        self.run()
