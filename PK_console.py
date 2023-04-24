#---------------------------by-fingal-1000----------------------------------
#----------------------------02/04/2023-------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------


#----------import-----------
import random
import subprocess as sp
#---------------------------


print('########  ####  ##    ##   ######       ###     ##           ##     #####     #####     #####   ')
print('##         ##   ###   ##  ##    ##     ## ##    ##         ####    ##   ##   ##   ##   ##   ##  ')
print('##         ##   ####  ##  ##          ##   ##   ##           ##   ##     ## ##     ## ##     ## ')
print('######     ##   ## ## ##  ##   ####  ##     ##  ##           ##   ##     ## ##     ## ##     ## ')
print('##         ##   ##  ####  ##    ##   #########  ##           ##   ##     ## ##     ## ##     ## ')
print('##         ##   ##   ###  ##    ##   ##     ##  ##           ##    ##   ##   ##   ##   ##   ##  ')
print('##        ####  ##    ##   ######    ##     ##  ########    ######   #####     #####     #####  ')

print()
print()
print()
print()
print('1:matrix')
print('2:user_wifi_profiles_password')
print('3:')
print('4:morze')
print('5:')
print("99:exit")

inp = input('select (1-5)')

if inp =="1":
    while True:
       print((random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000),random.randint(0, 10000)))

if inp =="2":
    sp.call( 'netsh wlan show profile key = clear')
    wifi = input("enter wifi:")
    sp.call('netsh wlan show profile' + " " + wifi + " " + "key = clear")


if inp =="3":
    f = open('1.txt')
    read = f.readline()
    print(read)
    exit = input(1)

if inp == '4':
    morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••', ' ': '\n'}

text = input('type text:').lower()

for i in text:
    for key, value in morze.items():
        if i==key:
            print(value, end=' ')

if inp == '5':
    print(555555)

if inp == '99':
     exit()

exit=input("press enter")


