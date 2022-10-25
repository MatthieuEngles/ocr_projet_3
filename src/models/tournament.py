from tinydb import TinyDB, Query,where
from models.base import BaseItem

class Tournament(BaseItem):

    def __init__(self):
        super().__init__('tournament')
    
    def serialize(self,nom,lieu,date,nb_turn,list_player_id,turns, time_control,description):
        return {'id':self.get_next_id(), 
                'nom': nom,
                'lieu': lieu,
                'date': date,
                'nb_turn': nb_turn,
                'list_player_id':list_player_id,
                'turns' : turns,
                'time_control':time_control,
                'description':description}
    
    def get_all_tournament(self):
        return self.table.all()
    
    def add_to_base(self,tournament):
        self.table.insert(tournament)
        return tournament['id']
    
    def get_tournament_from_id(self, id):
        tournament = Query()
        tournament = self.table.search(tournament.id == id)
        return tournament
    
    
    def delete_from_base(self,id):
        self.table.remove(where('id')==id)
        