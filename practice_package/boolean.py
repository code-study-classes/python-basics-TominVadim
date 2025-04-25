def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


def check_odd_three(n):
    return (100 <= abs(n) <= 999) and (n % 2 != 0)


def check_unique_digits(n):
    return (100 <= abs(n) <= 999) and (len(set(str(abs(n)))) == 3)


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


def check_ascending_digits(n):
    return (100 <= abs(n) <= 999) and (sorted(str(abs(n))) == list(str(abs(n)))) and (len(set(str(abs(n)))) == 3)  # noqa: E501
