import operator
from datetime import datetime

from classes.vacancy import Vacancy


def instance_vacancy_hh(data):
    """
    Создаем список экземпляров классов с сайта Headhunter.
    """
    vacancy_list = []
    for item in data["items"]:
        vacancy = Vacancy(item["id"],
                          item["name"],
                          item["area"]["name"],
                          item["alternate_url"],
                          item["salary"]["from"],
                          item["salary"]["to"],
                          item["salary"]["currency"],
                          item["published_at"],
                          item["snippet"]["requirement"],
                          item["snippet"]["responsibility"])
        vacancy_list.append(vacancy)
    return vacancy_list


def instance_vacancy_sj(data):
    """
    Создаем список экземпляров классов с сайта Superjob.
    """
    vacancy_list = []
    for item in data["objects"]:
        vacancy = Vacancy(item["id"],
                          item["profession"],
                          item["town"]["title"],
                          item["link"],
                          item["payment_from"],
                          item["payment_to"],
                          item["currency"],
                          item["date_published"],
                          item["candidat"],
                          item["vacancyRichText"])
        vacancy_list.append(vacancy)
    return vacancy_list


def filter_vacancies(list_vacancies, filter_words):
    """
    Фильтруем список словарей по словам.
    """
    new_list = []
    counter = 0
    for item in list_vacancies:
        for word in filter_words:
            if item['requirement'] and item['responsibility']:
                if word.lower() in item['requirement'].lower() or word.lower() in item['responsibility'].lower():
                    new_list.append(item)
                    counter += 1
    print(f'\nКол-во вакансий после обработки фильтров: {counter}\n')
    return new_list


def sorted_data(list_vacancies):
    """
    Сортируем по дате список вакансий.
    """
    for item in list_vacancies:
        if 'superjob.ru' in item['url']:
            item['published_at'] = datetime.fromtimestamp(item['published_at'])
            item['published_at'] = item['published_at'].strftime('%d-%m-%Y %H:%M:%S')
            item['published_at'] = datetime.strptime(item['published_at'], '%d-%m-%Y %H:%M:%S')
        else:
            item['published_at'] = datetime.fromisoformat(item['published_at'])
            item['published_at'] = item['published_at'].strftime('%d-%m-%Y %H:%M:%S')
            item['published_at'] = datetime.strptime(item['published_at'], '%d-%m-%Y %H:%M:%S')
    sorted_list = sorted(list_vacancies, key=operator.itemgetter('published_at'), reverse=True)
    for item in sorted_list:
        item['published_at'] = item['published_at'].strftime('%d-%m-%Y %H:%M:%S')
    return sorted_list


def instance_vacancy_sorted(data):
    """
    Создаем список экземпляров класса, полученные после всех сортировок и фильтров.
    """
    vacancy_list = []
    for item in data:
        vacancy = Vacancy(item["vacancy_id"],
                          item["name"],
                          item["city"],
                          item["url"],
                          item["salary_from"],
                          item["salary_to"],
                          item["currency"],
                          item["published_at"],
                          item["requirement"],
                          item["responsibility"])
        vacancy_list.append(vacancy)
    return vacancy_list


def top_n_vacancies(list_vacancies, n):
    """
    Выводим top N вакансий.
    """
    counter = 1
    for item in list_vacancies:
        print(item)
        counter += 1
        if counter > n:
            break
