from tinydb import TinyDB, Query,where
class BaseItem:

    def __init__(self,table):
        db = TinyDB('./data/ocr3_db.json')
        self.table = db.table(table)
    
    def get_next_id(self):
        list_id = self.get_list_id()
        if len(list_id)>0:
            next_id = list_id[-1]+1
        else:
            next_id = 0
        return next_id
    
    def get_list_id(self):
        liste_items = self.table.all()
        if len(liste_items)>0:
            list_id = [item['id'] for item in liste_items]
        else:
            list_id = []
        return list_id
    
    def get_count(self):
        return len(self.get_list_id())