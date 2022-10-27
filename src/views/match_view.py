# from datetime import datetime
from views.menu_view import MenuView


class MatchView(MenuView):
    """Player view."""
    def __init__(self):
        super().__init__()

    def prompt_match(self, p1, p2):
        self.clear()
        print(f"Le match oppose {p1['first_name']} {p1['family_name']} à {p2['first_name']} {p2['family_name']}")
        print()
        print(f"1 -> {p1['first_name']} {p1['family_name']}  a gagné")
        print("2 -> Match nul")
        print(f"3 -> {p2['first_name']} {p2['family_name']}  a gagné")
        result = self.prompt_for_int_in_list(input_text='Quel est le résultat ?: ', test_list=[1, 2, 3])
        return result

    def confirm_add_match(self, id):
        input(f'Match n°{id} enregistré, appuyez sur entrée')

    def show_match(self, match):
        print(f"Tour n°{match['turn_id']} - Match n°{match['id']}")
        print(f"joueur n°{match['player_1_id']} vs joueur n°{match['player_2_id']}")
        if match['player_1_score'] == 1:
            print(f"joueur n°{match['player_1_id']} a gagné")
        elif match['player_1_score'] == 0.5:
            print("match nul")
        else:
            print(f"joueur n°{match['player_2_id']} a gagné")
        print('------------')
