from views.menu_view import MenuView

import os
clear = lambda: os.system('clear')

class TournamentView(MenuView):
    

    def __init__(self):
        super().__init__()
    
    def prompt_tournament(self,num=None):
        clear()
        
        self.nom = ''
        self.liste_joueurs = []
        self.date = datetime.now()
        self.nb_tours = ''
        self.tournees = ''
        self.time_control = ''
        self.description = ''
        
        if num:
            print(f"Ajout du joueur #{num}")
        else:
            print("Ajout d'un nouveau joueur")
        print("Merci de renseigner les informations")
        nom = input("Nom du tournoi: ").title()
        date = input("Prénom: ").upper()
        birth_date = input("Date de naissance (jj/mm/AAAA): ")
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        gender = input("Genre: H/F: ").upper()
        rank = input("Rank: ")
        
        # est ce qu'on teste le parsing dans la vue ??? Oui
        return family_name,first_name,birth_date,gender,rank
    
    def show_tournament(self):
        clear()