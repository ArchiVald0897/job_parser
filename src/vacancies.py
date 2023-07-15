class Vacancies:
    """Класс для работы с вакансией из HeadHunter и SuperJob"""

    def __init__(self, title: str, vacancy_url: str, vacancy_id: int, company_name: str, work_place: str,
                 salary_from: int, salary_to: int, salary_currency: str, experience: str) -> None:
        self.title = title
        self.vacancy_url = vacancy_url
        self.vacancy_id = vacancy_id
        self.company_name = company_name
        self.work_place = work_place
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.experience = experience

        self.info = dict(title=self.title, vacancy_url=self.vacancy_url, vacancy_id=self.vacancy_id,
                         company_name=self.company_name, work_place=self.work_place,
                         salary_from=self.salary_from, salary_to=self.salary_to,
                         salary_currency=self.salary_currency, experience=self.experience)