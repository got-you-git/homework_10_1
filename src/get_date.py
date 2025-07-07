def get_date(date_time: str) -> str:
    """Преобразует дату"""

    times = date_time[: date_time.find("T")].split("-")
    return ".".join(times)
