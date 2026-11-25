"""RS-17 Chargeback time limits: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': '"fraud", date(2026, 1, 1), date(2026, 5, 1)', 'expect': 'True'},
    {'name': 'visible_2', 'args': '"fraud", date(2026, 1, 1), date(2026, 5, 2)', 'expect': 'False'},
    {'name': 'visible_3', 'args': '"chargeback", date(2026, 1, 1), date(2026, 2, 1)', 'expect': 'RAISES:ValueError'},
]
