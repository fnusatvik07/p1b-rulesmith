"""RS-05 Investigation deadline (Reg E): visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'date(2026, 11, 25), date(2020, 1, 1), False, False', 'expect': 'date(2027, 1, 9)'},
    {'name': 'visible_2', 'args': 'date(2026, 11, 25), date(2020, 1, 1), True, False', 'expect': 'date(2027, 2, 23)'},
    {'name': 'visible_3', 'args': 'date(2026, 11, 25), None, False, True', 'expect': 'date(2027, 2, 23)'},
]
