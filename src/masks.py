def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    # Удаляем все нецифровые символы
    digits = "".join(filter(str.isdigit, card_number))

    # Проверяем минимальную длину
    if len(digits) < 16:
        raise ValueError("Номер карты должен содержать минимум 16 цифр")

    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция маскировки номера банковского счета"""
    # Удаляем все нецифровые символы
    digits = "".join(filter(str.isdigit, account))

    # Проверяем минимальную длину
    if len(digits) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    return f"**{digits[-4:]}"
