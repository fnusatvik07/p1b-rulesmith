# RS-15 · Card cashback rewards

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def cashback(transactions: list) -> Decimal:
```

## Rules

Cashback on the Harborline Everyday card.

1. `transactions` is a list of `(date, category, amount)`. Positive amounts are purchases. Negative amounts are refunds. Category names are compared case-insensitively.
2. Rates: `dining` 3% on the first $1,500.00 of net dining spend **per calendar quarter** (Jan–Mar, Apr–Jun, Jul–Sep, Oct–Dec), then 1% above that. `grocery` 2%. Every other category 1%.
3. Work out the **net** spend (purchases minus refunds) per category per quarter. If a net amount is zero or negative, it earns nothing (no negative cashback).
4. Add up everything, then round the total **down** to cents (truncate). Return a `Decimal` with two decimal places.

## Examples

These are the visible tests. Your agent may see and use them.

```python
cashback([(date(2026, 11, 1), "dining", Decimal("100.00")), (date(2026, 11, 2), "grocery", Decimal("50.00")), (date(2026, 11, 3), "fuel", Decimal("20.00"))])
# -> Decimal("4.20")

cashback([(date(2026, 11, 1), "dining", Decimal("2000.00"))])
# -> Decimal("50.00")

cashback([])
# -> Decimal("0.00")
```
