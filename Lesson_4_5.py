from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)


def my_fun(a, b):
    return a * b


print(reduce(my_fun, [i for i in range(100, 1001) if i % 2 == 0]))
