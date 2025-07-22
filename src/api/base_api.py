from abc import ABC, abstractmethod
from typing import List, Dict


class BaseAPI(ABC):
    """
    Абстрактный базовый класс для API-клиентов.
    Определяет интерфейс подключения и получения данных.
    """

    @abstractmethod
    def _connect(self, **kwargs) -> Dict:
        """
        Приватный метод подключения к API.
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Метод получения вакансий по ключевому слову.
        :param keyword: строка для поиска вакансий
        :return: список словарей с вакансиями
        """
        pass
