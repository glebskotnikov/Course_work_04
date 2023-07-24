class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, vacancy_id, name, city, url, salary_from, salary_to,
                 currency, published_at, requirement, responsibility):
        self.vacancy_id = vacancy_id
        self.name = name
        self.city = city
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.published_at = published_at
        self.requirement = requirement
        self.responsibility = responsibility

    def __repr__(self):
        return f'Vacancy(vacancy_id={self.vacancy_id},' \
               f'name={self.name} ' \
               f'city={self.city},' \
               f'url={self.url}, ' \
               f'salary={self.salary_from}-{self.salary_to},' \
               f'currency={self.currency},' \
               f'published_at={self.published_at} ' \
               f'requirement={self.requirement},' \
               f'responsibility={self.responsibility})'

    def __str__(self):
        salary = ''
        if self.salary_from and self.salary_to:
            salary = f'Зарплата: от {self.salary_from} руб. до {self.salary_to} руб.\n'
        elif self.salary_from is None:
            salary = f'Зарплата: до {self.salary_to} руб.\n'
        elif self.salary_to is None:
            salary = f'Зарплата: от {self.salary_from} руб.\n'
        return f'vacancy_id: {self.vacancy_id}\n' \
               f'Профессия: {self.name}\n' \
               f'Город: {self.city}\n' \
               f'Ссылка на вакансию: {self.url}\n' \
               f'{salary}' \
               f'Дата публикации: {self.published_at}\n' \
               f'Требования: {self.requirement}\n' \
               f'Обязанности: {self.responsibility}\n'

    def __gt__(self, other):
        return self.salary_from > other.salary_from
