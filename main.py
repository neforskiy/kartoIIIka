from getpass import getpass
import time
passw = getpass("Введите пароль: ")
if passw == "pedik":
    print("Добро пожаловать.")
    pass
else:
    print("Неверно. Попробуйте ещё раз.")
    passw2att = getpass("Введите пароль: ")
    if passw2att == "pedik":
        print("Добро пожаловать.")
    else: 
        print("Был введён неправильные пароль 2 раза. Завершение выполнения программы..")
        exit()

        