"""RS-07 Validate an IBAN: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': '"GB82 WEST 1234 5698 7654 32"', 'expect': 'True'},
    {'name': 'visible_2', 'args': '"GB82 WEST 1234 5698 7654 33"', 'expect': 'False'},
    {'name': 'visible_3', 'args': '"DE89 3704 0044 0532 0130 00"', 'expect': 'True'},
]
