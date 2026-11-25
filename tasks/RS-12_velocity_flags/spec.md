# RS-12 · Card velocity rules

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def velocity_flags(txns: list) -> list:
```

## Rules

Two fraud velocity rules for card transactions. Return the sorted list of rule IDs that fire (for example `[]`, `["V1"]` or `["V1", "V2"]`).

Each transaction is a dict `{"ts": datetime (UTC, timezone-aware), "amount": Decimal, "channel": "cnp" or "cp", "country": "US"}`. The list is **not** sorted.

- **V1**: three or more card-not-present (`"cnp"`) transactions inside any 10-minute window (the first and last are at most 10 minutes apart, inclusive) whose amounts add up to **more than** $1,000.00.
- **V2**: two card-present (`"cp"`) transactions in **different countries** at most 60 minutes apart (inclusive). Country codes are compared case-insensitively.

Card-not-present transactions never count for V2, and card-present ones never count for V1.

## Examples

These are the visible tests. Your agent may see and use them.

```python
velocity_flags([{"ts": datetime(2026, 11, 25, 10, 0, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 4, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 9, tzinfo=timezone.utc), "amount": Decimal("300"), "channel": "cnp", "country": "US"}])
# -> ["V1"]

velocity_flags([{"ts": datetime(2026, 11, 25, 10, 0, tzinfo=timezone.utc), "amount": Decimal("50"), "channel": "cp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 45, tzinfo=timezone.utc), "amount": Decimal("60"), "channel": "cp", "country": "MX"}])
# -> ["V2"]

velocity_flags([{"ts": datetime(2026, 11, 25, 10, 0, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 5, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}])
# -> []
```
