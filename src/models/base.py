from tinydb import TinyDB, Query, where


class BaseItem:

    def __init__(self, table):
        db = TinyDB('./data/ocr3_db.json')
        self.table = db.table(table)

    def get_next_id(self):
        list_id = self.get_list_id()
        if len(list_id) > 0:
            next_id = list_id[-1] + 1
        else:
            next_id = 0
        return next_id

    def get_list_id(self):
        liste_items = self.table.all()
        if len(liste_items) > 0:
            list_id = [item['id'] for item in liste_items]
        else:
            list_id = []
        return list_id

    def get_count(self):
        return len(self.get_list_id())

    def get_from_id(self, id):
        if isinstance(id, int):
            query = Query()
            item = self.table.search(query.id == id)
            if len(item) > 0:
                return item[0]
            else:
                return None
        if isinstance(id, list):
            query = Query()
            items = self.table.search(query.id.one_of(id))
            return items

    def delete_from_base(self, id):
        self.table.remove(where('id') == id)

    def add_to_base(self, item):
        self.table.insert(item)
        return item['id']

    def get_all(self):
        return self.table.all()