from typing import Optional

from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver
from src.utils.filters import (
    filter_by_keywords,
    filter_by_salary_range,
    get_top_n,
    pretty_print,
)


def user_interaction() -> None:
    """
    Основная функция взаимодействия с пользователем.
    Запрашивает ключевое слово, количество вакансий, фильтры и выводит результаты.
    """

    print("Привет! Поиск вакансий на hh.ru")
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    query = input("Введите поисковый запрос: ").strip()
    if not query:
        print("Запрос не может быть пустым.")
        return

    print("Получаем вакансии с hh.ru...")
    vacancies_data = hh_api.get_vacancies(query)

    # Преобразуем словари в объекты Vacancy
    vacancies = [Vacancy.from_dict(vac) for vac in vacancies_data]

    # Сохраняем вакансии (без дублей)
    for vac in vacancies:
        json_saver.add_vacancy(vac)

    # Загружаем все вакансии из файла (можно фильтровать дальше)
    all_vacancies = json_saver.get_vacancies()

    # Фильтрация по ключевым словам в описании
    keywords_input = input("Введите ключевые слова для фильтрации (через пробел), или Enter чтобы пропустить: ").strip()
    keywords = keywords_input.split() if keywords_input else []
    filtered_vacancies = filter_by_keywords(all_vacancies, keywords)

    # Фильтрация по зарплате
    salary_min_str = input("Введите минимальную зарплату (или Enter чтобы пропустить): ").strip()
    salary_max_str = input("Введите максимальную зарплату (или Enter чтобы пропустить): ").strip()

    salary_min: Optional[int] = int(salary_min_str) if salary_min_str.isdigit() else None
    salary_max: Optional[int] = int(salary_max_str) if salary_max_str.isdigit() else None

    filtered_vacancies = filter_by_salary_range(filtered_vacancies, salary_min, salary_max)

    # Топ N вакансий по зарплате
    top_n_str = input("Введите количество вакансий для вывода в топ N (или Enter для всех): ").strip()
    top_n: Optional[int] = int(top_n_str) if top_n_str.isdigit() else None

    if top_n is not None and top_n > 0:
        result_vacancies = get_top_n(filtered_vacancies, top_n)
    else:
        result_vacancies = filtered_vacancies

    # Вывод результатов
    print("\nРезультаты поиска:\n")
    pretty_print(result_vacancies)


if __name__ == "__main__":
    user_interaction()
