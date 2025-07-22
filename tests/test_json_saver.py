import pytest
import tempfile
from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver


@pytest.fixture
def temp_json_file():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json") as f:
        yield f.name


def test_add_and_get_vacancies(temp_json_file):
    saver = JSONSaver(filename=temp_json_file)
    vac1 = Vacancy("Dev1", "url1", 100, "desc1")
    vac2 = Vacancy("Dev2", "url2", 200, "desc2")

    saver.add_vacancy(vac1)
    saver.add_vacancy(vac2)
    # Повторный добавление дубликата не должно влиять
    saver.add_vacancy(vac1)

    vacancies = saver.get_vacancies()
    assert len(vacancies) == 2

    urls = [v.url for v in vacancies]
    assert "url1" in urls and "url2" in urls


def test_delete_vacancy(temp_json_file):
    saver = JSONSaver(filename=temp_json_file)
    vac1 = Vacancy("Dev1", "url1", 100, "desc1")

    saver.add_vacancy(vac1)
    saver.delete_vacancy(vac1)

    vacancies = saver.get_vacancies()
    assert len(vacancies) == 0
