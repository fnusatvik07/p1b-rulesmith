"""RS-18 Format money for customer screens: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': 'Decimal("1234.5"), "USD"', 'expect': '"1,234.50 USD"'},
    {'name': 'visible_2', 'args': 'Decimal("1234.5"), "JPY"', 'expect': '"1,235 JPY"'},
    {'name': 'visible_3', 'args': 'Decimal("1234567.891"), "INR"', 'expect': '"12,34,567.89 INR"'},
]
