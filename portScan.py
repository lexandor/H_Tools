from termcolor import colored
import socket

import colorama
colorama.init()

print("="*30)
print('[1] --- Scan target port')
print('[2] --- Scan popular port')
print('[3] --- Scan all port')
print("="*30)

#print('{0: ^10}'.format("________"))


#col_g = colored('[+] ', 'green')
col_g = '[+] '
col_r = colored('[!] ', 'red')
col_y = colored('[!] ', 'yellow')

def scanTarget():
    print('-'*30)
    host = input(col_g + "Host --> ")
    port = input(col_g + "Port --> ")
    print('-'*30)

    scan = socket.socket()

    try:
        if host == '' or port == '':
            print(colored('Error, host/port field empty !', 'red'))
        else:
            port = int(port)
            scan.connect((host, port))
    except socket.error:
        print(col_r + "Port -- ",'{0: <6}'.format(port), " -- [CLOSED]")
    else:
        print(col_y + "Port -- ",'{0: <6}'.format(port), " -- [OPEN]")

def scanList(mode):

    print('-'*30)
    host = input(col_g + "Host --> ")
    if mode == "popular":
        ports = [20, 21, 22, 23, 42, 3, 53, 67, 69, 80, 433, 8080, 1020]
    elif mode == "all":
        ports = range(1, 6001)
    else:
        print(colored('Scan Mode Error!', 'red'))
    

    for i in ports:
        try:
            if host == "":
                print(colored('Error, host field empty!', 'red'))
                break
            else: 
                scan = socket.socket()
                scan.settimeout(0.5)
                scan.connect((host, i))
        except socket.error:
            print(col_r + "Port -- ",'{0: <6}'.format(i), " -- [CLOSED]")
        else:
            print(col_y + "Port -- ",'{0: <6}'.format(i), " -- [OPEN]")


answer = input('[scan]--> ')

if answer == "1":
    scanTarget()
elif answer == "2":
    scanList(mode="popular")
elif answer == "3":
    scanList(mode="all")
else:
    print(colored('Parrams Error!!!', 'red'))

    

