# RS-08 · Tiered savings interest

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def annual_interest(balance: Decimal, tiers: list) -> Decimal:
```

## Rules

Harborline's tiered savings account pays a different rate on each slice of the balance (like tax brackets).

1. `tiers` is a list of `(upper_bound, rate_percent)`. `upper_bound` is a `Decimal` or `None` (no upper limit). `rate_percent` is a string such as `"2.00"`.
2. The tiers can arrive **in any order**. Sort them by upper bound, with `None` last.
3. Each rate applies only to the part of the balance inside its slice. Example with tiers up to 10,000 at 1%, up to 50,000 at 2%, above at 3%: a balance of 60,000 earns 10,000 x 1% + 40,000 x 2% + 10,000 x 3% = 1,200.00.
4. If `balance` is zero or negative, return `0.00`.
5. Do not round each slice. Add them up and round once at the end to cents, halves up.

## Examples

These are the visible tests. Your agent may see and use them.

```python
annual_interest(Decimal("5000"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")])
# -> Decimal("50.00")

annual_interest(Decimal("60000"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")])
# -> Decimal("1200.00")

annual_interest(Decimal("0"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")])
# -> Decimal("0.00")
```
