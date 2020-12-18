my_list = [7, 5, 3, 3, 2]
rating = input("Enter a new component: ")
while not (rating.isdigit()):
    rating = input('You entered an invalid value. Please, enter a new component: ')
for i in my_list:
    if i == int(rating):
        my_list.insert(my_list.index(i) + my_list.count(i), rating)
        break
if my_list[0] < int(rating):
    my_list.insert(0, int(rating))
else:
    my_list.append(int(rating))
print(my_list)
