"""RS-06 Mask a card number: check_ tests."""
CASES = [
    {'name': 'check_1', 'args': '"5500-0000-0000-0004"', 'expect': '"5500-00**-****-0004"'},
    {'name': 'check_2', 'args': '"4222222222222"', 'expect': '"422222***2222"'},
    {'name': 'check_3', 'args': '"411111111111"', 'expect': 'RAISES:ValueError'},
    {'name': 'check_4', 'args': '"  4111111111111111 "', 'expect': '"411111******1111"'},
]
