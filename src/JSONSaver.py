import json
import os
from src.ABCClass import ABCSaver


class JSONSaver(ABCSaver):
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def create_empty_json_file(filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write('[]')
        else:
            with open(filename, 'w') as file:
                file.write('[]')

    def add_vacancy(self, vacancy):
        try:
            with open(self.filename, 'r+') as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        data.append(vacancy.to_dict())

        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def get_vacancies(self, criteria):
        pass

    def delete_vacancy(self, criteria):
        pass