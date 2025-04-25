# Задача 1 - T
def is_weekend(day):
    return day in {6, 7}


# Задача 2 - T
def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.10, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    else:
        return 0.0


# Задача 3
def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    length = len(str(abs(n)))
    sizes = {1: "однозначное", 2: "двузначное", 3: "трехзначное"}
    return f"{parity} {sizes.get(length, '')} число"


# Задача 4 - T
def convert_to_meters(unit, length):
    converters = {
        1: lambda x: x * 0.1,
        2: lambda x: x * 1000,
        3: lambda x: x,
        4: lambda x: x * 0.001,
        5: lambda x: x * 0.01
    }
    return converters.get(unit, lambda x: x)(length)


# Задача 5 - T
def describe_age(age):
    units = {
        1: "год",
        2: "года",
        3: "года",
        4: "года",
    }
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }
    ones = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    if age == 100:
        return "сто лет"
    ten, one = divmod(age, 10)
    if one == 0:
        return f"{tens[ten]} лет"
    else:
        word = units.get(one, "лет")
        return f"{tens[ten]} {ones[one]} {word}"
