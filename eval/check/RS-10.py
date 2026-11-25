"""RS-10 ATM daily limit: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': '[(datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc), Decimal("400"))], Decimal("120"), datetime(2026, 11, 26, 3, 0, tzinfo=timezone.utc)', 'expect': 'False'},
    {'name': 'check_2', 'args': '[(datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc), Decimal("400"))], Decimal("120"), datetime(2026, 11, 26, 5, 30, tzinfo=timezone.utc)', 'expect': 'True'},
    {'name': 'check_3', 'args': '[(datetime(2026, 3, 8, 4, 30, tzinfo=timezone.utc), Decimal("400"))], Decimal("200"), datetime(2026, 3, 8, 5, 30, tzinfo=timezone.utc)', 'expect': 'True'},
]
