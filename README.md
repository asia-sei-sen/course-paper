# Course Paper: Вакансии с hh.ru (API + Python)

Курсовой проект по Python — интеграция с API hh.ru, обработка вакансий, фильтрация и сохранение в JSON.

## 📦 Описание

Программа выполняет:

* Получение вакансий с hh.ru по ключевым словам.
* Сохранение результатов в JSON.
* Фильтрацию по зарплате, ключевым словам и локации.
* Сравнение и сортировку вакансий.
* Тестирование с покрытием `pytest`.

## 🧱 Архитектура

```
course-paper/
├── src/
│   ├── api/
│   │   └── hh_api.py
│   ├── models/
│   │   └── vacancy.py
│   ├── utils/
│   │   └── filters.py
│   └── json_saver.py
├── tests/
│   ├── test_hh_api.py
│   ├── test_json_saver.py
│   ├── test_utils_filters.py
│   └── test_vacancy.py
├── main.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## 🛠️ Использование

```bash
python main.py
```

## 🧪 Тестирование

```bash
pytest --cov=src --cov-report=term-missing
```

## 📌 Требования

Установить зависимости:

```bash
pip install -r requirements.txt
```

## 🪪 Лицензия

MIT License

---

## ✨ Автор

Asia Sei Sen
Курсовая работа, 2025
