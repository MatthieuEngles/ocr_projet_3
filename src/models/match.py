from tinydb import TinyDB, Query,where
from models.base import BaseItem
class Match(BaseItem):

    def __init__(self):
        super().__init__('matches')
               
    def serialize(self,family_name,first_name,birth_date,gender,rank):
        return {'id':self.get_next_id(), 
                'tournament_id': family_name,
                'turn_id': first_name,
                'data': birth_date,
                'player_1_id': gender,
                'player_2_id': rank}
        