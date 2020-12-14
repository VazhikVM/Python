revenue = int(input("Введите сумму выручки в рублях: "))
cost = int(input("Введите сумму издержек в рублях: "))

if revenue >= cost:
    print(f"Фирма отработала с прибылью {revenue - cost} рублей.")
    print(f"Рентабельность выручки {(revenue - cost) / revenue:.2f}")
else:
    print(f"Фирма понесла убытки в размере {revenue - cost} рублей.")

worker = int(input("Введите число сотрудников в компании : "))
print(f"Прибыль на одного сотрудника равна {(revenue - cost)/worker:.2f} рублей")