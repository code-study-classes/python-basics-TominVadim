# Задача 1 - L
extract_file_name = lambda full_file_name: full_file_name.rsplit('/', 1)[-1].split('.')[0]


# Задача 2
def encrypt_sentence(sentence):
    even_chars = sentence[1::2]
    odd_chars = sentence[0::2][::-1]
    return even_chars + odd_chars


# Задача 3
def check_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i
            stack.pop()
    return -1 if stack else 0


# Задача 4
def reverse_domain(domain):
    return '.'.join(reversed(domain.split('.'))) if '.' in domain else domain


# Задача 5
def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_vowel_group = False
    
    for char in word.lower():
        if char in vowels:
            if not in_vowel_group:
                count += 1
                in_vowel_group = True
        else:
            in_vowel_group = False
    return count
