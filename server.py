
import socket
import threading

HEADER = 64 #len of byte packet 
PORT = 5050 #selection of port to use
server = socket.gethostbyname(socket.gethostname()) #gets the host machine IPV4
ADDR = (server , PORT) #a tuple of ip address and port of client
FORMAT = 'utf-8'
DISCONNECT = 'Disconnect'
SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #created a SERVER obj
SERVER.bind(ADDR) #binding
def clients(conn,addr):
        i = 1
        print(f"Client connected {addr}")
       
        connection = True
        while connection:
                 recived_data = conn.recv(HEADER).decode(FORMAT)
                 if recived_data:
                        recived_data = int(recived_data)
                        actual_data = conn.recv(recived_data).decode(FORMAT)
                        if actual_data == DISCONNECT:
                                connection = False
                        if i == 1:
                                User = actual_data.upper()
                                i +=1
                                print(f"Client Name : {User}, Address = {ADDR}")
                        
                        
        conn.close()

def Server_start():
        SERVER.listen() #initalization for accepting connections. #backlog = max connection
        print(f"SERVER IS LISTEING IN {server}")
        while True: #infinite loop
                client_list = []
                conn,addr = SERVER.accept() #returened a server obj
                client_list.append(conn)
                thread = threading.Thread(target=clients, args=(conn,addr)) #threading by targeting clients fun to thread and values to thread
                thread.start()
                print(f"ACTIVE NUMBER OF CLIENTS : {threading.active_count() - 1}")
                while True:
                        i = 0
                        print(client_list[i])
                        i +=1

print('STARTING server')
Server_start()