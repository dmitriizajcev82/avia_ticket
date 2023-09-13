def print_menu():
    """
    Вывод на экран меню
    """
    print(
        """
    Главное меню:
    
    1 - ввод рейса
    2 - вывод всех рейсов
    3 - поиск рейса по номеру
    4 - завершение работы
    """
    )


def getInput():
    """
    Проверка введенных данных
    пользователем из основного пункта меню
    """
    menu_item = input("Введите номер пункта меню: ")
    while not menu_item.isdigit() or int(menu_item) < 1 or int(menu_item) > 4:
        print("Уважаемый пользователь введите число от 1 до 4!")
        print_menu()
        menu_item = input("Введите номер пункта меню: ")
    return int(menu_item)


def getFlightdata():
    """
    проверка введенных данных номмера рейса
    """
    data = input("XXXX - номер рейса:")
    while not len(data) == 4:
        print("Номер рейса состоит из 4 символов")
        data = input("XXXX - номер рейса:")
    return data


def getDeparturedate():
    """
    проверка введенных данных даты рейса
    """
    data = input("ДД/ММ/ГГГГ - дата вылета: ")
    while not len(data) == 10:
        print("Дата вылета в формате ДД/ММ/ГГГГ")
        data = input("ДД/ММ/ГГГГ - дфта вылета: ")
    return data


def getDeparturetime():
    """
        проверка введенных данных время вылета
        """
    data = input("Время вылета в формате ЧЧ:ММ: ")
    while not len(data) == 5:
        print("Время вылета в формате ЧЧ:ММ. Проверьте данные!")
        data = input("Время вылета в формате ЧЧ:ММ: ")
    return data


def getArrivaltime():
    """
        проверка введенных данных время перелета
        """
    data = input("Время перелёта в формате ЧЧ.ММ: ")
    while float(data) < 0 and type(data) == float:
        print("Время перелёта в формате ЧЧ.ММ. Проверьте данные!")
        data = input("Время перелёта в формате ЧЧ.ММ: ")
    return data

def getDepartureairport():
    """
    проверка введенных данных Код ИАТА аэропорта вылета в формате XXX.
    """
    data = input("Код ИАТА аэропорта вылета в формате XXX.")
    while not len(data) == 3:
        print("Код ИАТА аэропорта вылета состоит из 3 символов")
        data = input("Код ИАТА аэропорта вылета в формате XXX.")
    return data

def getArrivalairport():
    """
    проверка введенных данных Код ИАТА аэропорта прилета в формате XXX.
    """
    data = input("Код ИАТА аэропорта прилета в формате XXX.")
    while not len(data) == 3:
        print("Код ИАТА аэропорта прилета состоит из 3 символов")
        data = input("Код ИАТА аэропорта прилета в формате XXX.")
    return data

def getTicketprice():
    """
        проверка введенных данных Стоимость авиабилета
    """
    data = input("Стоимость авиабилета: ")
    while not data.isdigit() or float(data) < 0:
        print("Стоимость авиабилета. Проверьте данные!")
        data = input("Стоимость авиабилета: ")
    return data
