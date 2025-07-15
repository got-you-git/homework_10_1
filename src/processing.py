def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями
    :param state: Значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список словарей
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате (ключ 'date').

    :param transactions: Список словарей с транзакциями
    :param reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)
    :return: Отсортированный список словарей
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
