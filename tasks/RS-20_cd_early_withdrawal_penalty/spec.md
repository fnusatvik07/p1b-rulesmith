# RS-20 · CD early withdrawal penalty

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def cd_early_withdrawal_penalty(principal: Decimal, annual_rate_percent: str, term_months: int, months_held: int) -> Decimal:
```

## Rules

Penalty for closing a certificate of deposit (CD) before it matures.

1. If `months_held` is equal to or more than `term_months`, the CD has matured: penalty `0.00`.
2. Otherwise the penalty is simple interest on `principal` at `annual_rate_percent` (a string such as `"4.50"`) for a number of days that depends on the **term**:
   - term under 12 months: 90 days,
   - term from 12 to 36 months (both included): 180 days,
   - term over 36 months: 365 days.
3. Penalty = principal x rate / 100 x days / 365. The penalty can be bigger than the interest earned so far; that is allowed.
4. Round once at the end to cents, halves up.

## Examples

These are the visible tests. Your agent may see and use them.

```python
cd_early_withdrawal_penalty(Decimal("10000"), "4.00", 12, 3)
# -> Decimal("197.26")

cd_early_withdrawal_penalty(Decimal("10000"), "4.00", 6, 2)
# -> Decimal("98.63")

cd_early_withdrawal_penalty(Decimal("10000"), "4.00", 12, 12)
# -> Decimal("0.00")
```
