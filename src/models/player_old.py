from tinydb import TinyDB, Query
class Player:
    
    # mettre la liste des joueurs dans un attribut de classe et pas dans une  instance d'objet
    db = TinyDB('./data/ocr3_db.json')
    players_table = db.table('players')
    
    @classmethod
    def init_player_count(cls):
        
        # aller chercher dans la base le plus grand id joueur
        return cls.player_count
    
    @classmethod
    def get_player_count(cls):
        return cls.player_count
    
    player_count = init_player_count() 
    
    # inutile !!!!! pas besoin d'avoir une liste de joueur seul la base de données suffit
    # @classmethod
    # def update_list_player(cls):
    #     serialized_players = cls.players_table.all()
    #     return [Player(**sp) for sp in serialized_players]
    def __init__(self):
        db = TinyDB('./data/ocr3_db.json')
        self.players_table = db.table('players')
    
    def add_player(self, family_name,first_name,birth_date,gender,rank):
        self.id = self.player_count 
        self.family_name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        
    def __str__(self):
        return(self.first_name+" "+self.family_name)
    
    def serialize(self):
        palyer_serialized= {'id':self.get_player_count(), 
                            'family_name': self.family_name,
                            'first_name': self.first_name,
                            'birth_date': self.birth_date,
                            'gender': self.gender,
                            'rank': self.rank}

        
    def add_to_base(self): #c'est le modèle qui accède à la base
        self.players_table.insert(self.serialize())
        self.player_count+=1
        