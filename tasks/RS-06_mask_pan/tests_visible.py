"""RS-06 Mask a card number: visible_ tests."""
CASES = [
    {'name': 'visible_1', 'args': '"4111111111111111"', 'expect': '"411111******1111"'},
    {'name': 'visible_2', 'args': '"4111 1111 1111 1111"', 'expect': '"4111 11** **** 1111"'},
    {'name': 'visible_3', 'args': '"4111a11111111111"', 'expect': 'RAISES:ValueError'},
]
