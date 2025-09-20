from getpass import getpass
import random
password = getpass("Ведите мой пароль: ")

def incorrect():
    print("Нет, иди нафиг")

def drinks():
    print("Чай или кофе?")
    drink = input("Позиция чай(1) или кофе(2) или неизвестно(10)????: ")
    if drink == "10":
        print("+ 1 героин")
        next = input("Повторить? Д/Н: ")
        if next == "Д":
            drinks()
        elif next == "д":
            drinks()
        elif next == "Y":
            drinks()
        elif next == "y":
            drinks()
        else:
            exit()
        exit()
    incorrect()

def checkPassword():
    if password == "govno":
        pass
    else:
        incorrect()
        exit()

def work():
    work = input("Задачи: рандомное число от 1 до 100(1) или быть посланым(2): ")
    str_to_num(work)
    if work == "1":
        rand = random.randint(0, 100)
        print(rand)
    elif work == "2":
        print("иди за хлебом")
    else:
        incorrect()

def str_to_num(line):
    line = line.strip()
    if line.isdigit():
        return int(line) 
    elif '.' in line or ',' in line:
        if any(line.replace(x, '').isdigit() for x in ['.', ',']):
            return float(line.replace(',', '.'))
    else:
        print('Это не число!\n')
        return None

def choose():
    drinkorwork = input("Выберети услугу: задачи(1) или напитки(2): ")
    if drinkorwork == "1":
        work()
    elif drinkorwork == "2":
        drinks()
    else:
        incorrect()


checkPassword()
choose()


