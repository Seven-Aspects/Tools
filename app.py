"""
    Импорт модулей
"""
import time, os # Импортируем модули для задержки, работы с ОС и запросов на сайты
from Attack.functions import * # Импортируем вспомогательные функции и классы для работы програмы

"""
    Обьявляем классы
"""
color = Color('\033') # Класс для использования цвета в командной строке
project = System() # Класс с системными значениями

"""
    Основной код програмы
"""
clear()
if check_connection(): # Проверяем наличие подключения к интернету
    animate_message("\n\n\n\nПодключение к интернету установлено\n\n", color.green)
else:
    animate_message("\n\n\n\nПодключение к серверу не установлено\n\n", color.red)
    quit()
check_update() # Проверяем наличие обновлений
set_title("Seven Aspects - Bomber") # Переименновываем окно командной строки

def bomber():
    bomber = Bomber()
    bomber.bomber()

def snoser():
    clear()
    while True:
        animate_message(f'''{color.reset}
    {color.white}[1]{color.green} Виртуальный номер{color.reset}
    {color.white}[2]{color.green} Премиум{color.reset}
    {color.white}[3]{color.green} Оскорбление{color.reset}
    {color.white}[4]{color.green} Нарушение правил{color.reset}
    {color.white}[5]{color.green} Cнос Сессий{color.reset}
    {color.white}[6]{color.green} Спам{color.reset}
    {color.white}[7]{color.green} Прайс{color.reset}
    {color.white}[8]{color.green} Накрутка{color.reset}

    {color.white}[0]{color.green} Выйти{color.reset}


{color.white} Введите опцию{color.reset}

''', speed=0.005)
        complaint_choice = input(f"{color.red}~# {color.rgb_color(161, 161, 161)}")
        print(color.white)
        if complaint_choice == '0':
            waiting()
            break
        if complaint_choice in ["1", "2", "3", "4", "6", "7", "8"]:
            username = input("Введите @username: ")
            telegram_id = input("Введите Telegram ID: ")
            repeats = int(input("Введите количество жалоб: "))
            for _ in range(repeats):
                number = generate_phone_number()
                email = generate_random_email()
                proxies_list = get_proxies_list()
                proxies = {'http': random.choice(proxies_list)}
                send_complaint(username, telegram_id, number, email, 1, complaint_choice, proxies)
            waiting()
            clear()
        elif complaint_choice == '5':
            username = input("Введите юзернейм: ")
            telegram_id = input("Введите Telegram ID: ")
            repeats = int(input("Введите количество жалоб: "))
            number = input("Введите номер телефона аккаунта: ")
            email = generate_random_email()
            proxies_list = get_proxies_list()
            proxies = {'http': random.choice(proxies_list)}
            send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies)
            waiting()
            clear()
        else:
            clear()
            print(color.color_message("Некорректная причина", color.red))

def menu():
    clear()
    try:
        while True:
            match menu_input(f'{color.red}~# {color.rgb_color(161, 161, 161)}'):
                case 'stop':
                    stop()
                case 'bomber':
                    bomber()
                case 'snoser':
                    snoser()
            
            clear()
    except KeyboardInterrupt:
        stop()
    except Exception:
        check_update(True)
        quit()

if __name__ == '__main__':
    menu()