def my_func(a, b, c):
    my_list = [a, b, c]
    m_1 = max(my_list)
    my_list.remove(m_1)
    m_2 = max(my_list)
    return f'Сумма 2-х наибольших значений {m_1} и {m_2} равнов {m_1 + m_2}'


print(my_func(6, 8, 3))
print(my_func(88, 88, 88))
