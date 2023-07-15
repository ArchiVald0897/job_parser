from abc import ABC, abstractmethod
import requests


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
