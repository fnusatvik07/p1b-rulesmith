"""RS-10 ATM daily limit: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': '[], Decimal("500"), datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc)', 'expect': 'True'},
    {'name': 'visible_2', 'args': '[], Decimal("520"), datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc)', 'expect': 'False'},
    {'name': 'visible_3', 'args': '[], Decimal("30"), datetime(2026, 11, 25, 15, 0, tzinfo=timezone.utc)', 'expect': 'False'},
]
