"""RS-17 Chargeback time limits: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': '"not_received", date(2026, 1, 1), date(2026, 8, 1), date(2026, 6, 1)', 'expect': 'True'},
    {'name': 'check_2', 'args': '"not_received", date(2026, 1, 1), date(2026, 8, 1), None', 'expect': 'False'},
    {'name': 'check_3', 'args': '"duplicate", date(2026, 3, 10), date(2026, 3, 1)', 'expect': 'False'},
]
