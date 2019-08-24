import json
from os import path


class FileLoader:
    def __init__(self, file='data.json', key='categories'):
        self.file = file
        self.key = key
        self.data = []
        self.items = []

    def load_file(self):
        if not path.exists('data.json'):
            file = open('data.json', 'w')
            self.data = {
                "categories": [],
                "tutorials": {
                    "first-open": True,
                    "add-category": True
                }
            }
            json.dump(self.data, file, indent=4)
            return self.data
        with open('data.json', 'r') as f:
            self.data = json.load(f)
            self.items = self.data[self.key]
            f.close()
        return self.data

    def set_key(self, text):
        self.key = text

    def is_first_open(self):
        return self.data['tutorials']['first-open']
