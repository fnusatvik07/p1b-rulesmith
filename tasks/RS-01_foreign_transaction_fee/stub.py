from decimal import Decimal
from datetime import date, datetime, timezone


def foreign_transaction_fee(amount: Decimal, card_tier: str, is_atm: bool, merchant_country: str) -> Decimal:
    raise NotImplementedError
