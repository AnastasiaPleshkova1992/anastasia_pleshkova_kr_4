import os
from config import ROOT
import json

json_file = os.path.join(ROOT, 'data', 'hh.json')


class JSONSaver:
    @staticmethod
    def add_vacancy(vacancies):
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    # @staticmethod
    # def delete_vacancy():
    #     with open(json_file, 'w', encoding='utf-8') as file:
    #         data = json.load(file)
    #         data.clear()
    @staticmethod
    def get_vacancy(file):
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data


