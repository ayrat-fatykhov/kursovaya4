import json
from abc import ABC, abstractmethod

from src.settings import HH_PATH, SJ_PATH


class JSONSaver(ABC):
    """Интерфейс для классов, которые будут работать с данными в формате json"""

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_from):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class HHJSONSaver(JSONSaver):
    """Класс для работы с json данными из платформы HH"""

    def __init__(self, date: list[dict]):
        """Инициализирует атрибуты класса"""
        self.date: list[dict] = date

    def add_vacancies(self) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Vacancy"""
        with open(HH_PATH, 'w', encoding="utf-8") as file:
            json.dump(self.date, file, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary_from: int) -> None:
        """Отбирает вакансии по желаемой зп"""
        with open(HH_PATH, encoding="utf-8") as file:
            vacancies = json.load(file)
        for v in vacancies:
            if v['salary_from'] >= salary_from:
                print(f"{v['name']}\n{v['url']}\n")

    def delete_vacancy(self):
        pass


class SJJSONSaver(JSONSaver):
    """Класс для работы с json данными из платформы SuperJob"""

    def __init__(self, date: list[dict]):
        """Инициализирует атрибуты класса"""
        self.date = date

    def add_vacancies(self):
        """Сохраняет в файл значения атрибутов экземпляра Vacancy"""
        with open(SJ_PATH, 'w', encoding="utf-8") as file:
            json.dump(self.date, file, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary_from: int) -> None:
        """Отбирает вакансии по желаемой зп"""
        with open(SJ_PATH, encoding="utf-8") as file:
            vacancies = json.load(file)
        for v in vacancies:
            if v['salary_from'] >= salary_from:
                print(f"{v['name']}\n{v['url']}\n")

    def delete_vacancy(self):
        pass
