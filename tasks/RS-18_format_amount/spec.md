# RS-18 · Format money for customer screens

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def format_amount(amount: Decimal, currency: str) -> str:
```

## Rules

Format an amount for display.

1. Currency codes are case-insensitive. Supported currencies and their decimal places: `USD 2, EUR 2, GBP 2, INR 2, JPY 0, KRW 0, BHD 3, KWD 3`. Any other currency: raise `ValueError`.
2. Round to that many decimal places, halves up (away from zero).
3. Use `.` as the decimal point and `,` to group digits. Groups are of three (`1,234,567.89`) **except INR**, which uses Indian grouping: the last three digits, then groups of two (`12,34,567.89`).
4. The result is the number, a space, and the upper-case code: `"1,234.50 USD"`. Currencies with 0 decimals have no decimal point: `"1,235 JPY"`.
5. Negative amounts start with `-`: `"-12.00 USD"`. If the amount rounds to zero, there is no minus sign: `"0.00 USD"`.

## Examples

These are the visible tests. Your agent may see and use them.

```python
format_amount(Decimal("1234.5"), "USD")
# -> "1,234.50 USD"

format_amount(Decimal("1234.5"), "JPY")
# -> "1,235 JPY"

format_amount(Decimal("1234567.891"), "INR")
# -> "12,34,567.89 INR"
```
