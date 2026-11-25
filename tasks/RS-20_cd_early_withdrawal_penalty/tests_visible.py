"""RS-20 CD early withdrawal penalty: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'Decimal("10000"), "4.00", 12, 3', 'expect': 'Decimal("197.26")'},
    {'name': 'visible_2', 'args': 'Decimal("10000"), "4.00", 6, 2', 'expect': 'Decimal("98.63")'},
    {'name': 'visible_3', 'args': 'Decimal("10000"), "4.00", 12, 12', 'expect': 'Decimal("0.00")'},
]
