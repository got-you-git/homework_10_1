def get_date(date_str: str) -> str:
    """Преобразует дату"""

    # отделяем дату от времени
    date_part = date_str.split("T")[0]
    # разбиваем на компоненты
    year, month, day = date_part.split("-")
    # собираем в нужном формате
    return f"{day}.{month}.{year}"
