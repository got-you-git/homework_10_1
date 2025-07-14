import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        # Стандартный 16-значный номер карты
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("1234-5678-1234-5678", "1234 56** **** 5678"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "123456789012",
        "",
        "abcdefghijklmnop",
        None,
    ],
)
def test_get_mask_card_number_invalid(card_number):
    with pytest.raises((ValueError, TypeError)):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account, expected",
    [
        # Стандартные номера счетов
        ("1234567890123456", "**3456"),
        ("9876543210", "**3210"),
        ("1234 5678 9012 3456", "**3456"),
        ("12-34-56-78", "**5678"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


@pytest.mark.parametrize(
    "account",
    [
        "123",
        "",
        "ABC123",
        None,
    ],
)
def test_get_mask_account_invalid(account):
    with pytest.raises((ValueError, TypeError)):
        get_mask_account(account)
