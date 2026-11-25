# RS-10 · ATM daily limit

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def atm_withdrawal_allowed(history: list, amount: Decimal, at: datetime) -> bool:
```

## Rules

Decide whether an ATM withdrawal is allowed.

1. `amount` must be greater than zero and a whole multiple of $20. Otherwise return `False`.
2. The daily limit is **$500.00** per **calendar day in New York time** (`America/New_York`, which observes daylight saving time).
3. `history` is a list of `(timestamp, amount)` for withdrawals already approved. `at` and every timestamp are timezone-aware datetimes in UTC.
4. Add up the approved withdrawals whose New York date equals the New York date of `at`. Allow the new withdrawal only if that total plus `amount` is **$500.00 or less**.

## Examples

These are the visible tests. Your agent may see and use them.

```python
atm_withdrawal_allowed([], Decimal("500"), datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc))
# -> True

atm_withdrawal_allowed([], Decimal("520"), datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc))
# -> False

atm_withdrawal_allowed([], Decimal("30"), datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc))
# -> False
```
