from tinydb import Query
from models.base import BaseItem


class Tournament(BaseItem):

    def __init__(self):
        super().__init__('tournament')

    def serialize(self, nom, lieu, date, nb_turn, list_player_id, time_control, description):
        return {'id': self.get_next_id(),
                'nom': nom,
                'lieu': lieu,
                'date': date,
                'nb_turn': nb_turn,
                'nb_turn_completed': 0,
                'list_player_id': list_player_id,
                'time_control': time_control,
                'description': description}

    def upgrade_nb_turn_completed(self, id):
        old_rank = self.get_nb_turn_completed_from_id(id)
        self.table.update({'nb_turn_completed': old_rank + 1}, Query()['id'] == id)

    def get_nb_turn_completed_from_id(self, id):
        tournament = self.get_from_id(id)
        if tournament:
            return tournament['nb_turn_completed']
        else:
            return None

    def get_sorted_player(self, id):
        tournament = self.get_from_id(id)
        if tournament:
            return tournament['nb_turn_completed']
        else:
            return None
