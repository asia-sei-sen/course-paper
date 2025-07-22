from typing import List, Optional
from src.models.vacancy import Vacancy


def filter_by_keywords(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """
    Фильтрует вакансии по наличию хотя бы одного из ключевых слов в описании.
    :param vacancies: список вакансий
    :param keywords: ключевые слова для фильтрации
    :return: отфильтрованный список вакансий
    """
    if not keywords:
        return vacancies
    keywords_lower = [kw.lower() for kw in keywords]
    return [
        vac for vac in vacancies
        if any(kw in vac.description.lower() for kw in keywords_lower)
    ]


def get_top_n(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """
    Возвращает топ N вакансий по зарплате (от высокой к низкой).
    :param vacancies: список вакансий
    :param n: количество вакансий
    :return: топ N вакансий
    """
    sorted_vacs = sorted(vacancies, key=lambda v: v.salary, reverse=True)
    return sorted_vacs[:n]


def sort_by_salary(vacancies: List[Vacancy], reverse: bool = False) -> List[Vacancy]:
    """
    Сортирует вакансии по зарплате.
    :param vacancies: список вакансий
    :param reverse: если True — по убыванию
    :return: отсортированный список вакансий
    """
    return sorted(vacancies, key=lambda v: v.salary, reverse=reverse)


def filter_by_salary_range(
    vacancies: List[Vacancy],
    min_salary: Optional[int] = None,
    max_salary: Optional[int] = None
) -> List[Vacancy]:
    """
    Фильтрует вакансии по диапазону зарплат.
    :param vacancies: список вакансий
    :param min_salary: минимальная зарплата (включительно)
    :param max_salary: максимальная зарплата (включительно)
    :return: отфильтрованный список вакансий
    """
    def in_range(salary: int) -> bool:
        if min_salary is not None and salary < min_salary:
            return False
        if max_salary is not None and salary > max_salary:
            return False
        return True

    return [vac for vac in vacancies if in_range(vac.salary)]


def pretty_print(vacancies: List[Vacancy]) -> None:
    """
    Человекочитаемый вывод списка вакансий в консоль.
    """
    if not vacancies:
        print("Вакансии не найдены.")
        return

    for i, vac in enumerate(vacancies, 1):
        print(f"{i}. {vac.title}")
        print(f"   Зарплата: {vac.salary if vac.salary > 0 else 'Не указана'} ₽")
        print(f"   Ссылка: {vac.url}")
        print(f"   Описание: {vac.description[:150]}{'...' if len(vac.description) > 150 else ''}")
        print("-" * 50)
