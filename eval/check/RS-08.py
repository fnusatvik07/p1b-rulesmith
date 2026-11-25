"""RS-08 Tiered savings interest: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("60000"), [(None, "3.00"), (Decimal("10000"), "1.00"), (Decimal("50000"), "2.00")]', 'expect': 'Decimal("1200.00")'},
    {'name': 'check_2', 'args': 'Decimal("10000"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")]', 'expect': 'Decimal("100.00")'},
    {'name': 'check_3', 'args': 'Decimal("10000.50"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")]', 'expect': 'Decimal("100.01")'},
    {'name': 'check_4', 'args': 'Decimal("-5"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")]', 'expect': 'Decimal("0.00")'},
]
