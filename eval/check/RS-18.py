"""RS-18 Format money for customer screens: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': 'Decimal("-0.004"), "USD"', 'expect': '"0.00 USD"'},
    {'name': 'check_2', 'args': 'Decimal("1.2345"), "bhd"', 'expect': '"1.235 BHD"'},
    {'name': 'check_3', 'args': 'Decimal("999.999"), "EUR"', 'expect': '"1,000.00 EUR"'},
    {'name': 'check_4', 'args': 'Decimal("10"), "XYZ"', 'expect': 'RAISES:ValueError'},
]
