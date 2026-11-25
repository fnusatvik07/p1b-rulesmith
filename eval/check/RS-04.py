"""RS-04 Provisional credit deadline (Reg E): check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'date(2026, 11, 25), date(2026, 10, 26), {date(2026, 11, 26)}', 'expect': 'date(2026, 12, 24)'},
    {'name': 'check_2', 'args': 'date(2026, 11, 25), date(2026, 10, 25), {date(2026, 11, 26)}', 'expect': 'date(2026, 12, 10)'},
    {'name': 'check_3', 'args': 'date(2026, 11, 28), date(2019, 5, 5), set()', 'expect': 'date(2026, 12, 11)'},
]
