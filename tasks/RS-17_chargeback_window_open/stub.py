from decimal import Decimal
from datetime import date, datetime, timezone


def chargeback_window_open(reason: str, transaction_date: date, dispute_date: date, expected_delivery_date=None) -> bool:
    raise NotImplementedError
