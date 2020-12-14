number = int(input("Введите время в секундах: "))
hour = int(number/3600)
minutes = int(number/60 - hour * 60)
second =  int(number - (minutes * 60+hour*3600))
print(f'{hour}:{minutes}:{second}')# с доп переменными
print(f'{int(number/3600)}:{int(number/60 - int(number/3600) * 60)}:{int(number - (int(number/60 - int(number/3600) * 60) * 60+int(number/3600)*3600))}')# без доп переменными