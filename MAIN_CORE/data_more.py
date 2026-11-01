import json
import socket
import os



def func_json_loads():
    os.chdir('json_data')
    with open('LOG_SCAN-recent.json','r') as f:
        data_json=f.read()
    os.chdir('..')
    data_json=json.loads(data_json)
    return data_json
    
data_json=func_json_loads()
print(data_json)

def func_recv_ports(**data):
    for port_list in data['OPEN_TCP_PORT']:
        
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.settimeout(3.0)


                result_data = s.connect_ex((data['ip'],port_list))
                

                if result_data == 0:
                    s.sendall("GET / HTTP/1.0\r\nHELP\r\n\r\n".encode('utf-8'))
                    data_baner = s.recv(1024)
                    print(f'baner-\t{data_baner}')
                    s.close()
func_recv_ports(**data_json)
