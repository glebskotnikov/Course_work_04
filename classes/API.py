import requests
from abc import ABC, abstractmethod
import os

SUPERJOB_API = os.getenv('SUPERJOB_API_KEY')


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

        # Справочник для параметров GET-запроса
        params = {
            'text': f'NAME:{name}',  # Текст фильтра.
            'area': 1,  # Поиск оcуществляется по вакансиям города Москва
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100,  # Кол-во вакансий на 1 странице
            'only_with_salary': True  # Поиск вакансий только с зарплатой
        }

        response = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = response.json()
        return data


class SuperJobAPI(VacancyAPI):
    """
    Класс для работы с API сайта Superjob.
    """

    def get_vacancies(self, name):
        URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
        SUPERJOB_API = os.environ.get('SUPERJOB_API_KEY')

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
