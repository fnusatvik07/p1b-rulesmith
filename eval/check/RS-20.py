"""RS-20 CD early withdrawal penalty: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("10000"), "4.00", 36, 1', 'expect': 'Decimal("197.26")'},
    {'name': 'check_2', 'args': 'Decimal("10000"), "4.00", 60, 59', 'expect': 'Decimal("400.00")'},
    {'name': 'check_3', 'args': 'Decimal("2500"), "5.25", 11, 0', 'expect': "Decimal('32.36')"},
]
