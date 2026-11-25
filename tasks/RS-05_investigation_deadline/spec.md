# RS-05 · Investigation deadline (Reg E)

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def investigation_deadline(notice_date: date, first_deposit_date, is_pos: bool, is_foreign: bool) -> date:
```

## Rules

The last day Harborline may take to finish investigating an error notice.

1. The normal deadline is **45 calendar days** after `notice_date`.
2. The deadline is **90 calendar days** after `notice_date` if any of these is true:
   - the account is new (same definition as RS-04: `0 <= (notice_date - first_deposit_date).days <= 30`; `None` means not new),
   - the transaction was a point-of-sale debit card transaction (`is_pos`),
   - the transaction was initiated outside the United States (`is_foreign`).
3. These are calendar days. The deadline does **not** move if it lands on a weekend or holiday.

## Examples

These are the visible tests. Your agent may see and use them.

```python
investigation_deadline(date(2026, 11, 25), date(2020, 1, 1), False, False)
# -> date(2027, 1, 9)

investigation_deadline(date(2026, 11, 25), date(2020, 1, 1), True, False)
# -> date(2027, 2, 23)

investigation_deadline(date(2026, 11, 25), None, False, True)
# -> date(2027, 2, 23)
```
