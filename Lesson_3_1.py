def div(divisible, divider):
    try:
        private = divisible / divider
    except ZeroDivisionError:
        return print("На нуль делить и использовать буквы нельзя))")
    return round(private, 3)


print(div(float(input('Введите делимое число: ')), float(input('Введите делитель:'))))


'''def div(divisible=float(input('Введите делимое число: ')), divider=float(input('Введите делитель:'))):
    try:
        private = divisible / divider
    except (ZeroDivisionError, ValueError):
        return print("На нуль делить и использовать буквы нельзя))")
    return round(private, 3)


print(div())'''
