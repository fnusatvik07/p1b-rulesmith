# RS-13 · Round-up savings

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def round_up_total(transactions: list, year: int, month: int) -> Decimal:
```

## Rules

Harborline's round-up feature moves spare change into savings.

1. `transactions` is a list of `(date, amount)`. Negative amounts are card purchases (debits). Positive amounts are credits and are ignored.
2. Only count transactions in the given `year` and `month`.
3. Each debit is rounded up to the next whole dollar, and the difference is saved. A debit of $3.25 saves $0.75.
4. A debit that is already a whole dollar amount (for example $4.00) saves **nothing** (not $1.00).
5. The total saved in a month is capped at **$100.00**.
6. Return a `Decimal` with two decimal places.

## Examples

These are the visible tests. Your agent may see and use them.

```python
round_up_total([(date(2026, 11, 2), Decimal("-3.25")), (date(2026, 11, 3), Decimal("-4.00")), (date(2026, 11, 4), Decimal("-0.01"))], 2026, 11)
# -> Decimal("1.74")

round_up_total([(date(2026, 11, 2), Decimal("20.00"))], 2026, 11)
# -> Decimal("0.00")

round_up_total([], 2026, 11)
# -> Decimal("0.00")
```
