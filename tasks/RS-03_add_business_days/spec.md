# RS-03 · Add business days

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def add_business_days(start: date, n: int, holidays: set) -> date:
```

## Rules

Count forward `n` business days from `start`.

1. A business day is Monday to Friday and not in `holidays` (a set of `datetime.date`).
2. `start` itself is never counted. Day 1 is the first business day **after** `start`, whether or not `start` is a business day.
3. If `n` is 0, return `start` if it is a business day, otherwise the next business day.
4. If `n` is negative, raise `ValueError`.

## Examples

These are the visible tests. Your agent may see and use them.

```python
add_business_days(date(2026, 11, 25), 1, {date(2026, 11, 26), date(2026, 12, 25), date(2027, 1, 1)})
# -> date(2026, 11, 27)

add_business_days(date(2026, 11, 27), 1, set())
# -> date(2026, 11, 30)

add_business_days(date(2026, 11, 28), 0, set())
# -> date(2026, 11, 30)
```
