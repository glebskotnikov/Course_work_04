import requests
from abc import ABC, abstractmethod
import os

URL_HH = 'https://api.hh.ru/vacancies'
URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
SUPERJOB_API = os.getenv('SUPERJOB_API_KEY')


# SUPERJOB_API = os.environ.get('SUPERJOB_API_KEY')


class VacancyAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, name):
        pass


class HeadHunterAPI(VacancyAPI):
    """
    Класс для работы с API сайта Headhunter.
    """

    def get_vacancies(self, name):
        """
        Создаем метод для получения страницы со списком вакансий.
        """
        print(f'\nПолучаем данные с {URL_HH}...')
        params = {
            'text': f'NAME:{name}',
            'page': 0,
            'per_page': 100,
            'only_with_salary': True
        }

        response = requests.get(URL_HH, params)
        data = response.json()
        return data


class SuperJobAPI(VacancyAPI):
    """
    Класс для работы с API сайта Superjob.
    """

    def get_vacancies(self, name):
        print(f'\nПолучаем данные с {URL_SJ}...')
        headers = {'X-Api-App-Id': SUPERJOB_API}
        params = {
            'keywords': name,
            'page': 0,
            'count': 100,
            'no_agreement': 1
        }
        response = requests.get(URL_SJ, headers=headers, params=params)
        result_page = response.json()
        return result_page
