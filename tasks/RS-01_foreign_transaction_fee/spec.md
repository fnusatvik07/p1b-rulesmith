# RS-01 · Foreign transaction fee

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def foreign_transaction_fee(amount: Decimal, card_tier: str, is_atm: bool, merchant_country: str) -> Decimal:
```

## Rules

Harborline charges a fee when a debit card is used outside the United States.

1. `amount` is the transaction amount in USD (already converted). It is a `Decimal`.
2. If `amount` is zero or negative (a refund or reversal), the fee is `0.00`.
3. If `merchant_country` is `"US"`, the fee is `0.00`. Country codes are ISO 3166 two-letter codes and must be compared case-insensitively.
4. **Purchases** (`is_atm` is False): the fee is 3% of `amount`.
5. **ATM withdrawals** (`is_atm` is True): the fee is a flat $3.00 plus 1% of `amount`.
6. Cards on the `Voyager` tier (case-insensitive) pay **no fee on purchases**. The Voyager waiver does **not** apply to ATM withdrawals.
7. Round the fee to cents, with halves rounded **up** (away from zero). Return a `Decimal` with exactly two decimal places.

## Examples

These are the visible tests. Your agent may see and use them.

```python
foreign_transaction_fee(Decimal("100.00"), "classic", False, "FR")
# -> Decimal("3.00")

foreign_transaction_fee(Decimal("100.00"), "classic", False, "US")
# -> Decimal("0.00")

foreign_transaction_fee(Decimal("200.00"), "classic", True, "MX")
# -> Decimal("5.00")
```
