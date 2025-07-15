from datetime import datetime

import pytest

from src.processing import filter_by_state, sort_by_date

SAMPLE_TRANSACTIONS = [
    {"id": 1, "state": "EXECUTED", "date": "2023-10-05T12:30:45"},
    {"id": 2, "state": "PENDING", "date": "2023-09-15T08:12:30"},
    {"id": 3, "state": "EXECUTED", "date": "2023-10-10T15:45:00"},
    {"id": 4, "state": "CANCELED", "date": "2023-08-20T10:00:00"},
    {"id": 5, "state": "EXECUTED", "date": "2023-10-10T10:30:00"},  # Та же дата как у id=3
]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 5]),
        ("PENDING", [2]),
        ("CANCELED", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(state: str, expected_ids: list[int]) -> None:
    """Тестирование фильтрации по статусу"""
    filtered = filter_by_state(SAMPLE_TRANSACTIONS, state)
    assert [t["id"] for t in filtered] == expected_ids


def test_filter_by_state_default() -> None:
    """Тестирование фильтрации со статусом по умолчанию (EXECUTED)"""
    filtered = filter_by_state(SAMPLE_TRANSACTIONS)
    assert [t["id"] for t in filtered] == [1, 3, 5]


@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (True, [3, 5, 1, 2, 4]),  # По убыванию (новые сначала)
        (False, [4, 2, 1, 5, 3]),  # По возрастанию (старые сначала)
    ],
)
def test_sort_by_date(reverse: bool, expected_order: list[int]) -> None:
    """Тестирование сортировки по дате"""
    sorted_transactions = sort_by_date(SAMPLE_TRANSACTIONS, reverse)
    assert [t["id"] for t in sorted_transactions] == expected_order


def test_sort_by_date_default() -> None:
    """Тестирование сортировки по умолчанию (по убыванию)"""
    sorted_transactions = sort_by_date(SAMPLE_TRANSACTIONS)
    assert [t["id"] for t in sorted_transactions] == [3, 5, 1, 2, 4]


def test_sort_by_date_same_dates() -> None:
    """Тестирование сортировки при одинаковых датах (должны сохранять исходный порядок)"""
    # Добавляем транзакцию с такой же датой как у id=3 и id=5
    test_data = SAMPLE_TRANSACTIONS + [{"id": 6, "state": "EXECUTED", "date": "2023-10-10T15:45:00"}]
    sorted_transactions = sort_by_date(test_data)
    # Проверяем что id=3 и id=6 идут последовательно (сохраняют порядок)
    sorted_ids = [t["id"] for t in sorted_transactions]
    assert sorted_ids.index(3) < sorted_ids.index(6)


@pytest.mark.parametrize(
    "date_str",
    [
        "2023-12-31T23:59:59",  # Корректный формат
        "2023-12-31",  # Без времени
        "31.12.2023",  # Другой формат даты
        "INVALID_DATE",  # Невалидная дата
    ],
)
def test_sort_with_different_date_formats(date_str: str) -> None:
    """Тестирование сортировки с разными форматами дат"""
    test_data = SAMPLE_TRANSACTIONS + [{"id": 99, "state": "EXECUTED", "date": date_str}]

    try:
        # Пытаемся преобразовать дату для проверки валидности
        datetime.fromisoformat(date_str.replace("T", " "))
        is_valid = True
    except ValueError:
        is_valid = False

    if is_valid:
        sorted_transactions = sort_by_date(test_data)
        sorted_dates = [t["date"] for t in sorted_transactions]
        assert date_str in sorted_dates
    else:
        # Для невалидных дат проверяем что функция не падает
        sort_by_date(test_data)
