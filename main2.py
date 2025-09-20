from getpass import getpass
password = getpass("Ведите мой пароль: ")

def idinahig():
    print("Нет, иди нафиг")

if password == "govno":
    pass
else:
    idinahig()
    exit()


print("Чай или кофе?")
teaorcoffe = input("Позиция 1 или 2: ")
idinahig()