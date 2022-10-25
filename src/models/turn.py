from tinydb import TinyDB, Query,where
from models.base import BaseItem
class Turn(BaseItem):

    def __init__(self):
        super().__init__('turns')
               
    def serialize(self,list_matches_id,date,player_1_id,player_2_id,result_player_1,result_player_2):
        return {'id':self.get_next_id(), 
                'list_matches_id': list_matches_id,
                'date': date,
                'player_1_id': player_1_id,
                'player_2_id': player_2_id,
                'result_player_1':result_player_1,
                'result_player_2':result_player_2}