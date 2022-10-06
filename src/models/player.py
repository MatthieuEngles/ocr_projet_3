class Player:
    
    # mettre la liste des joueurs dans un attribut de classe et pas dans une  instance d'objet
    
    
    def __init__(self, family_name,first_name,birth_date,gender,rank):
        """Has a name and a hand."""
        self.family_name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        
    def __str__(self):
        return(self.first_name+" "+self.family_name)