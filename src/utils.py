def hh_reformat_response(vacancies) -> list[dict]:
    """
    Переформатирует вакансии с API HH
    :param vacancies: вакансии с API HH
    :return: переформатированные вакансии с API HH
    """
    reformat_vacancies: list = []
    for vacancy in vacancies['items']:
        vacancy_dict: dict = {}
        vacancy_dict['name'] = vacancy['name']
        vacancy_dict['url'] = vacancy['alternate_url']
        if vacancy['salary']:
            if vacancy['salary']['from']:
                vacancy_dict['salary_from'] = vacancy['salary']['from']
            else:
                vacancy_dict['salary_from'] = 0
            if vacancy['salary']['to']:
                vacancy_dict['salary_to'] = vacancy['salary']['to']
            else:
                vacancy_dict['salary_to'] = 0
        else:
            vacancy_dict['salary_from'] = 0
            vacancy_dict['salary_to'] = 0
        vacancy_dict['snippet'] = vacancy['snippet']['requirement'].lower()
        reformat_vacancies.append(vacancy_dict)
    return reformat_vacancies


def sj_reformat_response(vacancies) -> list[dict]:
    """
    Переформатирует вакансии с API SuperJob
    :param vacancies: вакансии с API SuperJob
    :return: переформатированные вакансии с API SuperJob
    """
    reformat_vacancies: list = []
    for vacancy in vacancies['objects']:
        vacancy_dict: dict = {}
        vacancy_dict['name'] = vacancy['profession']
        vacancy_dict['url'] = vacancy['link']
        vacancy_dict['salary_from'] = vacancy['payment_from']
        vacancy_dict['salary_to'] = vacancy['payment_to']
        vacancy_dict['snippet'] = vacancy['candidat'].lower()
        reformat_vacancies.append(vacancy_dict)
    return reformat_vacancies


def filter_vacancies(vacancies, words):
    """
    Фильтрует вакансии по ключевому слову
    :param vacancies: вакансии
    :param words: ключевое слово
    :return: отфильтрованне вакансии
    """
    all_filter_vacancies = []
    for vacancy in vacancies:
        if words in vacancy['snippet']:
            all_filter_vacancies.append(vacancy)
    return all_filter_vacancies
