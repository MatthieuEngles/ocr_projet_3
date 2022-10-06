import os
clear = lambda: os.system('clear')


class MenuView:
    
       
    def show_menu(self,menu_options):
        clear()
        for k,v in menu_options.items():
            print(f'{k} -> {v[1]}')
        print('')
        choix = None
        while choix == None:
            try: 
                choix = int(input('Votre choix : '))
                if choix not in list(menu_options.keys()):
                    print('Ce choix n\'est pas disponible veuillez recommencer')
                    choix = None
            except Exception as e:
                print('La saisie est invalide veuillez recommencer')
        return choix