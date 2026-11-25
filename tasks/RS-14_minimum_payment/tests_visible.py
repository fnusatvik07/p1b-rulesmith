"""RS-14 Credit card minimum payment: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'Decimal("1000.00"), Decimal("10.00"), Decimal("0.00"), Decimal("0.00")', 'expect': 'Decimal("35.00")'},
    {'name': 'visible_2', 'args': 'Decimal("5000.00"), Decimal("60.00"), Decimal("40.00"), Decimal("0.00")', 'expect': 'Decimal("150.00")'},
    {'name': 'visible_3', 'args': 'Decimal("20.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")', 'expect': 'Decimal("20.00")'},
]
