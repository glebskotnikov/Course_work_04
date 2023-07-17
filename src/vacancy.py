class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, published_at, requirement, responsibility):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.published_at = published_at
        self.requirement = requirement
        self.responsibility = responsibility

    def __repr__(self):
        return f'Vacancy(name={self.name}, ' \
               f'url={self.url}, ' \
               f'salary={self.salary_from}-{self.salary_to},' \
               f'published_at={self.published_at} ' \
               f'requirement={self.requirement},' \
               f'responsibility={self.responsibility})'

    def __str__(self):
        return f'Профессия: {self.name},\n' \
               f'Ссылка на вакансию: {self.url},\n' \
               f'Зарплата: от {self.salary_to} до {self.salary_from},\n' \
               f'Дата публикации: {self.published_at},\n' \
               f'Требования: {self.requirement},\n' \
               f'Обязанности: {self.responsibility}\n'
