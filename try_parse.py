def try_parse_int():
    while True:
        try:
            console_input = int(input('Enter a weekand number: '))
            if 1 <= console_input <= 7:
                return int(console_input)
        except ValueError:
            print('is not a valid number')

number = try_parse_int()

print(number)