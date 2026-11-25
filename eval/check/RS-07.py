"""RS-07 Validate an IBAN: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': '"gb82west12345698765432"', 'expect': 'True'},
    {'name': 'check_2', 'args': '"FR14 2004 1010 0505 0001 3M02 606"', 'expect': 'True'},
    {'name': 'check_3', 'args': '"US64 SVBK US6S 3300 9673 8637"', 'expect': 'False'},
    {'name': 'check_4', 'args': '"GB82-WEST-1234-5698-7654-32"', 'expect': 'False'},
]
