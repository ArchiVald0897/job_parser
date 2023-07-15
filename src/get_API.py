from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def search_vacancies(self, keyword, quantity=15):
        """получение вакансий по API"""
        pass

    @abstractmethod
    def get_info(self, response):
        """Получение информации по вакансии"""
        pass
