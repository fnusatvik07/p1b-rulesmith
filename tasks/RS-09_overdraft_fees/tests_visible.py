"""RS-09 Overdraft fees: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'Decimal("100.00"), [{"date": date(2026, 11, 25), "amount": Decimal("-50.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-60.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-2.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-10.00")}]', 'expect': 'Decimal("70.00")'},
    {'name': 'visible_2', 'args': 'Decimal("100.00"), [{"date": date(2026, 11, 25), "amount": Decimal("40.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-20.00")}]', 'expect': 'Decimal("0.00")'},
    {'name': 'visible_3', 'args': 'Decimal("0.00"), [{"date": date(2026, 11, 25), "amount": Decimal("-5.00")}]', 'expect': 'Decimal("0.00")'},
]
