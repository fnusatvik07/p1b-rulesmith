# RS-07 · Validate an IBAN

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def validate_iban(iban: str) -> bool:
```

## Rules

Check an international bank account number (IBAN) before an outbound wire.

1. Remove spaces and convert to upper case. No other separators are allowed (a hyphen makes it invalid).
2. After that, only `A-Z` and `0-9` are allowed.
3. The first two letters are the country code. Only these countries are supported, with these exact lengths:
   `GB 22, DE 22, FR 27, ES 24, IT 27, NL 18, IE 22, CH 21, AE 23, SA 24`.
   Any other country is invalid.
4. Characters 3 and 4 must be digits (the check digits).
5. Move the first 4 characters to the end. Replace each letter with two digits (`A=10`, `B=11`, ... `Z=35`). Read the result as one integer. The IBAN is valid only if that integer mod 97 equals 1.
6. Never raise. Return `False` for anything invalid, including input that is not a string.

## Examples

These are the visible tests. Your agent may see and use them.

```python
validate_iban("GB82 WEST 1234 5698 7654 32")
# -> True

validate_iban("GB82 WEST 1234 5698 7654 33")
# -> False

validate_iban("DE89 3704 0044 0532 0130 00")
# -> True
```
