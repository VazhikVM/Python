from sys import argv

name, production, rate, bonus = argv

print(argv)
print(production)
print(rate)
print(bonus)
try:
    print(
        f"Сотрудник отработал {float(production)} часов, со ставкой {float(rate)} рублей, премия {float(bonus)} рублей."
        f" Итого: {round(float(production) * float(rate) + float(bonus))} рублей заработная плата")
except ValueError:
    print("Вы ввели неподходящие значения попробуйте снова")
