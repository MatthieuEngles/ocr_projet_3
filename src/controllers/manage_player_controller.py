"""Define the main controller."""
from models.player import Player
from views.player_view import PlayerView
# from const import *

from controllers.base_controller import BaseController


class ManagePlayer(BaseController):
    """Main controller."""

    def __init__(self, parent_controller):
        self.player_model = Player()

        menu_options = {1: [self.add_player, 'Créer un joueur'],
                        2: [self.show_all_palyer, 'Voir les joueurs'],
                        3: [self.update_rank_player, 'Modifier le classement d\'un joueur'],
                        4: [self.remove_player, 'Supprimer un joueur'],
                        5: [parent_controller.run, 'Revenir au menu précedent'],
                        }
        super().__init__(menu_options, PlayerView())

    def add_player(self):
        player_info = self.view.prompt_player()
        player = self.player_model.serialize(*player_info)
        id = self.player_model.add_to_base(player)
        self.view.confirm_add_player(id)
        self.run()  # on retourne au menu

    def show_all_palyer(self):
        list_players = self.player_model.get_all_player()
        self.view.show_all_player(list_players, full=True)
        self.run()  # on retourne au menu

    def update_rank_player(self):
        list_ids = self.player_model.get_list_id()
        player_id, new_rank = self.view.prompt_update_player_rank(list_ids)
        if player_id is not None:
            self.player_model.update_rank_player(player_id, new_rank)
            self.view.confirm_update_rank_player(player_id)
        else:
            self.view.prompt_annulation()
        self.run()  # on retourne au menu

    def remove_player(self):
        list_ids = self.player_model.get_list_id()
        id = self.view.prompt_remove_player(list_ids)
        if id is not None:
            self.player_model.delete_from_base(id)
            self.view.confirm_remove_player(id)
        else:
            self.view.prompt_annulation()
        self.run()  # on retourne au menu
