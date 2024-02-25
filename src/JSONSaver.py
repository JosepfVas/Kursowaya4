import json
from src.ABCClass import ABCSaver


class JSONSaver(ABCSaver):
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        try:
            with open(self.filename, 'r+') as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        data.append(vacancy.to_dict())

        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)