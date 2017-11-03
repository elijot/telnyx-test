# -*- coding: utf-8 -*-
# !/usr/bin/env python

import csv

import typecheck as tc

CSV_FILE = 'results.csv'
CSV_DELIMITER = ','
QUOTE_CHAR = '|'


@tc.typecheck
def ternary(n: int, base: int) -> str:
    if n == 0:
        return str(0)
    nums = []
    while n:
        n, reminder = divmod(n, base)
        nums.append(str(reminder))
    return ''.join(reversed(nums))


@tc.typecheck
def is_palindrome(number: str) -> bool:
    return number == number[::-1]


@tc.typecheck
def save_csv(results: list, out_file: str):
    try:
        with open(out_file, 'w') as csvfile:
            w = csv.writer(csvfile, delimiter=CSV_DELIMITER, quotechar=QUOTE_CHAR, quoting=csv.QUOTE_MINIMAL)
            for row in results:
                w.writerow(row)
    except Exception as e:
        raise IOError('Error while writing csv. {}'.format(e))


@tc.typecheck
def get_palindromes(start: int, end: int, start_base: int=2) -> list:
    results = []
    i = start
    while i <= end:
        base = start_base
        if start_base < 2:
            raise ValueError('Base needs to be >= 2')
        while True:
            n = ternary(i, base)
            if is_palindrome(n):
                results.append((i, base))
                break
            base += 1
        i += 1
    return results


if __name__ == "__main__":
    r = get_palindromes(start=1, end=1000, start_base=2)
    save_csv(r, out_file=CSV_FILE)
