# Задача 1
def find_common_elements(set1, set2):
    return {x for x in set1 if x in set2}


# Задача 2
def is_superset(set_a, set_b):
    return all(x in set_a for x in set_b)


# Задача 3
def remove_duplicates(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]


# Задача 4
def count_unique_words(text):
    return len({word.lower() for word in text.split()})


# Задача 5
def find_shared_items(*sets):
    if not sets:
        return set()
    return set.intersection(*sets)
