# tests/test_main.py
import pytest
from unittest.mock import patch
from src.main import user_interaction

def test_user_interaction_runs():
    inputs = [
        "Python",   # поисковый запрос
        "3",        # топ N вакансий
        "Django Flask",  # ключевые слова фильтрации
        "100000-200000"  # диапазон зарплат
    ]

    with patch('builtins.input', side_effect=inputs):
        # Запускаем функцию, проверяем, что она не выбросит исключений
        user_interaction()
