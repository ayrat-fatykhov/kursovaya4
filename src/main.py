from src.api import HeadHunterAPI, SuperJobAPI
from src.jsonsaver import HHJSONSaver, SJJSONSaver
from src.utils import filter_vacancies, hh_reformat_response, sj_reformat_response
from src.vacancy import Vacancy


def user_interaction() -> None:
    """
    Принимает параметры пользователя и выдает результат
    :return: None
    """
    platforms: int = int(input("1 - HeadHunter,\n2 - SuperJob\nВведите число, соответствующее платформе: "))
    if platforms == 1 or platforms == 2:
        vacancies: list = []
        search_query: str = input("Введите поисковый запрос: ").lower()
        if platforms == 1:
            hh_api: HeadHunterAPI = HeadHunterAPI()
            hh_vacancies: list[dict] = hh_api.get_response(search_query)
            vacancies: list[dict] = hh_reformat_response(hh_vacancies)
            save_json: HHJSONSaver = HHJSONSaver(vacancies)
            save_json.add_vacancies()
        elif platforms == 2:
            sj_api: SuperJobAPI = SuperJobAPI()
            sj_vacancies: list[dict] = sj_api.get_response(search_query)
            vacancies: list[dict] = sj_reformat_response(sj_vacancies)
            save_json: SJJSONSaver = SJJSONSaver(vacancies)
            save_json.add_vacancies()
        filter_words: str = input("Введите ключевое слово для фильтрации вакансий (например, postgres): ").lower()
        filtered_vacancies: list[dict] = filter_vacancies(vacancies, filter_words)
        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
            return
        Vacancy.instantiate_vacancies(filtered_vacancies)
        Vacancy.all.sort(reverse=True)
        top_vacancies: int = int(input("Введите число для выведения ТОП вакансий: "))
        if len(Vacancy.all) <= top_vacancies:
            for i in range(len(Vacancy.all)):
                print(f'Вакансия N{i + 1}\n{Vacancy.all[i]}\n')
        else:
            for i in range(top_vacancies):
                print(f'Вакансия N{i + 1}\n{Vacancy.all[i]}\n')
    else:
        print("Увы... такой платформы нет")


if __name__ == "__main__":
    user_interaction()
