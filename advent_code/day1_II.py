# https://adventofcode.com/2023/day/1

import re

input = []

test = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

numbers_map = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

def calibration_codes(codes):
    res = 0

    for code in codes:
        first_digit, last_digit = None, None

        for i, char in enumerate(code):
            if char.isdigit():
                if not first_digit:
                    first_digit = int(char)
                last_digit = int(char)

            else:
                if i < len(code) - 2 and code[i:i+3] in numbers_map:
                    if not first_digit:
                        first_digit = numbers_map[code[i:i+3]]
                    last_digit = numbers_map[code[i:i+3]]
                    continue
                
                if i < len(code) - 3 and code[i:i+4] in numbers_map:
                    if not first_digit:
                        first_digit = numbers_map[code[i:i+4]]
                    last_digit = numbers_map[code[i:i+4]]
                    continue
                
                if i < len(code) - 4 and code[i:i+5] in numbers_map:
                    if not first_digit:
                        first_digit = numbers_map[code[i:i+5]]
                    last_digit = numbers_map[code[i:i+5]]
                    continue
                

        calibrated = int(f"{first_digit}{last_digit}")
        # print(calibrated)
        res += calibrated

    return res


print(calibration_codes(input))

