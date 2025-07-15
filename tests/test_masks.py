import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234-5678-9012-3456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Тест функции маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "123456789012345",  # 15 цифр
        "1234 5678 901",  # 11 цифр
        "",  # пустая строка
    ],
)
def test_get_mask_card_number_invalid(card_number: str) -> None:
    """Тест функции маскировки номера карты с некорректными данными"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account, expected",
    [
        ("1234567890", "**7890"),
        ("1234 5678 90", "**7890"),
        ("1234-5678-90", "**7890"),
    ],
)
def test_get_mask_account(account: str, expected: str) -> None:
    """Тест функции маскировки номера счета"""
    assert get_mask_account(account) == expected


@pytest.mark.parametrize(
    "account",
    [
        "123",  # 3 цифры
        "12",  # 2 цифры
        "",  # пустая строка
    ],
)
def test_get_mask_account_invalid(account: str) -> None:
    """Тест функции маскировки номера счета с некорректными данными"""
    with pytest.raises(ValueError):
        get_mask_account(account)
