def get_mask_card_number(cart_number: str) -> str:
    """Функцию маскировки номера банковской карты"""

    masked_card = f"{cart_number[:4]} {cart_number[4:6]}** **** {cart_number[-4:]}"
    return masked_card


def get_mask_account(account: str) -> str:
    """Функцию маскировки номера банковского счета"""

    masked_account = f"**{account[-4:]}"
    return masked_account
