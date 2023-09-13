from picture import print_picture
from progress import print_progress_bar
from function_file import (print_menu, getInput,
                           getFlightdata, getDeparturedate,
                           getDeparturetime, getArrivaltime,
                           getDepartureairport, getArrivalairport,
                           getTicketprice)
fly_date = dict() # данные о всех рейсах

while True:
    print_picture()
    print_menu()
    item_user = getInput()

    if item_user == 4:
       print_progress_bar()
       print("Выход из программы!")
       break

    elif item_user == 2:
        if len(fly_date) != 0:
            print("Информация о всех рейсах.")
            for i, j in fly_date.items():
                print(i, ' '.join(j))

        else:
            print("Данные о рейсах нет")
            print_progress_bar()

    elif item_user == 3:
        if len(fly_date) != 0:
            flight_number = input('Введите номер рейса...').upper()
            if flight_number in fly_date.keys():
                print_progress_bar()
                print(flight_number, " ".join(fly_date[flight_number]))

        else:
            print("Данных о рейсах нет!")
            print_progress_bar()

    elif item_user == 1:
       print_progress_bar()
       print("Введите данные рейса.")
       question = input("Желаете вести данные?(Нажмите 1 для продолжения ввода: )")
       if question == '1':
           while question == '1':
               trip = dict() # буфер словарь
               date_trip = [] # буфер списки
               flight_number = getFlightdata().upper()

               flight_time = getDeparturedate()

               date_trip.append(flight_time)

               departure_time = getDeparturetime()
               date_trip.append(departure_time)

               arrival_time = getArrivaltime()
               date_trip.append(arrival_time)

               departure_airport = getDepartureairport().upper()
               date_trip.append(departure_airport)

               arrival_airport = getArrivalairport().upper()
               date_trip.append(arrival_airport)

               ticket_price = getTicketprice()
               date_trip.append(ticket_price)

               trip[flight_number] = date_trip

               for i, j in trip.items():
                   print(f"Информация о рейсе {i} {j[0]} {j[1]} {j[2]} {j[3]} {j[4]} {j[5]} добавлена")
               fly_date = fly_date | trip
               question = input("Желаете вести данные? (Для продолжения нажмите 1:) ")

else:
    print("Выход из ввода данных рейса")
    print_picture()
    print_menu()



