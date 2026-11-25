# RS-17 · Chargeback time limits

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def chargeback_window_open(reason: str, transaction_date: date, dispute_date: date, expected_delivery_date=None) -> bool:
```

## Rules

Can Harborline still raise a chargeback with the card network? Harborline's network rules:

1. `reason` is one of `"fraud"`, `"not_received"`, `"duplicate"`. Anything else: raise `ValueError`.
2. If `dispute_date` is before `transaction_date`, return `False`.
3. `fraud` and `duplicate`: the window is open if `dispute_date` is at most **120 calendar days** after `transaction_date` (day 120 is still open).
4. `not_received` (goods or services never arrived): the 120 days start from `expected_delivery_date` if one is given **and** it is later than `transaction_date`; otherwise from `transaction_date`. But the window can never stay open more than **540 days** after `transaction_date`.

## Examples

These are the visible tests. Your agent may see and use them.

```python
chargeback_window_open("fraud", date(2026, 1, 1), date(2026, 5, 1))
# -> True

chargeback_window_open("fraud", date(2026, 1, 1), date(2026, 5, 2))
# -> False

chargeback_window_open("chargeback", date(2026, 1, 1), date(2026, 2, 1))
# -> ValueError is raised
```
