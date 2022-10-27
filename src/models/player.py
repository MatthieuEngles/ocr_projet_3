from tinydb import Query
from models.base import BaseItem


class Player(BaseItem):

    def __init__(self):
        super().__init__('players')

    def serialize(self, family_name, first_name, birth_date, gender, rank):
        return {'id': self.get_next_id(),
                'family_name': family_name,
                'first_name': first_name,
                'birth_date': birth_date,
                'gender': gender,
                'rank': rank}

    def update_rank_player(self, id, new_rank):
        self.table.update({'rank': new_rank}, Query()['id'] == id)
