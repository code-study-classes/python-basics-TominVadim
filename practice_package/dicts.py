from collections import defaultdict


# Задача 1
def count_char_occurrences(text):
    result = defaultdict(int)
    for char in text.lower():
        if char.isalpha():
            result[char] += 1
    return dict(result)


# Задача 2
def merge_dicts(dict1, dict2, resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = resolver(key, result[key], value)
        else:
            result[key] = value
    return result


# Задача 3
def invert_dictionary(original):
    inverted = defaultdict(list)
    for key, value in original.items():
        inverted[value].append(key)
    return {k: sorted(v) for k, v in inverted.items()}


# Задача 4
def dict_to_table(data_dict, columns):
    rows = []
    for item in data_dict.values():
        row = [str(item.get(col, 'N/A')) for col in columns]
        rows.append(row)
    
    headers = [col.upper() for col in columns]
    col_widths = []
    for i in range(len(columns)):
        max_data_len = max((len(row[i]) for row in rows), default=0)
        col_widths.append(max(len(headers[i]), max_data_len))
    
    header_line = "| " + " | ".join(
        h.ljust(w) for h, w in zip(headers, col_widths)
    ) + " |"
    
    separator = "|" + "|".join(["-" * (w + 2) for w in col_widths]) + "|"
    
    data_lines = []
    for row in rows:
        data_line = "| " + " | ".join(
            cell.ljust(w) for cell, w in zip(row, col_widths)
        ) + " |"
        data_lines.append(data_line)
    
    return "\n".join([header_line, separator] + data_lines)


# Задача 5
def deep_update(base, update):
    result = base.copy()
    for key, value in update.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_update(result[key], value)
            else:
                result[key] = value
    return result