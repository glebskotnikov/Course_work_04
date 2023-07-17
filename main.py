from src.classes_API import HeadHunterAPI, SuperJobAPI
from src.utils import instance_vacancy_hh, instance_vacancy_sj

if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python")
    dict_vacancy_hh = instance_vacancy_hh(hh_vacancies)
    # for item in dict_vacancy:
    #     print(item)
    superjob_api = SuperJobAPI()
    superjob_vacancies = superjob_api.get_vacancies("Python")
    dict_vacancy_sj = instance_vacancy_sj(superjob_vacancies)
    # for item in dict_vacancy_sj:
    #     print(item)
