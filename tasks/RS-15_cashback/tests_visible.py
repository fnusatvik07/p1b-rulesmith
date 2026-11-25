"""RS-15 Card cashback rewards: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': '[(date(2026, 11, 1), "dining", Decimal("100.00")), (date(2026, 11, 2), "grocery", Decimal("50.00")), (date(2026, 11, 3), "fuel", Decimal("20.00"))]', 'expect': 'Decimal("4.20")'},
    {'name': 'visible_2', 'args': '[(date(2026, 11, 1), "dining", Decimal("2000.00"))]', 'expect': 'Decimal("50.00")'},
    {'name': 'visible_3', 'args': '[]', 'expect': 'Decimal("0.00")'},
]
