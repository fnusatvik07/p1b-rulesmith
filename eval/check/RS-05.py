"""RS-05 Investigation deadline (Reg E): check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'date(2026, 11, 25), date(2026, 11, 1), False, False', 'expect': 'date(2027, 2, 23)'},
    {'name': 'check_2', 'args': 'date(2028, 1, 15), None, False, False', 'expect': 'date(2028, 2, 29)'},
    {'name': 'check_3', 'args': 'date(2026, 11, 25), date(2026, 10, 25), False, False', 'expect': 'date(2027, 1, 9)'},
]
