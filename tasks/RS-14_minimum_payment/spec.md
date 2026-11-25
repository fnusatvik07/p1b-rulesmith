# RS-14 · Credit card minimum payment

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def minimum_payment(new_balance: Decimal, interest_charged: Decimal, fees_charged: Decimal, past_due: Decimal) -> Decimal:
```

## Rules

The minimum payment printed on a Harborline credit card statement.

1. If `new_balance` is zero or negative, the minimum payment is `0.00`.
2. Start with 1% of `new_balance`, plus `interest_charged`, plus `fees_charged`. Do not round yet.
3. If that is less than $35.00, use $35.00.
4. Add `past_due`.
5. The minimum payment can never be more than `new_balance`. If it would be, it equals `new_balance`.
6. Round once at the end to cents, halves up.

## Examples

These are the visible tests. Your agent may see and use them.

```python
minimum_payment(Decimal("1000.00"), Decimal("10.00"), Decimal("0.00"), Decimal("0.00"))
# -> Decimal("35.00")

minimum_payment(Decimal("5000.00"), Decimal("60.00"), Decimal("40.00"), Decimal("0.00"))
# -> Decimal("150.00")

minimum_payment(Decimal("20.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00"))
# -> Decimal("20.00")
```
