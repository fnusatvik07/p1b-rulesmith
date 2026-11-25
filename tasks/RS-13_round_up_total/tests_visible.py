"""RS-13 Round-up savings: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': '[(date(2026, 11, 2), Decimal("-3.25")), (date(2026, 11, 3), Decimal("-4.00")), (date(2026, 11, 4), Decimal("-0.01"))], 2026, 11', 'expect': 'Decimal("1.74")'},
    {'name': 'visible_2', 'args': '[(date(2026, 11, 2), Decimal("20.00"))], 2026, 11', 'expect': 'Decimal("0.00")'},
    {'name': 'visible_3', 'args': '[], 2026, 11', 'expect': 'Decimal("0.00")'},
]
