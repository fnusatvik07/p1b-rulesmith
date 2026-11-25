"""RS-08 Tiered savings interest: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'Decimal("5000"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")]', 'expect': 'Decimal("50.00")'},
    {'name': 'visible_2', 'args': 'Decimal("60000"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")]', 'expect': 'Decimal("1200.00")'},
    {'name': 'visible_3', 'args': 'Decimal("0"), [(Decimal("10000"), "1.00"), (Decimal("50000"), "2.00"), (None, "3.00")]', 'expect': 'Decimal("0.00")'},
]
