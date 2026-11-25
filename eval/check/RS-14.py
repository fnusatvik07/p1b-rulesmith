"""RS-14 Credit card minimum payment: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("1000.00"), Decimal("10.00"), Decimal("0.00"), Decimal("25.00")', 'expect': 'Decimal("60.00")'},
    {'name': 'check_2', 'args': 'Decimal("50.00"), Decimal("0.00"), Decimal("0.00"), Decimal("30.00")', 'expect': 'Decimal("50.00")'},
    {'name': 'check_3', 'args': 'Decimal("12345.67"), Decimal("100.00"), Decimal("0.00"), Decimal("0.00")', 'expect': 'Decimal("223.46")'},
]
