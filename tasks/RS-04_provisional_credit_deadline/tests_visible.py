"""RS-04 Provisional credit deadline (Reg E): visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'date(2026, 11, 25), date(2020, 1, 1), {date(2026, 11, 26)}', 'expect': 'date(2026, 12, 10)'},
    {'name': 'visible_2', 'args': 'date(2026, 11, 25), date(2026, 11, 10), {date(2026, 11, 26)}', 'expect': 'date(2026, 12, 24)'},
    {'name': 'visible_3', 'args': 'date(2026, 11, 25), None, {date(2026, 11, 26)}', 'expect': 'date(2026, 12, 10)'},
]
