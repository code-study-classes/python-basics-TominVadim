# Задача 1 - L
calculate_distance = lambda x1, x2: abs(x1 - x2)

# Задача 2 - L
calculate_segments = lambda length_a, length_b: length_a // length_b

# Задача 3 - L
calculate_digit_sum = lambda number: sum(int(d) for d in str(abs(number)))


# Задача 4
def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return width * height


# Задача 5
def round_to_multiple(number, multiple):
    if multiple == 0:
        return 0
    rounded = round(number / multiple) * multiple
    return int(rounded) if isinstance(multiple, int) and isinstance(number, int) else rounded
