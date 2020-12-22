def user_card(name, surname, year_birth, city_residence, email, phone):
    print(f'{surname} {name}, Дата рождения: {year_birth}, Город проживания: {city_residence}, {email}, {phone}')


user_card(name="Иван", surname="Иванов", year_birth="05.04.1999", city_residence="Воронеж",
          email="vv_123@mail.ru", phone="+7900 000 90 90")
