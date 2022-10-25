from tinydb import Query, where
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

    def get_all_player(self):
        return self.table.all()

    def add_to_base(self, player):
        self.table.insert(player)
        return player['id']

    def get_player_from_id(self, id):
        player = Query()
        player = self.table.search(player.id == id)
        print(player)

    def update_rank_player(self, id, new_rank):
        player = Query()
        self.table.update({'rank': new_rank}, player['id'] == id)

    def delete_from_base(self, id):
        self.table.remove(where('id') == id)
