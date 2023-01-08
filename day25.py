#! /usr/bin/env python

conversion = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}


def convert_to_integer(snafu_number):
    int_number = 0
    for digit in snafu_number:  # E.g. '1=-0-2'
        int_number = int_number * 5 + conversion[digit]
    return int_number


def to_snafu(int_number):
    snafu_digit = {v % 5: k for k, v in conversion.items()}
    snafu_number = ''
    while int_number != 0:
        remainder = int_number % 5
        digit = snafu_digit[remainder]
        snafu_number = digit + snafu_number
        value = conversion[digit]
        int_number = (int_number - value) // 5

    return snafu_number


if __name__ == '__main__':
    with open('day25_input.txt') as f:
        lines = f.read().splitlines()

    int_sum = 0
    for line in lines:
        int_number = convert_to_integer(line)
        int_sum += int_number
    snafu_sum = to_snafu(int_sum)
    
    print('Bob\'s SNAFU number: %s' % snafu_sum)
