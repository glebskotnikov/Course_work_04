import json

from src.vacancy import Vacancy


def instance_vacancy_hh(data):
    vacancy_list = []
    for item in data["items"]:
        vacancy = Vacancy(item["name"],
                          item["alternate_url"],
                          item["salary"]["from"],
                          item["salary"]["to"],
                          item["published_at"],
                          item["snippet"]["requirement"],
                          item["snippet"]["responsibility"])
        vacancy_list.append(vacancy)
    return vacancy_list


def instance_vacancy_sj(data):
    vacancy_list = []
    for item in data["objects"]:
        # print(json.dumps(item, indent=4, ensure_ascii=False))
        # break
        vacancy = Vacancy(item["profession"],
                          item["link"],
                          item["payment_from"],
                          item["payment_to"],
                          item["date_published"],
                          item["candidat"],
                          item["vacancyRichText"])
        vacancy_list.append(vacancy)
    return vacancy_list
