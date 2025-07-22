import pytest
from src.models.vacancy import Vacancy


def test_vacancy_creation_and_validation():
    vac = Vacancy(" Dev ", " http://example.com ", 100000, " Test description ")
    assert vac.title == "Dev"
    assert vac.url == "http://example.com"
    assert vac.salary == 100000
    assert vac.description == "Test description"

    vac2 = Vacancy("", "", -10, "")
    assert vac2.title == "Без названия"
    assert vac2.url == "https://hh.ru"
    assert vac2.salary == 0
    assert vac2.description == "Описание отсутствует"


def test_comparison():
    vac1 = Vacancy("A", "url1", 100, "desc")
    vac2 = Vacancy("B", "url2", 200, "desc")
    vac3 = Vacancy("C", "url3", 100, "desc")

    assert (vac1 == vac3) is True
    assert (vac1 < vac2) is True
    assert (vac2 > vac1) is True
