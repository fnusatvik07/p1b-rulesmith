# RS-04 · Provisional credit deadline (Reg E)

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def provisional_credit_deadline(notice_date: date, first_deposit_date, holidays: set) -> date:
```

## Rules

When a customer reports an error on a debit card or electronic transfer, Harborline must decide quickly or give the money back provisionally. This function returns the last day to give provisional credit.

1. The normal deadline is **10 business days** after `notice_date`.
2. For a **new account**, the deadline is **20 business days** after `notice_date`. An account is new if the notice arrives within 30 days after the first deposit: `0 <= (notice_date - first_deposit_date).days <= 30`.
3. `first_deposit_date` may be `None`. Then the account is not new.
4. Count business days exactly as in RS-03: weekends and `holidays` are skipped, and `notice_date` itself is never counted.

## Examples

These are the visible tests. Your agent may see and use them.

```python
provisional_credit_deadline(date(2026, 11, 25), date(2020, 1, 1), {date(2026, 11, 26)})
# -> date(2026, 12, 10)

provisional_credit_deadline(date(2026, 11, 25), date(2026, 11, 10), {date(2026, 11, 26)})
# -> date(2026, 12, 24)

provisional_credit_deadline(date(2026, 11, 25), None, {date(2026, 11, 26)})
# -> date(2026, 12, 10)
```
