def mask_account_card(input_str: str) -> str:
    """Функция для маскировки счёта или номера карты"""
    parts = input_str.split()
    numbers = []
    text_parts = []

    for part in parts:
        # Извлекаем только цифры из каждой части
        digits = "".join(filter(str.isdigit, part))
        if digits:
            numbers.append(digits)
        else:
            text_parts.append(part)

    number = "".join(numbers)
    text = " ".join(text_parts)

    if not number:  # Если цифр нет, возвращаем исходную строку
        return input_str

    if len(number) == 16:
        masked_card = f"{text} {number[:4]} {number[4:6]}** **** {number[-4:]}"
        return masked_card.strip()
    else:
        masked_account = f"{text} **{number[-4:]}"
        return masked_account.strip()


def get_date(date_time: str) -> str:
    """Преобразует дату из формата YYYY-MM-DD в DD.MM.YYYY"""
    if not date_time:
        return ""

    # Ищем дату в формате YYYY-MM-DD
    date_part = ""
    for i, char in enumerate(date_time):
        if char.isdigit() or char == "-":
            date_part += char
        else:
            # Прерываем при первом нецифровом символе (кроме '-')
            break

    parts = date_part.split("-")
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        year, month, day = parts
        return f"{day}.{month}.{year}"

    return date_time
