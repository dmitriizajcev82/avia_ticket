import random

def print_picture():
    picture_to_out = {
        1: """
        ************************************************
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣏⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣦⠄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣧⠄⠄⠙⠿⢋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠄⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⡷⠄⠄⠄⠘⠛⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⢿⣿⣿⣿⣿
            ⣿⣿⣿⣿⡿⠇⣀⣀⠄⠄⠄⠄⠄⠄⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠄⠄⠄⠰⠰⠙⠛⠁⠙⢿⣿
            ⣿⣟⣫⣵⣶⣿⣿⣿⣿⣶⣤⣄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣤⣾⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠄⠄⣤⣴⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⣁⣤⣶⣦⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⡿⠟⣋⣡⣤⣶⣾⣿⣿⣿⣿⣿⣷⣶⣤⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣛⣩⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿Сервис поиска авиабилетов
        ************************************************
           """,
        2: """
        **************************************
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣯⣉⠙⠛⠛⠿⠿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠄⠄⢀⣴⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⣠⣴⠾⠛⠋⠁⠄⠄⠄⣠⣴⣾⣿⣿⣿⣿
            ⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣄⠈⠙⠻⠿⠛⠉⠄⠄⠄⣀⣤⣤⠄⠄⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣆⠄⠄⠄⢀⣠⣴⣶⣿⣿⣿⣿⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿
            ⣿⣿⣿⣿⣿Сервис поиска авиабилетов
        **************************************
           """,
        3: """
        **************************************
            ⢀⢀⢀⣖⠲⡀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⠉⡇⢀⢀⢀⢀⢀⢀⢀
            ⢀⢀⢀⠸⡆⠹⡀⣠⢤⡄⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡏⢀⡧⢤⡄⢀⢀⢀⢀⢀
            ⢀⢀⢀⢀⡧⢄⣹⣅⣜⡀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⠁⢀⢹⠚⠃⢀⢀⢀⢀⢀
            ⢀⣀⠴⢒⣉⡹⣶⣤⣀⡉⠉⠒⠒⠒⠤⠤⣀⣀⣀⠇⢀⢀⢸⠠⣄⢀⢀⢀⢀⢀
            ⢀⠈⠉⠁⢀⢀⢀⠉⠒⠯⣟⣲⠦⣤⣀⡀⢀⢀⠈⠉⠉⠉⠛⠒⠻⢥⣀⢀⢀⢀
            ⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠈⠙⣲⡬⠭⠿⢷⣦⣤⢄⣀⢀⢀⠚⠛⠛⠓⢦⡀
            ⢀⢀⢀⢀⢀⢀⢀⢀⣀⠤⠴⠚⠉⠁⢀⢀⢀⢀⣀⣉⡽⣕⣯⡉⠉⠉⠑⢒⣒⡾
            ⢀⢀⣀⡠⠴⠒⠉⠉⢀⢀⣀⣀⠤⡤⢶⣶⣋⠉⠉⢀⢀⢀⠈⠉⠉⠉⠉⠉⠁⢀
            ⣖⣉⣁⣠⠤⠶⡶⡶⢍⡉⢀⢀⢀⠙⠒⠯⠜⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀
            ⢀⠁⢀⢀⢀⢀⠑⢦⣯⠇⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀
            ......Сервис поиска авиабилетов
        **************************************
           """
    }

    picture_print = random.choice(list(picture_to_out.values()))

    print("   ",picture_print)