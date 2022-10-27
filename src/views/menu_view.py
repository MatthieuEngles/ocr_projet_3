import time
import os


class MenuView:

    def clear(self):
        os.system('clear')

    def prompt_annulation(self):
        print('Commande annulée')
        time.sleep(0.5)

    def prompt_for_int(self,
                       input_text='Saisissez un nombre entier',
                       error_text='La saisie est invalide, vous devez saisir un entier',
                       with_none_quit=True):
        data = None
        while data is None:
            try:
                data = input(input_text)
                if with_none_quit and data == '':
                    return None
                data = int(data)
            except Exception:
                print(error_text)
        return data

    def prompt_list(self, data, test_list, error_text, prompt_list):
        if data not in test_list:
            data = None
            if prompt_list:
                print(f"{error_text} [{', '.join(map(str, test_list))}]")
            else:
                print(f'{error_text}')
            return None
        return data

    def prompt_for_str_in_list(self,
                               input_text='Saisissez une donnée: ',
                               error_text='La saisie est invalide, elle ne se trouve pas dans: ',
                               test_list=None,
                               set_upper=True,
                               prompt_list=True):
        data = None
        while data is None:
            data = input(input_text)
            if set_upper:
                data = data.upper()
            data = self.prompt_list(data, test_list, error_text, prompt_list)
        return data

    def prompt_for_int_in_list(self,
                               input_text='Saisissez un nombre entier',
                               error_text='La saisie est invalide, elle ne se trouve pas dans:',
                               test_list=None,
                               prompt_list=True,
                               with_none_quit=True):
        data = None
        while data is None:
            data = self.prompt_for_int(input_text=input_text)
            if data is None and with_none_quit:
                return data
            data = self.prompt_list(data, test_list, error_text, prompt_list)
        return data

    def show_menu(self, menu_options):
        self.clear()
        for k, v in menu_options.items():
            print(f'{k} -> {v[1]}')
        print('')
        choix = self.prompt_for_int_in_list(input_text='Votre choix : ',
                                            error_text='Ce choix n\'est pas disponible veuillez recommencer',
                                            test_list=list(menu_options.keys()),
                                            prompt_list=False,
                                            with_none_quit=False)
        return choix

    def prompt_not_implemented(self):
        input('Commande non implémentée, appuyez sur entrée')
