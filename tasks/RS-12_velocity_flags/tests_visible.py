"""RS-12 Card velocity rules: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': '[{"ts": datetime(2026, 11, 25, 10, 0, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 4, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 9, tzinfo=timezone.utc), "amount": Decimal("300"), "channel": "cnp", "country": "US"}]', 'expect': '["V1"]'},
    {'name': 'visible_2', 'args': '[{"ts": datetime(2026, 11, 25, 10, 0, tzinfo=timezone.utc), "amount": Decimal("50"), "channel": "cp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 45, tzinfo=timezone.utc), "amount": Decimal("60"), "channel": "cp", "country": "MX"}]', 'expect': '["V2"]'},
    {'name': 'visible_3', 'args': '[{"ts": datetime(2026, 11, 25, 10, 0, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}, {"ts": datetime(2026, 11, 25, 10, 5, tzinfo=timezone.utc), "amount": Decimal("400"), "channel": "cnp", "country": "US"}]', 'expect': '[]'},
]
