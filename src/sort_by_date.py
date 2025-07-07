def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате (ключ 'date').

    :param transactions: Список словарей с транзакциями
    :param reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)
    :return: Отсортированный список словарей
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
