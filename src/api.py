import os
from abc import ABC, abstractmethod

import requests


class InterfaceAPI(ABC):
    """Интерфейс для классов с запросом к API"""

    @abstractmethod
    def get_response(self, profession):
        pass


class HeadHunterAPI(InterfaceAPI):
    """Класс для запросов в API HH"""

    def get_response(self, profession: str) -> list[dict]:
        """Получает вакансии из API HH"""
        params: dict = {
            "text": f"name:{profession}"
        }
        response = requests.get("https://api.hh.ru/vacancies", params)
        return response.json()


class SuperJobAPI(InterfaceAPI):
    """Класс для запросов в API SuperJob"""

    def get_response(self, profession: str) -> list[dict]:
        """Получает вакансии из API SuperJob"""
        api_key: str = os.getenv('SUPER_JOB_API_KEY')
        headers: dict = {
            "X-Api-App-Id": api_key
        }
        params: dict = {
            "keyword": profession
        }
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers)
        return response.json()
