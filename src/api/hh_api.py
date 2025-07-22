import requests
from typing import List, Dict

from src.api.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с API сайта hh.ru.
    Наследуется от абстрактного класса BaseAPI.
    """

    __BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        """
        Инициализация клиента HH API.
        """
        pass  # можно добавить логирование, headers и т.д.

    def _connect(self, **kwargs) -> Dict:
        """
        Отправляет запрос к API hh.ru.
        :param kwargs: параметры запроса
        :return: JSON-ответ
        """
        response = requests.get(self.__BASE_URL, params=kwargs)
        if response.status_code != 200:
            raise ConnectionError(f"Ошибка подключения: {response.status_code}")
        return response.json()

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Получает список вакансий по ключевому слову.
        :param keyword: поисковый запрос
        :return: список вакансий (словарей)
        """
        params = {
            "text": keyword,
            "per_page": 50,  # можно увеличить
        }
        data = self._connect(**params)
        return data.get("items", [])
