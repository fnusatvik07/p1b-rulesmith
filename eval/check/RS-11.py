"""RS-11 Wire value date and cutoff: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'datetime(2026, 7, 15, 20, 30, tzinfo=timezone.utc), set()', 'expect': 'date(2026, 7, 15)'},
    {'name': 'check_2', 'args': 'datetime(2026, 7, 15, 21, 30, tzinfo=timezone.utc), set()', 'expect': 'date(2026, 7, 16)'},
    {'name': 'check_3', 'args': 'datetime(2026, 11, 28, 1, 0, tzinfo=timezone.utc), set()', 'expect': 'date(2026, 11, 30)'},
]
