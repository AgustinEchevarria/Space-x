# SERVER LOCAL 
import json
import socket
import requests
from random import randint

api_token = 'b3a9f284e77aa2ac135c755fa6dab100' #Your api key
client_token = 'eab6bad1a899972bd2bbde194ac11404b3c4bd32efc6f73dd19d07ccd382d8c8' #Your Client token

def SplitDataClient(data):
    d = data.split('\n')
    request = d[0].split(' ')
    method = [request[0],]
    if method[0] == 'GET':
        pass
    elif method[0] == 'POST':
        method.append(data.split('\r\n\r\n')[1])
    else:
        method.append('SOLO SE ADMINTEN SOLICITUDES GET/POST, LEA LA DOCUMENTACION PARA MAS INFORMACION.')
    print(method)
    return method

def Comunicattion(soc,ip):
    host = 'api.trello.com'
    while True:
        res = []
        try:
            soc.settimeout(2)
            while True:
                try:
                    r = soc.recv(3080)
                    res.append(r)
                    continue
                except socket.timeout:
                    if len(res) > 0:
                        break
                    else:
                        continue
                except:
                    print('Error to recived information')
                    break
            r = b''
            for i in res:
                r = r + i
            z = open('cache-{0}'.format(ip),'wb').write(r)
            z = open('cache-{0}'.format(ip),'rb').read().decode()
            r = SplitDataClient(z)
            if r[0] == 'GET':
                print('GET')
                path = '/1/boards/62517722f26860129a457743/lists?key={0}&token={1}'.format(api_token,client_token)
                re = requests.get(url='https://{0}{1}'.format(host,path),headers={'User-Agent':'X-Space Endpoint'})
                packet =  'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(re.content)))      
                packet = packet.encode() + re.content 
                soc.send(packet)
            elif r[0] == 'POST':
                print('POST')
                data = json.loads(r[1])
                path = '/1/cards'
                args = {'key':api_token,'token':client_token}
                url= 'https://{}{}'.format(host,path)
                if data['type'] == 'issue':
                    print('issue')
                    try: 
                        payload = {'name':data['title'],'desc':data['description'],'pos':'top','idList':'625177edbe1ff62478abca24'}
                    except:
                        msj = ''
                        packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                        soc.send(packet.encode() + msj.encode())
                    re = requests.post(url,params=args,json=payload)
                    msj = 'NEW ISSUE CREATED IN SPACE-X'
                    packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                    soc.send(packet.encode() + msj.encode())
                elif data['type'] == 'bug':
                    print('bug')
                    abc = list('qwertyuiopasdfghjklzxcvbnm')
                    palabra = ''
                    indice = ''
                    re = requests.get(url='https://api.trello.com/1/boards/62517722f26860129a457743/members',params=args)
                    members = json.loads(re.content)
                    member = members[randint(0,len(members))]['id']
                    for i in range(0,4):
                        palabra = palabra + abc[randint(0,len(abc))]
                        indice = indice + str(randint(0,9))
                    title = 'ERROR-{}-{}'.format(palabra,indice)
                    try:  
                        payload = {'name':title.upper(),'desc':data['description'],'idList':'62517722f26860129a457745','idLabels':['625177222d2ecec5005b168d',],'idMembers':[member,]}
                    except:
                        msj = ''
                        packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                        soc.send(packet.encode() + msj.encode())
                    re = requests.post(url,params=args,json=payload)
                    msj = 'NEW BUG CREATED IN SPACE-X'
                    packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                    soc.send(packet.encode() + msj.encode())
                elif data['type'] == 'task':
                    print('task')
                    if data['category'] == 'Maintenance' or data['category'] == 'maintenance':
                        Idlabel = '625177222d2ecec5005b1689'
                    elif data['category'] == 'Research' or data['category'] == 'research':
                        Idlabel = '625177222d2ecec5005b168b'
                    elif data['category'] == 'Test' or data['category'] == 'test':
                        Idlabel = '625177222d2ecec5005b1694'
                    try:
                        payload = {'name':data['title'],'idList':'62517722f26860129a457746','idLabels':[Idlabel,]}
                    except:
                        msj = ''
                        packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                        soc.send(packet.encode() + msj.encode())
                    re = requests.post(url,json=payload,params=args)
                    msj = 'NEW TASK CREATED IN SPACE-X'
                    packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                    soc.send(packet.encode() + msj.encode())
                else:
                    msj = 'NO TYPE, PLEACE READ DOCUMENTATION'
                    print(msj)
                    packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                    soc.send(packet.encode() + msj.encode())
            else:
                msj = r[1]
                print(msj)
                packet =  'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-length: {}\r\nConnection: keep-alive\r\nServer: Space-X Endpoint\r\n\r\n'.format(str(len(msj)))                      
                soc.send(packet.encode() + msj.encode())
            break
        except socket.timeout:
            print('TIMEOUT')    
            break

def ListenConn(soc):
    while True:
        try:
            soc.settimeout(1)
            conn, ipr = soc.accept()
            print('Connection recived from {}:{}'.format(ipr[0],ipr[1]))
            return conn, ipr
        except socket.timeout:
            continue
        except:
            print('Error waiting for connection')
            break

def CreateServer(port=8080,ip='127.0.0.1'):
    secure = True
    while secure:
        try:
            server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            server.bind((ip,port))
            server.listen(10)
            print('Server in {0}:{1}'.format(ip,port))
            iplist = []
            print('Waiting for connection')
            while True:
                conn, ip = ListenConn(server)
                print('Connection to {}:{} active'.format(ip[0],ip[1]))
                iplist.append(ip)
                Comunicattion(conn,ip[0])

        except socket.error:
            port = port + 1
            print('Address already in use,changing port to {0}'.format(str(port)))
            continue

CreateServer()
