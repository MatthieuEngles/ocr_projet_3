import sqlite3
from os.path import exists

class Main:
    

    def __init__(self):
        if not exists('ocr3.db'):
            #### Faire en tiny db
            conn = sqlite3.connect('ocr3.db')
            c = conn.cursor()

            # Create table
            c.execute('''CREATE TABLE players
                        (nom text, prenom text, date_naissance real, genre text, rank int)''')

            c.execute('''CREATE TABLE tournaments
                        (nom text, joueurs text, date real, nb_tour int, price real)''')
            # Save (commit) the changes
            conn.commit()

            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            conn.close()
            print('Log : Base de données créée')
            input()
        else:
            print('Log : Base de données présente')
            input()

