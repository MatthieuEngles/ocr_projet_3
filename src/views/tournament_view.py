from views.menu_view import MenuView


class TournamentView(MenuView):

    def __init__(self):
        super().__init__()

    def prompt_tournament(self, all_player):
        self.clear()
        print("Merci de renseigner les informationsdu tournoi")
        nom = input("Nom du tournoi: ")
        lieu = input("Lieu: ")
        date = None
        while date is None:
            try:
                date = str(input("Date du tournoi(jj/mm/AAAA): "))
                # date = datetime.strptime(date, "%d/%m/%Y") ne convient pas à la base de données
            except Exception as e:
                print('La date saisie est invalide veuillez la saisir à nouveau', e)
                date = None

        nb_turn = 4  #ne pas hardcoder ca ici

        list_player_id = []
        while len(list_player_id) < 8:
            print("Ajouter un joueur parmi:")
            list_all_player_id = [player['id'] for player in all_player]
            for player in all_player:
                print(f"     {player['id']}: {player['family_name']} {player['first_name']} classé(e) {player['rank']}")
            choix = self.prompt_for_int_in_list(input_text='Votre choix : ', test_list=list_all_player_id)
            list_player_id.append(choix)
            all_player = [player for player in all_player if player['id'] != choix]
            print(f'Joueur n°{choix} ajouté au tournoi, il manque encore {8-len(list_player_id)} joueurs')
            print()

        time_control = self.prompt_for_int_in_list(
            input_text='"Contrôle du temps: 1-> Bullet | 2-> Blitz | 3-> Coup rapide"',
            test_list=[1, 2, 3])

        description = input("Ajoutez une description: ")

        return nom, lieu, date, nb_turn, list_player_id, time_control, description

    def prompt_select_tournament(self, list_id):
        self.clear()
        print('Quel tournoi voulez vous jouer ?')
        remove_id = self.prompt_for_int_in_list(
            input_text='Saisissez son identifiant (pour quitter taper "entrée" sans saisir de numéro):',
            test_list=list_id)
        return remove_id

    def prompt_not_enough_player(self, player_count):
        print('Il faut au moins 8 joueur dans la base pour créer un tournoi')
        print(f'Actuellement il y a {player_count} joueur(s)')
        input('appuyez sur entrée pour continuer')

    def confirm_add_tournament(self, id):
        input(f'Tournoi n°{id} créé, appuyez sur entrée')

    def show_tournament(self):
        self.clear()
