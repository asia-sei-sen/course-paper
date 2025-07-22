from abc import ABC, abstractmethod
from typing import List
from src.models.vacancy import Vacancy


class BaseSaver(ABC):
    """
    Абстрактный класс для сохранения и получения вакансий.
    Определяет интерфейс для работы с файлами или БД.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавить вакансию в хранилище.
        """
        pass

    @abstractmethod
    def get_vacancies(self, **filters) -> List[Vacancy]:
        """
        Получить вакансии из хранилища по заданным фильтрам.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удалить вакансию из хранилища.
        """
        pass
