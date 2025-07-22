import json
from typing import List, Optional
from pathlib import Path

from src.storage.base_saver import BaseSaver
from src.models.vacancy import Vacancy


class JSONSaver(BaseSaver):
    """
    Класс для работы с JSON-файлом для хранения вакансий.
    """

    def __init__(self, filename: Optional[str] = None):
        self.__filename = filename or Path("data/vacancies.json")
        if isinstance(self.__filename, str):
            self.__filename = Path(self.__filename)

        # Создаём файл, если нет
        if not self.__filename.exists():
            self.__filename.parent.mkdir(parents=True, exist_ok=True)
            self.__filename.write_text("[]", encoding="utf-8")

    def __read_file(self) -> List[Vacancy]:
        """
        Считывает вакансии из файла и возвращает список объектов Vacancy.
        """
        with self.__filename.open(encoding="utf-8") as f:
            data = json.load(f)
        return [Vacancy.from_dict(item) for item in data]

    def __write_file(self, vacancies: List[Vacancy]) -> None:
        """
        Записывает список вакансий в файл.
        """
        data = [vac.to_dict() for vac in vacancies]
        with self.__filename.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавляет вакансию, если её нет в файле.
        """
        vacancies = self.__read_file()
        if not any(v.url == vacancy.url for v in vacancies):
            vacancies.append(vacancy)
            self.__write_file(vacancies)

    def get_vacancies(self, **filters) -> List[Vacancy]:
        """
        Возвращает вакансии, можно фильтровать по ключам.
        Если фильтры не заданы — возвращает все.
        """
        vacancies = self.__read_file()

        def matches(vac: Vacancy) -> bool:
            for key, value in filters.items():
                attr = getattr(vac, key, None)
                if attr != value:
                    return False
            return True

        return [vac for vac in vacancies if matches(vac)]

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию из файла.
        """
        vacancies = self.__read_file()
        vacancies = [v for v in vacancies if v.url != vacancy.url]
        self.__write_file(vacancies)
