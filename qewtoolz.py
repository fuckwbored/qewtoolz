import requests
import pyshorteners
import pyshorteners as sh
from faker import Faker
from faker.providers import internet
from colorama import Fore, Back, Style

print(Fore.RED + """
                  *   '''`````'''
             *
          *
        *           ..i'             q.
       *         .poj;                qq.
      .         oKPO                   THk
     .k        {HHk`                    THH,
     dH,       ;YJH.                     YHHk
    {HHk       :lHHk                     jHHH
     THHk      `NJHH,                   .HHHl'
      THHk,     lHHHHk                 jHHHHP
       THHHi:,  `GHHHHH,.            .'HHHHH
        `THHHHHHiWHHHHHkoo....ooooojHHHHHHFL
          `*THHHH`THHHHHHHHHHHHHHHHHHHHHHHHl
             `*THHHYHHHHHHHHHHHHHHHHHHHHHHHI
                `*THHYHHHHHHHHHHHHHHHHHHHHHH
                  `*THHHHHHHHHHHHHHHHHHHHHH
                     `THHHHHHHHHHHHHHHHHHHP
                       `THHHHHHHHHHHHHHHHHH| 


ПОДПИСЫВАЙИЕСЬ НА НАШ ТЕЛЕГРАМ КАНАЛ - @termuxqew
ПОДПИСЫВАЙИЕСЬ НА НАШ ТЕЛЕГРАМ КАНАЛ - @termuxqew
ПОДПИСЫВАЙИЕСЬ НА НАШ ТЕЛЕГРАМ КАНАЛ - @termuxqew
""" + Style.RESET_ALL)
print("""
[1] Спрасить анонимные proxy
[2] Укоротить ссылку
[3] Информация по IP
[4] Сгенерировать фейкового человека

[99] Возникла ошибка? Нужна помощь?
""")

def proxy():
	try:
		proxytype = input("Укажите тип прокси (http|https|socks4|socks5) >>> ")
		print("[+] Сохраняю прокси, подождите...")
		limk = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=' + str(proxytype) + '&timeout=1000&country=all&anonymity=elite').text
		limk1 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=' + str(proxytype) + '&timeout=1000&country=all').text
		f1 = open('anonymous.txt', 'w+')
		f2 = open('not_anonymous.txt', 'w+')
		f1.write(limk)
		f2.write(limk1)
		f1.close()
		f2.close()
		print("[+] Прокси сохранены усешно")
		print("Прокси с элитной анонимностью - anonymous.txt\nПрокси без анонимности - not_anonymous.txt")
	except:
		print("[-] Убедитесь, что тип прокси верный!")

def cutlink():
	site = input('Укажите ссылку, какую нужно сократить \nНапример: https://qewtoolz.com/ >>> ')
	try:
		print("[+] Начинаю сокращать")
		s = sh.Shortener()
		isgd = s.isgd.short(site)
		dagd = s.dagd.short(site)
		osdb = s.osdb.short(site)
		tinyurl = s.tinyurl.short(site)
		print('[+] Сокращено успешно: ' + "\n" + tinyurl + "\n" + isgd + "\n" + dagd + "\n" + osdb)
	except:
		print("[-] Убедитесь, что ссылка нужного формата")

def ipinfo():
	ip = input('Укажите ip адрес >>> ')
	try:
		print("[+] Получаю информацию...")
		site = "https://ipinfo.io/" + ip + "/json"
		response = requests.get(site).text
		print("[+] Сканирование по " + ip + " выполнено успешно:" + "\n" + response)
	except:
		print('[-] Убедитесь что вы ввели правильный IP адрес и повторите попытку')

def fakedat():
	fake = Faker()
	print("[+] Начинаю генерировать...")
	name12 = fake.name()
	adress = fake.address()
	text = fake.text()
	ipv4 = fake.ipv4_private()
	print(name12 + "\n" + "\n" + adress +"\n" + "\n" + text + "\n" + "\n" + ipv4)

def error_99():
	print("Возникла ошибка? Нашли баг? \n\nНапишите в наш телеграм бот, четко описав вашу проблему")
	print(Back.CYAN + "-----  @Termuxqew_bot   -----" + Style.RESET_ALL)

user_input = input(">>> ")
if user_input == "1":
	proxy()
elif user_input == "2":
	cutlink()
elif user_input == "3":
	ipinfo()
elif user_input == "4":
	fakedat()
elif user_input == "99":
	error_99()
else:
	print("[-] Такого пункта нету, долбоеб!")