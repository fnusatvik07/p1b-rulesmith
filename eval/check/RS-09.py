"""RS-09 Overdraft fees: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("0.00"), [{"date": date(2026, 11, 25), "amount": Decimal("-10.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-10.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-10.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-10.00")}, {"date": date(2026, 11, 25), "amount": Decimal("-10.00")}]', 'expect': 'Decimal("105.00")'},
    {'name': 'check_2', 'args': 'Decimal("10.00"), [{"date": date(2026, 11, 25), "amount": Decimal("-20.00")}, {"date": date(2026, 11, 26), "amount": Decimal("40.00")}, {"date": date(2026, 11, 26), "amount": Decimal("-5.00")}]', 'expect': 'Decimal("70.00")'},
    {'name': 'check_3', 'args': 'Decimal("0.00"), [{"date": date(2026, 11, 25), "amount": Decimal("-4.99")}, {"date": date(2026, 11, 25), "amount": Decimal("-4.99")}]', 'expect': 'Decimal("0.00")'},
]
