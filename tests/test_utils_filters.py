from src.models.vacancy import Vacancy
from src.utils.filters import (
    filter_by_keywords,
    get_top_n,
    sort_by_salary,
    filter_by_salary_range,
)
import pytest


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Dev A", "url1", 100, "Python developer"),
        Vacancy("Dev B", "url2", 200, "Java developer"),
        Vacancy("Dev C", "url3", 0, "No salary info"),
        Vacancy("Dev D", "url4", 150, "Python, Java"),
    ]


def test_filter_by_keywords(sample_vacancies):
    filtered = filter_by_keywords(sample_vacancies, ["Python"])
    assert len(filtered) == 2

    filtered_empty = filter_by_keywords(sample_vacancies, [])
    assert len(filtered_empty) == 4


def test_get_top_n(sample_vacancies):
    top_2 = get_top_n(sample_vacancies, 2)
    assert top_2[0].salary >= top_2[1].salary


def test_sort_by_salary(sample_vacancies):
    sorted_asc = sort_by_salary(sample_vacancies)
    assert sorted_asc[0].salary <= sorted_asc[-1].salary

    sorted_desc = sort_by_salary(sample_vacancies, reverse=True)
    assert sorted_desc[0].salary >= sorted_desc[-1].salary


def test_filter_by_salary_range(sample_vacancies):
    filtered = filter_by_salary_range(sample_vacancies, min_salary=100, max_salary=150)
    salaries = [v.salary for v in filtered]
    assert all(100 <= s <= 150 for s in salaries)
