class Vacancy:
    """Класс для работы с вакансиями"""
    all: list = []

    def __init__(self, profession: str, url: str, salary_from: int, salary_to: int, snippet: str):
        """Инициализирует атрибуты класса"""
        self.profession = profession
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.snippet = snippet
        Vacancy.all.append(self)

    def __str__(self):
        """Выводит информацию для пользователя"""
        return f"""{self.profession}
                   \rСсылка: {self.url}
                   \rЗарплата от {self.salary_from} до {self.salary_to} руб.
                   \rОписание: {self.snippet}"""

    def __add__(self, other) -> int:
        """Возвращает результат сложения количества подписчиков"""
        return int(self.salary_from) + int(other.salary_from)

    def __sub__(self, other) -> int:
        """Возвращает результат вычитания количества подписчиков"""
        return int(self.salary_from) - int(other.salary_from)

    def __gt__(self, other) -> bool:
        """Возвращает результат сравнения (меньше) количества подписчиков"""
        return int(self.salary_from) > int(other.salary_from)

    def __ge__(self, other) -> bool:
        """Возвращает результат сравнения (меньше или равно) количества подписчиков"""
        return int(self.salary_from) >= int(other.salary_from)

    def __lt__(self, other) -> bool:
        """Возвращает результат сравнения (больше) количества подписчиков"""
        return int(self.salary_from) < int(other.salary_from)

    def __le__(self, other) -> bool:
        """Возвращает результат сравнения (больше или равно) количества подписчиков"""
        return int(self.salary_from) <= int(other.salary_from)

    def __eq__(self, other) -> bool:
        """Возвращает результат сравнения (равно) количества подписчиков"""
        return int(self.salary_from) == int(other.salary_from)

    @classmethod
    def instantiate_vacancies(cls, vacancies) -> None:
        """Инициализируют экземпляры класса Vacancy данными из запроса на ресурс"""
        cls.all.clear()
        for vacancy in vacancies:
            Vacancy(
                profession=vacancy['name'],
                url=vacancy['url'],
                salary_from=vacancy['salary_from'],
                salary_to=vacancy['salary_to'],
                snippet=vacancy['snippet']
            )
