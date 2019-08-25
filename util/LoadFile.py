import json
from os import path

add_button = {"icon": "plus_button.png", "exe": "Add Button"}
category_add_button = {"name": "Add Button", "icon": "plus_button.png"}


class FileLoader:
    def __init__(self, file='data.json', key='categories'):
        self.file = file
        self.key = key
        print(self.key)
        self.load_file()

    def load_file(self):
        if not path.exists('data.json'):
            print('no')
            file = open('data.json', 'w')
            self.data = {
                "categories": [],
                "tutorials": {
                    "first-open": True,
                    "add-category": True,
                    "enter-category": True,
                    "add-icon": True,
                    "add-game": True
                }
            }
            json.dump(self.data, file, indent=4)
            return self.data
        with open('data.json', 'r') as f:
            self.data = json.load(f)
            self.items = self.data[self.key]
            f.close()
        return self.data

    def dump_data(self, **kwargs):
        with open('data.json', 'w') as f:
            self.data[self.key] = self.items
            json.dump(self.data, f, indent=4)
            f.close()
        return self.data

    def disable_tutorials(self):
        if self.data is None:
            self.load_file()
        self.data['tutorials'] = {
            "tutorials": {
                "first-open": False,
                "add-category": False,
                "enter-category": False,
                "add-icon": False,
                "add-game": False
            }
        }

    def set_key(self, text):
        self.key = text
        return self.load_file()

    def get_key(self):
        return self.key

    def is_first_open(self):
        return self.data['tutorials']['first-open']

    def get_items(self, **kwargs):
        if self.items is None:
            return self.load_file()[self.key]
        return self.items
