import os
import json
import socket
import sys
IP_HOST = '39.101.117.243'
CONNECT_SETTIMEOUT = float(1.5)
PORTS_LIST= [21, 22, 23, 25, 53, 80,135, 139, 443, 445, 1433, 3306, 3389, 8080, 8443, 27017]
PORTS_LIST_HONYPOT = list(range(20))


def func_valid_ip(*,IP=IP_HOST):
    if len(IP) <= 15 and len(IP) >= 7 and '.' in IP:
        print('IP valid')
        print('_'*32)
    else:
         print('IP invalid')
         print('_'*32)
         sys.exit(1)
func_valid_ip()

def func_check_ip_honypot(*,ip,LIST,SETTIMEOUT):
    honypot_bool = False
    for port in LIST:  
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(SETTIMEOUT)
        result_data = s.connect_ex((ip,port))
        s.close()
        if result_data == 0:
              honypot_bool = True
              break
        else:
              honypot_bool = False
    if honypot_bool == True:
        print('='*20)
        print(f'ip {ip} is honypot!')
        print('='*20)
    else:
        print('='*20)
        print(f'ip {ip} not is honypot!')
        print('='*20)
    return honypot_bool

hon=func_check_ip_honypot(ip=IP_HOST,LIST=PORTS_LIST_HONYPOT,SETTIMEOUT=CONNECT_SETTIMEOUT)






def func_scan_ip(*,ip,LIST,SETTIMEOUT):
            open_ports = []
            for i in LIST:

                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.settimeout(SETTIMEOUT)


                result_data = s.connect_ex((ip,i))
                s.close()

                if result_data == 0:
                    print(f'port {i} open')
                    open_ports.append(i)
                elif result_data == 110:
                    print("Connection timed out",i)
                elif result_data == 111:
                    print('Connection refused',i)
                elif result_data == 113:
                    print("No route to host",i)
                else:
                    print(f'port {i} close')


            return open_ports

scan=func_scan_ip(ip=IP_HOST,LIST=PORTS_LIST,SETTIMEOUT=CONNECT_SETTIMEOUT)

DATA_IP = {
    'ip':IP_HOST,
    'HONYPOT?':hon,
    'OPEN_TCP_PORT':scan
}

def func_dump_json(**kwargs):

    json_data = json.dumps(kwargs,indent=10, ensure_ascii=False)

    os.chdir('json_data')
    with open('LOG_SCAN-recent.json','w') as f:
        f.write(json_data)
    os.chdir('..')

func_dump_json(**DATA_IP)