from random import randint
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list_2 = [i for i in my_list if my_list.count(i) == 1]
print(my_list_2)
# -------------------------------------------------------2--------------------------------------------------------------
my_list = [randint(0, 100) for i in range(randint(0, 500))]
my_list_2 = [i for i in my_list if my_list.count(i) == 1]
print(my_list)
print(my_list_2)
