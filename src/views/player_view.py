import os
from datetime import datetime
from views.menu_view import MenuView

clear = lambda: os.system('clear')


class PlayerView(MenuView):
    """Player view."""
    def __init__(self):
        super().__init__()
                    
    def prompt_player(self,num=None):
        clear()
        if num:
            print(f"Ajout du joueur #{num}")
        else:
            print("Ajout d'un nouveau joueur")
        print("Merci de renseigner les informations")
        family_name = input("Nom de famille: ").title()
        first_name = input("Prénom: ").upper()
        birht_date=None
        while birht_date==None:
            try:
                birth_date = input("Date de naissance (jj/mm/AAAA): ")
                birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
            except Exception as e:
                print('La date saisie est invalide veuillez la saisir à nouveau')
                birth_date=None
        gender = None
        while gender==None:
            gender = input("Genre: H/F: ").upper()
            if gender not in ['H','F']:
                gender = None
                print('Le genre saisi est invalide veuillez spécifier "H" ou "F"')
        rank = None 
        while rank==None:
            rank = input("Rank: ")
            try:
                rank = int(input("Rank: "))
            except Exception as e:
                print('La saisie est invalide, le rank doit être un entier')
                rank=None
        
        # est ce qu'on teste le parsing dans la vue ??? OUI !!!!!
        return family_name,first_name,birth_date,gender,rank

    def show_player(self, player,full=False):
        if full:
            birth_value  = 'né le' if gender == 'H' else 'née le'
            print(f'{player.first_name} {player.family_name} {player.birth_value} {player.birth_date} a un score de {player.rank}')    
        else:
            print(f'{player.first_name} {player.family_name} a un score de {player.rank}')
        input("Pressez une touche pour continuer")    
        
    
