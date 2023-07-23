import json

from classes.JSON import JSONSaver, JSONLoader
from classes.API import HeadHunterAPI, SuperJobAPI
from src.utils import instance_vacancy_hh, instance_vacancy_sj, filter_vacancies, \
    sorted_data, instance_vacancy_sorted, \
    top_n_vacancies

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_saver = JSONSaver()
json_loader = JSONLoader()


def user_interaction():
    # получаем список вакансий по запросу пользователя от api и создаем экземпляры класса
    search_query = input("Введите название профессии: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    list_instance_vacancy_hh = instance_vacancy_hh(hh_vacancies)
    superjob_vacancies = superjob_api.get_vacancies(search_query)
    list_instance_vacancy_sj = instance_vacancy_sj(superjob_vacancies)

    # сохраняем список вакансий в json файл
    json_saver.add_vacancy(list_instance_vacancy_hh, list_instance_vacancy_sj)

    # фильтруем список вакансий по указанной зарплате
    search_salary = int(input("Введите желаемую минимальную зарплату: "))
    salary_sorted = json_loader.get_vacancies_by_salary(search_salary)

    # фильтруем список вакансий по ключевым словам пользователя
    filter_words = input("\nВведите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(salary_sorted, filter_words)

    #  сортируем список вакансий по дате
    sort_data = sorted_data(filtered_vacancies)

    # создаем экземпляры класса после применения всех фильтров и сортировки
    list_instance_vacancy_sorted = instance_vacancy_sorted(sort_data)

    # выводим топ N список вакансий
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_n_vacancies(list_instance_vacancy_sorted, top_n)

    # сохраняем top N список вакансий в json файл
    while True:
        save_json = input("Сохранить в json файл? [y/n]: ")
        if save_json.lower() == 'y':
            json_saver.save_json(list_instance_vacancy_sorted)
            break
        elif save_json.lower() == 'n':
            print('Программа завершена')
            break
        else:
            print('Неверный ввод')


if __name__ == '__main__':
    user_interaction()
