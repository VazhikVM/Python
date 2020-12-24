"""def fact(n):
    for a in range(1, n + 1):
        yield a


b = 1

for i in fact(5):
    b = i * b
print(b)"""
# --------------------------------------------------------------2------------------------------------------------------


def fact(n):
    f = 1
    for a in range(1, n + 1):
        f = f * a
    yield f


for i in fact(4):
    print(i)
