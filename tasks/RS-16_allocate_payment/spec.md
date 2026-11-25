# RS-16 · Allocate a card payment across balances

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def allocate_payment(payment: Decimal, min_payment: Decimal, balances: list) -> dict:
```

## Rules

A card can carry several balances at different rates (purchases, cash advances, a promotional balance). Split a payment across them.

1. `balances` is a list of dicts `{"name": str, "apr": Decimal, "balance": Decimal}`.
2. The part of the payment up to `min_payment` goes to the **lowest** APR balance first, then the next lowest, and so on.
3. Anything paid **above** `min_payment` goes to the **highest** APR balance first, then the next highest (this is the CARD Act rule).
4. If two balances have the same APR, the one earlier in the list goes first.
5. Never pay more into a balance than what is left on it. Whatever cannot be placed is returned as `"overpayment"`.
6. If `payment` is less than `min_payment`, all of it follows rule 2.
7. Return a dict with every balance name and `"overpayment"`, each a `Decimal` with two decimal places (use `0.00` when nothing was allocated).

## Examples

These are the visible tests. Your agent may see and use them.

```python
allocate_payment(Decimal("300"), Decimal("100"), [{"name": "purchase", "apr": Decimal("20"), "balance": Decimal("1000")}, {"name": "cash", "apr": Decimal("25"), "balance": Decimal("500")}, {"name": "promo", "apr": Decimal("0"), "balance": Decimal("2000")}])
# -> {"purchase": Decimal("0.00"), "cash": Decimal("200.00"), "promo": Decimal("100.00"), "overpayment": Decimal("0.00")}

allocate_payment(Decimal("4000"), Decimal("100"), [{"name": "purchase", "apr": Decimal("20"), "balance": Decimal("1000")}, {"name": "cash", "apr": Decimal("25"), "balance": Decimal("500")}, {"name": "promo", "apr": Decimal("0"), "balance": Decimal("2000")}])
# -> {"purchase": Decimal("1000.00"), "cash": Decimal("500.00"), "promo": Decimal("2000.00"), "overpayment": Decimal("500.00")}

allocate_payment(Decimal("50"), Decimal("100"), [{"name": "purchase", "apr": Decimal("20"), "balance": Decimal("1000")}, {"name": "cash", "apr": Decimal("25"), "balance": Decimal("500")}, {"name": "promo", "apr": Decimal("0"), "balance": Decimal("2000")}])
# -> {"purchase": Decimal("0.00"), "cash": Decimal("0.00"), "promo": Decimal("50.00"), "overpayment": Decimal("0.00")}
```
