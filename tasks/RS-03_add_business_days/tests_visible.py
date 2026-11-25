"""RS-03 Add business days: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'date(2026, 11, 25), 1, {date(2026, 11, 26), date(2026, 12, 25), date(2027, 1, 1)}', 'expect': 'date(2026, 11, 27)'},
    {'name': 'visible_2', 'args': 'date(2026, 11, 27), 1, set()', 'expect': 'date(2026, 11, 30)'},
    {'name': 'visible_3', 'args': 'date(2026, 11, 28), 0, set()', 'expect': 'date(2026, 11, 30)'},
]
