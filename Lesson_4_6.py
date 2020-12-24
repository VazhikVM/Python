from itertools import count, cycle

for i in count(3):
    if i == 11:
        break
    print(i)
a = 0
for i in cycle('Hello'):
    if a == 10:
        break
    a += 1
    print(i)
