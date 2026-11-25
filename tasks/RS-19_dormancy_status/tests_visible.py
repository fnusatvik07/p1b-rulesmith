"""RS-19 Dormant account status: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'date(2020, 1, 1), [(date(2026, 6, 1), "deposit")], date(2026, 11, 25)', 'expect': '"active"'},
    {'name': 'visible_2', 'args': 'date(2020, 1, 1), [(date(2025, 6, 1), "deposit"), (date(2026, 10, 1), "interest")], date(2026, 11, 25)', 'expect': '"dormant"'},
    {'name': 'visible_3', 'args': 'date(2020, 1, 1), [], date(2026, 11, 25)', 'expect': '"escheat_review"'},
]
