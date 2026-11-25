"""RS-02 Late payment fee: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("25.00"), Decimal("0.00"), 3, True', 'expect': 'Decimal("25.00")'},
    {'name': 'check_2', 'args': 'Decimal("35.00"), Decimal("34.00"), 4, False', 'expect': 'Decimal("0.00")'},
    {'name': 'check_3', 'args': 'Decimal("35.00"), Decimal("33.99"), 4, False', 'expect': 'Decimal("30.00")'},
    {'name': 'check_4', 'args': 'Decimal("35.00"), Decimal("0.00"), 0, True', 'expect': 'Decimal("0.00")'},
]
