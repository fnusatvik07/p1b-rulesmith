# RS-02 · Late payment fee

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def late_fee(min_payment_due: Decimal, amount_paid: Decimal, days_late: int, late_in_prior_6_cycles: bool) -> Decimal:
```

## Rules

Harborline's credit card late fee.

1. If `days_late` is 0 or less, there is no fee.
2. If `min_payment_due` is 0 or less, there is no fee.
3. Harborline's tolerance rule: if the shortfall (`min_payment_due - amount_paid`) is **$1.00 or less**, the payment counts as made and there is no fee. Paying more than the minimum is also no fee.
4. Otherwise the fee is $30.00, or $41.00 if the customer was also late in any of the prior 6 billing cycles.
5. The fee can never be higher than `min_payment_due`. If it would be, the fee equals `min_payment_due`.
6. Return a `Decimal` with two decimal places.

## Examples

These are the visible tests. Your agent may see and use them.

```python
late_fee(Decimal("35.00"), Decimal("0.00"), 5, False)
# -> Decimal("30.00")

late_fee(Decimal("50.00"), Decimal("0.00"), 5, True)
# -> Decimal("41.00")

late_fee(Decimal("35.00"), Decimal("35.00"), 5, False)
# -> Decimal("0.00")
```
