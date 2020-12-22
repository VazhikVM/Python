total = []
total_err = []
my_sum = 0
exit_while = None
while exit_while != "q":
    use_number = input('Введите числа через пробел: ').split()
    if my_sum == 0:
        try:
            my_sum = sum(list(map(int, use_number)))
            total.append(my_sum)
            print(total[-1])
        except ValueError:
            for i in use_number:
                if i.isdigit():
                    total_err.append(i)
            total_err = list(map(int, total_err))
            exit_while = input(f'{sum(total_err)}, Для выхода нажмите "q"').lower()
    else:
        try:
            my_sum = sum(list(map(int, use_number)))
            total.append(my_sum)
            print(f'{total[-1]} ({sum(total)})')
        except ValueError:
            for i in use_number:
                if i.isdigit():
                    total_err.append(i)
            total_err = list(map(int, total_err))
            exit_while = input(f'{sum(total_err)}, Для выхода нажмите "q"').lower()

print("Спасибо за игру")
