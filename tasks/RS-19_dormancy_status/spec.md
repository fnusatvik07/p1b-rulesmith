# RS-19 · Dormant account status

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def dormancy_status(account_opened: date, events: list, today: date) -> str:
```

## Rules

Return `"active"`, `"dormant"` or `"escheat_review"` for a deposit account.

1. `events` is a list of `(date, type)`. Only **customer-initiated** events count as activity: `deposit`, `withdrawal`, `transfer`, `login`, `contact`. System events such as `interest`, `fee` and `statement` do **not** count.
2. Ignore events dated after `today`.
3. The last activity date is the latest counting event. If there is none, use `account_opened`.
4. Days inactive = `(today - last_activity).days`.
   - 1,095 or more: `"escheat_review"` (the account may have to be handed to the state as unclaimed property).
   - 365 or more: `"dormant"`.
   - Otherwise: `"active"`.

## Examples

These are the visible tests. Your agent may see and use them.

```python
dormancy_status(date(2020, 1, 1), [(date(2026, 6, 1), "deposit")], date(2026, 11, 25))
# -> "active"

dormancy_status(date(2020, 1, 1), [(date(2025, 6, 1), "deposit"), (date(2026, 10, 1), "interest")], date(2026, 11, 25))
# -> "dormant"

dormancy_status(date(2020, 1, 1), [], date(2026, 11, 25))
# -> "escheat_review"
```
