"""RS-03 Add business days: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'date(2026, 12, 23), 3, {date(2026, 11, 26), date(2026, 12, 25), date(2027, 1, 1)}', 'expect': 'date(2026, 12, 29)'},
    {'name': 'check_2', 'args': 'date(2026, 12, 31), 1, {date(2026, 11, 26), date(2026, 12, 25), date(2027, 1, 1)}', 'expect': 'date(2027, 1, 4)'},
    {'name': 'check_3', 'args': 'date(2026, 11, 28), 1, set()', 'expect': 'date(2026, 11, 30)'},
    {'name': 'check_4', 'args': 'date(2026, 11, 25), -1, set()', 'expect': 'RAISES:ValueError'},
]
