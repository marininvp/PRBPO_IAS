def data_verify():
    print("Введите данные для объекта класса: ")
    firstname = input("Введите имя пользователя: ")
    while len(firstname) == 0 or len(firstname) > 255:
        firstname = input("Введите имя пользователя, количество символов некорректно: ")
    lastname = input("Введите фамилию пользователя: ")
    while len(lastname) == 0 or len(lastname) > 255:
        lastname = input("Введите фамилию пользователя, количество символов некорректно: ")
    while True:
        try:
            age = int(input("Введите возраст пользователя как количество лет: "))
            break
        except:
            print("Возраст должен представлять собой натуральное число, меньшее чем 2147483647")
    country = input("Введите страну проживания пользователя: ")
    while len(country) == 0 or len(country) > 255:
        country = input("Введите страну проживания пользователя, количество символов некорректно: ")
    city = input("Введите город проживания пользователя: ")
    while len(city) == 0 or len(city) > 255:
        city = input("Введите город проживания пользователя, количество символов некорректно: ")
    return firstname,lastname,age,country, city