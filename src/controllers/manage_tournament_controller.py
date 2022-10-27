from models.player import Player
from models.tournament import Tournament
from models.match import Match
from views.tournament_view import TournamentView
from views.match_view import MatchView

# from const import *

from controllers.base_controller import BaseController


class ManageTournament(BaseController):

    def __init__(self, parent_controller):
        # models
        self.tournament_model = Tournament()
        self.player_model = Player()
        self.match_model = Match()
        self.match_view = MatchView()
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
            all_player = self.player_model.get_all()
            tournament_info = self.view.prompt_tournament(all_player)
            tournament = self.tournament_model.serialize(*tournament_info)
            id = self.tournament_model.add_to_base(tournament)
            self.view.confirm_add_tournament(id)
        self.run()  # on retourne au menu

    def play_turn(self, tournament, list_player):
        # creation des 4 premiere paires
        turn_id = tournament['nb_turn_completed']
        list_match_player_pos = []
        if turn_id == 0:
            for i in range(4):
                list_match_player_pos.append((list_player[i], list_player[i + 4]))
        else:
            while len(list_match_player_pos) != 4:
                player_to_remove = []
                p1 = list_player[0]
                player_to_remove.append(p1)
                for p in list_player[1:]:
                    if not self.match_model.is_match_between_p1_p2(tournament['id'], p1['id'], p['id']):
                        list_match_player_pos.append((p1, p))
                        player_to_remove.append(p)
                        break
                list_player = [p for p in list_player if p not in player_to_remove]

        for p1, p2 in list_match_player_pos:
            result = self.match_view.prompt_match(p1, p2)
            if result == 1:
                p1_score = 1
                p2_score = 0
            elif result == 2:
                p1_score = 0.5
                p2_score = 0.5
            else:
                p1_score = 0
                p2_score = 1
            match = self.match_model.serialize(tournament_id=tournament['id'],
                                               turn_id=turn_id,
                                               date='',
                                               p1_id=p1['id'],
                                               p2_id=p2['id'],
                                               p1_score=p1_score,
                                               p2_score=p2_score
                                               )
            id = self.match_model.add_to_base(match)
            self.match_view.confirm_add_match(id)

    def update_player_score(self, tournament_id, player):
        list_match = self.match_model.get_match_tournament_player(tournament_id, player['id'])
        score_player = 0
        for m in list_match:
            if m['p1_id'] == player['id']:
                delta_score = m['p1_score']
            else:
                delta_score = m['p2_score']
            score_player += delta_score
        player['score'] = score_player + player['rank'] / 10000.
        return player

    def load_and_sort_player(self, tournament):
        turn_id = tournament['nb_turn_completed']
        list_players_id = tournament['list_player_id']
        list_player = self.player_model.get_from_id(list_players_id)
        if turn_id == 0:
            list_player.sort(key=lambda p: p['rank'], reverse=True)
        else:
            list_player = [self.update_player_score(tournament['id'], p) for p in list_player]
            list_player.sort(key=lambda p: p['score'], reverse=True)

        return list_player

    def play_tournament(self):
        list_ids = self.tournament_model.get_list_id()
        tournament_id = self.view.prompt_select_tournament(list_ids)
        tournament = self.tournament_model.get_from_id(tournament_id)
        if tournament['nb_turn_completed'] >= 4:
            self.view.prompt_tournament_complete(tournament_id)
        else:
            list_player = self.load_and_sort_player(tournament)
            self.play_turn(tournament, list_player)
        self.tournament_model.upgrade_nb_turn_completed(tournament_id)
        self.run()

    def show_tournament(self):
        list_ids = self.tournament_model.get_list_id()
        tournament_id = self.view.prompt_select_tournament(list_ids)
        matches = self.match_model.get_match_tournament(tournament_id)
        self.view.show_tournament(tournament_id, matches)
        self.run()

    def remove_tournament(self):
        self.view.prompt_not_implemented()
        self.run()
