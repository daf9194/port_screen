import socket
import threading
import requests


port_lst = [80, 443, 20, 21, 25]        #Укажите порты, которые необходимо проверить


def is_port_open(host, port):
    '''определяет открытый порт'''
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((host, port))
    except:
        pass
    else:
        print(f'({host}:{port} OPEN)')
        if port == 80 or port == 443:
            r = requests.get(f'http://{host}').headers
        print(r['Server'])


hosts_file = open('hosts.txt', 'r')
for host in hosts_file:
    for port in port_lst:
        '''запускает многопоточность'''
        flow = threading.Thread(target=is_port_open, args=(host.strip(), port))
        flow.start()
hosts_file.close()
