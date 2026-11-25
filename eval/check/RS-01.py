"""RS-01 Foreign transaction fee: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("12.50"), "classic", True, "CA"', 'expect': 'Decimal("3.13")'},
    {'name': 'check_2', 'args': 'Decimal("100.00"), "Voyager", False, "FR"', 'expect': 'Decimal("0.00")'},
    {'name': 'check_3', 'args': 'Decimal("100.00"), "voyager", True, "FR"', 'expect': 'Decimal("4.00")'},
    {'name': 'check_4', 'args': 'Decimal("-40.00"), "classic", False, "GB"', 'expect': 'Decimal("0.00")'},
    {'name': 'check_5', 'args': 'Decimal("55.00"), "classic", False, "us"', 'expect': 'Decimal("0.00")'},
]
