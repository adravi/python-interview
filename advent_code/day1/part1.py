# https://adventofcode.com/2023/day/1

input = []

def calibration_values(values):
    res = 0
    first_digit, last_digit = '', ''

    for val in values:
        num_found = False

        for char in val:
            if char.isdigit() and not num_found:
                first_digit = char
                last_digit = char
                num_found = True

            elif char.isdigit() and num_found:
                last_digit = char

        calibrated = int(first_digit + last_digit)
        res += calibrated

    return res


test = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
]


print(calibration_values(input))