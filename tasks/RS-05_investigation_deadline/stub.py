from decimal import Decimal
from datetime import date, datetime, timezone


def investigation_deadline(notice_date: date, first_deposit_date, is_pos: bool, is_foreign: bool) -> date:
    raise NotImplementedError
