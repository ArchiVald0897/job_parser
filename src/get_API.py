from abc import ABC, abstractmethod
import requests
from vacancies import Vacancies
from seve_json import JSON_save


class API(ABC):

    @abstractmethod
    def search_vacancies(self, keyword, quantity=15):
        """получение вакансий по API"""
        pass

    @abstractmethod
    def get_info(self, response):
        """Получение информации по вакансии"""
        pass


class HHAPI(API):
    """Поиск вакансий на HeadHunter"""
    hh_url = 'https://api.hh.ru/vacancies'

    def search_vacancies(self, keyword, quantity=15, page=1):
        """Подключение к API HeadHunter"""
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,
            "per_page": quantity,
            "only_with_salary": 'true'
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            vacancies = response.json().get("items")
            return vacancies
        else:
            print(f"Не удалось выполнить запрос к API HeadHunter")

    def vacancies_info(self, vacancies):
        """Получение информации для создания класса Vacancies"""

        for vacancy in vacancies:
            title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            vacancy_id = vacancy.get("id")
            company_name = vacancy.get("employer").get("name")
            work_place = vacancy.get("area").get("name")
            salary_from = vacancy.get("salary").get("from")

            if salary_from is None:
                salary_from = 0

            salary_to = vacancy.get("salary").get("to")

            if salary_to is None:
                salary_to = 0

            salary_currency = vacancy.get("salary").get("currency")
            experience = vacancy.get("experience").get("name")

            vac = Vacancies(title, vacancy_url, vacancy_id, company_name, work_place,
                            salary_from, salary_to, salary_currency, experience)
            print("----------------------------------------------------------------------------------------------")
            print(vac)
            user_answer = input("Добавить вакансию? (Да/Нет) ").lower()
            if user_answer == "да" or user_answer == "yes" or user_answer == "lf":
                my_object = JSON_save()
                my_object.add_vacancy(vac.info)
            elif user_answer == "стоп" or user_answer == "stop":
                break
            else:
                continue
