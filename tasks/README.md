# Tasks

20 business rules from Harborline Bank. Each folder has:

- `spec.md`: the rule, written for an engineer, with 3 examples
- `stub.py`: the function signature
- `tests_visible.py`: the same 3 examples as test cases (your agent may use these)

`index.json` lists every task with its function name.

| ID | Rule | Function |
|:--|:--|:--|
| RS-01 | Foreign transaction fee | `foreign_transaction_fee` |
| RS-02 | Late payment fee | `late_fee` |
| RS-03 | Add business days | `add_business_days` |
| RS-04 | Provisional credit deadline (Reg E) | `provisional_credit_deadline` |
| RS-05 | Investigation deadline (Reg E) | `investigation_deadline` |
| RS-06 | Mask a card number | `mask_pan` |
| RS-07 | Validate an IBAN | `validate_iban` |
| RS-08 | Tiered savings interest | `annual_interest` |
| RS-09 | Overdraft fees | `overdraft_fees` |
| RS-10 | ATM daily limit | `atm_withdrawal_allowed` |
| RS-11 | Wire value date and cutoff | `wire_value_date` |
| RS-12 | Card velocity rules | `velocity_flags` |
| RS-13 | Round-up savings | `round_up_total` |
| RS-14 | Credit card minimum payment | `minimum_payment` |
| RS-15 | Card cashback rewards | `cashback` |
| RS-16 | Allocate a card payment across balances | `allocate_payment` |
| RS-17 | Chargeback time limits | `chargeback_window_open` |
| RS-18 | Format money for customer screens | `format_amount` |
| RS-19 | Dormant account status | `dormancy_status` |
| RS-20 | CD early withdrawal penalty | `cd_early_withdrawal_penalty` |
