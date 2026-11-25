"""RS-11 Wire value date and cutoff: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'datetime(2026, 11, 25, 21, 30, tzinfo=timezone.utc), {date(2026, 11, 26)}', 'expect': 'date(2026, 11, 25)'},
    {'name': 'visible_2', 'args': 'datetime(2026, 11, 25, 22, 0, tzinfo=timezone.utc), {date(2026, 11, 26)}', 'expect': 'date(2026, 11, 27)'},
    {'name': 'visible_3', 'args': 'datetime(2026, 11, 28, 15, 0, tzinfo=timezone.utc), set()', 'expect': 'date(2026, 11, 30)'},
]
