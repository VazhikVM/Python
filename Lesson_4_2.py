from random import randint
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 123, 123, 55]
my_list_2 = []
a = 0
try:
    for i in my_list:
        a += 1
        if i < my_list[a]:
            my_list_2.append(my_list[a])
except IndexError:
    print(my_list)
    print(my_list_2)

# -------------------------------------------------------2--------------------------------------------------------------

my_list = [randint(0, 500) for i in range(randint(0, 50))]
print(my_list)
my_list_2 = []
a = 0
try:
    for i in my_list:
        a += 1
        if i < my_list[a]:
            my_list_2.append(my_list[a])
except IndexError:
    print(my_list_2)
