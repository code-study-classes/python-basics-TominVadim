# Задача 1 - G
square_odds = lambda numbers: [x**2 for x in numbers if x % 2 != 0]

# Задача 2 - G
normalize_names = lambda names: [name.capitalize() for name in names]


# Задача 3 - G
def remove_invalid_emails(emails):
    return [email for email in emails if 
            email.count('@') == 1 and 
            len(email) >= 5 and 
            not email.startswith('@') and 
            not email.endswith('@')]


# Задача 4 - G
filter_palindromes = lambda words: [word for word in words if word.lower() == word.lower()[::-1]]


# Задача 5
def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


# Задача 6
def find_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
