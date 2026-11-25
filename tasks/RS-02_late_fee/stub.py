from decimal import Decimal
from datetime import date, datetime, timezone


def late_fee(min_payment_due: Decimal, amount_paid: Decimal, days_late: int, late_in_prior_6_cycles: bool) -> Decimal:
    raise NotImplementedError
