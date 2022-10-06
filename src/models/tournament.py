from typing import List
from datetime import datetime

class Tournament:
    def __init__(self):
        self.nom = ''
        self.liste_joueurs = []
        self.date = datetime.now()
        self.nb_tours = ''
        self.tournees = ''
        self.time_control = ''
        self.description = ''
        