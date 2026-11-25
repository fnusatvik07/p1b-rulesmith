"""RS-01 Foreign transaction fee: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'Decimal("100.00"), "classic", False, "FR"', 'expect': 'Decimal("3.00")'},
    {'name': 'visible_2', 'args': 'Decimal("100.00"), "classic", False, "US"', 'expect': 'Decimal("0.00")'},
    {'name': 'visible_3', 'args': 'Decimal("200.00"), "classic", True, "MX"', 'expect': 'Decimal("5.00")'},
]
