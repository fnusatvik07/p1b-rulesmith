# RS-06 · Mask a card number

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def mask_pan(pan: str) -> str:
```

## Rules

Mask a card number (PAN) before it is written to a log.

1. Strip leading and trailing whitespace first.
2. The PAN may contain digits, spaces and hyphens. Any other character: raise `ValueError`.
3. Count the digits only. There must be between 13 and 19 digits (inclusive), otherwise raise `ValueError`.
4. Keep the **first 6** and **last 4** digits. Replace every other digit with `*`.
5. Spaces and hyphens stay exactly where they were.
6. Do not check the Luhn digit.

## Examples

These are the visible tests. Your agent may see and use them.

```python
mask_pan("4111111111111111")
# -> "411111******1111"

mask_pan("4111 1111 1111 1111")
# -> "4111 11** **** 1111"

mask_pan("4111a11111111111")
# -> ValueError is raised
```
