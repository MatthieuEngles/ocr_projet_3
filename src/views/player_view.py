# from datetime import datetime
from views.menu_view import MenuView


class PlayerView(MenuView):
    """Player view."""
    def __init__(self):
        super().__init__()

    def prompt_player(self):
        self.clear()
        print("Merci de renseigner les informations")
        family_name = input("Nom de famille: ").title()
        first_name = input("Prénom: ").upper()
        birth_date = None
        while birth_date is None:
            try:
                birth_date = str(input("Date de naissance (jj/mm/AAAA): "))
                # birth_date = datetime.strptime(birth_date, "%d/%m/%Y") ne convient pas à la base de données
            except Exception as e:
                print('La date saisie est invalide veuillez la saisir à nouveau', e)
                birth_date = None
        gender = self.prompt_for_str_in_list(input_text='Genre: H/F: ', test_list=['H', 'F'])
        rank = self.prompt_for_int(input_text='Classement: ')

        return family_name, first_name, birth_date, gender, rank

    def prompt_update_player_rank(self, list_id):
        self.clear()
        update_id = self.prompt_for_int_in_list(input_text='De quel joueur souhaitez vous mettre à jour le classement?',
                                                test_list=list_id)
        if update_id:
            rank = self.prompt_for_int("Rank: ")
            return update_id, rank
        else:
            return None, None

    def prompt_remove_player(self, list_id):
        self.clear()
        print('Quel joueur souhaitez vous retirer ?')
        remove_id = self.prompt_for_int_in_list(
            input_text='Saisissez son identifiant (pour quitter taper "entrée" sans saisir de numéro): ',
            test_list=list_id)
        return remove_id

    def confirm_remove_player(self, id):
        input(f'Joueur n°{id} retiré, appuyez sur entrée')

    def confirm_add_player(self, id):
        input(f'Joueur n°{id} ajouté, appuyez sur entrée')

    def confirm_update_rank_player(self, id):
        input(f'Classement du joueur n°{id} modifié, appuyez sur entrée')

    def show_player(self, player, full=False):
        print("Joueur n° : ", player['id'])
        if full:
            birth_value = 'né le' if player['gender'] == 'H' else 'née le'
            print(f"{player['first_name']} {player['family_name']} {birth_value} {player['birth_date']} \
                    a un score de {player['rank']}")    #{player['birth_date'].strftime('%d/%m/%Y')}
        else:
            print(f"{player['first_name']} {player['family_name']} a un score de {player['rank']}")

    def show_all_player(self, list_player, full=False):
        self.clear()
        print('---------')
        for player in list_player:
            self.show_player(player, full)
            print('---------')
        input('Appuyez sur entrée pour continuer')
