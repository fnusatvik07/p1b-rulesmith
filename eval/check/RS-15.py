"""RS-15 Card cashback rewards: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': '[(date(2026, 9, 30), "dining", Decimal("1000.00")), (date(2026, 10, 1), "dining", Decimal("1000.00"))]', 'expect': 'Decimal("60.00")'},
    {'name': 'check_2', 'args': '[(date(2026, 11, 1), "grocery", Decimal("50.00")), (date(2026, 11, 9), "grocery", Decimal("-80.00")), (date(2026, 11, 2), "fuel", Decimal("10.00"))]', 'expect': 'Decimal("0.10")'},
    {'name': 'check_3', 'args': '[(date(2026, 11, 1), "Dining", Decimal("33.33"))]', 'expect': 'Decimal("0.99")'},
]
