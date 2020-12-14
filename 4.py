a = int(input("Введите любое число: "))
b = a % 10
max = a % 10
while True:
    if a // 10 == 0:
        break
    else:
        a = a // 10
        b = a % 10
    if b > max:
        max = b
print(max)