from tinydb import Query
from models.base import BaseItem


class Match(BaseItem):

    def __init__(self):
        super().__init__('matches')

    def serialize(self, tournament_id, turn_id, date, p1_id, p2_id, p1_score, p2_score):
        return {'id': self.get_next_id(),
                'tournament_id': tournament_id,
                'turn_id': turn_id,
                'date': date,
                'player_1_id': p1_id,
                'player_2_id': p2_id,
                'player_1_score': p1_score,
                'player_2_score': p2_score}

    def get_match_tournament(self, tournament_id):
        # liste des matches du tournoi tournament_id dans lequel joué player_id
        list_match = self.table.search(Query()['tournament_id'] == tournament_id)
        return list_match

    def get_match_tournament_player(self, tournament_id, player_id):
        # liste des matches du tournoi tournament_id dans lequel joué player_id
        list_match = self.table.search((Query()['tournament_id'] == tournament_id) and
                                       ((Query()['p1_id'] == player_id) or (Query()['p2_id'] == player_id))
                                       )
        return list_match

    def is_match_between_p1_p2(self, tournament_id, p1, p2):
        # liste des matches du tournoi tournament_id dans lequel joué player_id
        list_match = self.table.search((Query()['tournament_id'] == tournament_id) and
                                       ((Query()['p1_id'] == p1) or (Query()['p2_id'] == p1) and
                                        (Query()['p1_id'] == p2) or (Query()['p2_id'] == p2))
                                       )
        return len(list_match) > 0
