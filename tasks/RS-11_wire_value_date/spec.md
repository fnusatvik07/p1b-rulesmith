# RS-11 · Wire value date and cutoff

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def wire_value_date(submitted_at: datetime, holidays: set) -> date:
```

## Rules

Domestic wires submitted before the cutoff go out the same day. Later ones go out the next business day.

1. `submitted_at` is a timezone-aware datetime in UTC.
2. The cutoff is **5:00 PM New York time** (`America/New_York`, with daylight saving time). A wire submitted at exactly 17:00:00 or later has missed the cutoff.
3. Work in New York local time. If the New York date is a business day (Monday to Friday and not in `holidays`) and the time is before 17:00:00, the value date is that New York date.
4. Otherwise the value date is the next business day after the New York date.
5. `holidays` is a set of New York `datetime.date` values.

## Examples

These are the visible tests. Your agent may see and use them.

```python
wire_value_date(datetime(2026, 11, 25, 21, 30, tzinfo=timezone.utc), {date(2026, 11, 26)})
# -> date(2026, 11, 25)

wire_value_date(datetime(2026, 11, 25, 22, 0, tzinfo=timezone.utc), {date(2026, 11, 26)})
# -> date(2026, 11, 27)

wire_value_date(datetime(2026, 11, 28, 15, 0, tzinfo=timezone.utc), set())
# -> date(2026, 11, 30)
```
