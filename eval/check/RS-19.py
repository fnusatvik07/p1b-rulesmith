"""RS-19 Dormant account status: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'date(2020, 1, 1), [(date(2025, 11, 25), "login")], date(2026, 11, 25)', 'expect': '"dormant"'},
    {'name': 'check_2', 'args': 'date(2020, 1, 1), [(date(2025, 11, 26), "login")], date(2026, 11, 25)', 'expect': '"active"'},
    {'name': 'check_3', 'args': 'date(2020, 1, 1), [(date(2027, 1, 1), "deposit"), (date(2023, 1, 1), "statement")], date(2026, 11, 25)', 'expect': '"escheat_review"'},
]
