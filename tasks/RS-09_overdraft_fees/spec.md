# RS-09 · Overdraft fees

```python
from decimal import Decimal
from datetime import date, datetime, timezone

def overdraft_fees(opening_balance: Decimal, transactions: list) -> Decimal:
```

## Rules

Work out the total overdraft fees for a run of transactions.

1. `transactions` is a list of dicts `{"date": date, "amount": Decimal}`, already in posting order. Negative amounts are debits, positive are credits. Apply them in the order given.
2. After each **debit**, if the running balance is **below -$5.00**, that debit gets a $35.00 overdraft fee. A balance of exactly -$5.00 does not.
3. Debits smaller than $5.00 (absolute value) never get a fee. Credits never get a fee.
4. At most **3 fees per calendar day**.
5. Fees are posted at the **end of each day**: they do not change the balance used for that day's checks, but they are subtracted from the balance before the next day starts.
6. Return the total fees as a `Decimal` with two decimal places.

## Examples

These are the visible tests. Your agent may see and use them.

```python
overdraft_fees(Decimal("100.00"), [{"date": date(2026, 11, 25), "amount": Decimal("-50.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-60.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-2.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-10.00")}])
# -> Decimal("70.00")

overdraft_fees(Decimal("100.00"), [{"date": date(2026, 11, 25), "amount": Decimal("40.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-20.00")}])
# -> Decimal("0.00")

overdraft_fees(Decimal("0.00"), [{"date": date(2026, 11, 25), "amount": Decimal("-5.00")}])
# -> Decimal("0.00")
```
