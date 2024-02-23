from src.Abstract import AbstractHeadHunter
import requests


class HeadHunter(AbstractHeadHunter):
    """
    Класс для работы с API hh.ru
    """
    def __init__(self, name, top_n):
        self.name = name
        self.top_n = top_n
        self.url = 'https://api.hh.ru'

    def get_vacancies(self):
        """
        Получение вакансий с hh.ru в формате JSON
        """
        data = requests.get(f"{self.url}/vacancies",
                            params={'text': self.name,
                                    'area': 113,
                                    'per_page': self.top_n}).json()
        return data
