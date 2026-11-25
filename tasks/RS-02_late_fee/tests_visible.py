"""RS-02 Late payment fee: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'Decimal("35.00"), Decimal("0.00"), 5, False', 'expect': 'Decimal("30.00")'},
    {'name': 'visible_2', 'args': 'Decimal("50.00"), Decimal("0.00"), 5, True', 'expect': 'Decimal("41.00")'},
    {'name': 'visible_3', 'args': 'Decimal("35.00"), Decimal("35.00"), 5, False', 'expect': 'Decimal("0.00")'},
]
