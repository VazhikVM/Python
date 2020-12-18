my_str = input('Введените несколько любых слов: ')
my_list = my_str.split()
for i, a in enumerate(my_list, 1):
    print(f"{i}. {a[0:10]}")
