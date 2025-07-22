from typing import Optional


class Vacancy:
    """
    Класс, представляющий вакансию.
    Содержит основные атрибуты вакансии и поддерживает сравнение по зарплате.
    """

    __slots__ = ("__title", "__url", "__salary", "__description")

    def __init__(self, title: str, url: str, salary: Optional[int], description: str) -> None:
        """
        Инициализация экземпляра вакансии.
        :param title: название вакансии
        :param url: ссылка на вакансию
        :param salary: зарплата в числовом виде
        :param description: краткое описание вакансии
        """
        self.__title = self.__validate_title(title)
        self.__url = self.__validate_url(url)
        self.__salary = self.__validate_salary(salary)
        self.__description = self.__validate_description(description)

    # --- Приватные методы валидации ---

    def __validate_title(self, title: str) -> str:
        return title.strip() if title else "Без названия"

    def __validate_url(self, url: str) -> str:
        return url.strip() if url else "https://hh.ru"

    def __validate_salary(self, salary: Optional[int]) -> int:
        return salary if isinstance(salary, int) and salary > 0 else 0

    def __validate_description(self, desc: str) -> str:
        return desc.strip() if desc else "Описание отсутствует"

    # --- Геттеры (если нужно обращаться к атрибутам) ---

    @property
    def title(self) -> str:
        return self.__title

    @property
    def url(self) -> str:
        return self.__url

    @property
    def salary(self) -> int:
        return self.__salary

    @property
    def description(self) -> str:
        return self.__description

    # --- Магические методы сравнения по зарплате ---

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __repr__(self) -> str:
        return f"<Vacancy {self.title} — {self.salary}₽>"

    def to_dict(self) -> dict:
        """
        Представление вакансии в виде словаря (для сохранения в файл).
        """
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Vacancy":
        """
        Создаёт экземпляр Vacancy из словаря.
        """
        return cls(
            title=data.get("title"),
            url=data.get("url"),
            salary=data.get("salary"),
            description=data.get("description")
        )
