"""RS-16 Allocate a card payment across balances: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("1000"), Decimal("100"), [{"name": "purchase", "apr": Decimal("20"), "balance": Decimal("1000")}, {"name": "cash", "apr": Decimal("25"), "balance": Decimal("500")}, {"name": "promo", "apr": Decimal("0"), "balance": Decimal("2000")}]', 'expect': '{"purchase": Decimal("400.00"), "cash": Decimal("500.00"), "promo": Decimal("100.00"), "overpayment": Decimal("0.00")}'},
    {'name': 'check_2', 'args': 'Decimal("300"), Decimal("100"), [{"name": "a", "apr": Decimal("20"), "balance": Decimal("50")}, {"name": "b", "apr": Decimal("20"), "balance": Decimal("500")}]', 'expect': '{"a": Decimal("50.00"), "b": Decimal("250.00"), "overpayment": Decimal("0.00")}'},
    {'name': 'check_3', 'args': 'Decimal("0"), Decimal("35"), [{"name": "purchase", "apr": Decimal("20"), "balance": Decimal("1000")}, {"name": "cash", "apr": Decimal("25"), "balance": Decimal("500")}, {"name": "promo", "apr": Decimal("0"), "balance": Decimal("2000")}]', 'expect': '{"purchase": Decimal("0.00"), "cash": Decimal("0.00"), "promo": Decimal("0.00"), "overpayment": Decimal("0.00")}'},
]
