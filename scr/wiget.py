def mask_account_card(input_str: str) -> str:
    '''Функция для маскировки счёта или номера карты'''

    # разделяем строку и создаём отдельные спики
    parts = input_str.split()
    numbers = []
    text_parts = []

    # проверяем каджый символ и добавляем в свой список
    for part in parts:
        if part.isdigit():
            numbers.append(part)
        else:
            text_parts.append(part)

    number = ''.join(numbers)
    text = ' '.join(text_parts)

    # маскируем счёт или номер карты
    if len(number) == 16:
        masked_card = f"{text} {number[:4]} {number[4:6]}** **** {number[-4:]}"
        return masked_card
    else:
        masked_account = f"{text} **{number[-4:]}"
        return masked_account