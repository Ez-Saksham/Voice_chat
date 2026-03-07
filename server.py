
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
        print(f"Client connected {addr}")

        connection = True
        while connection:
                raw_data = conn.recv(HEADER).decode(FORMAT)
                if raw_data:
                        raw_data = int(raw_data)
                        actual_data = conn.recv(raw_data).decode(FORMAT)
                        if actual_data == DISCONNECT:
                                connection = False
                        print(f"{addr} {actual_data}")

        conn.close()

def Server_start():
        SERVER.listen() #initalization for accepting connections. #backlog = max connection
        print(f"SERVER IS LISTEING IN {server}")
        while True: #infinite loop
                conn,addr = SERVER.accept()
                thread = threading.Thread(target=clients, args=(conn,addr)) #threading by targeting clients fun to thread and values to thread
                thread.start()
                print(f"ACTIVE NUMBER OF CLIENTS : {threading.active_count() - 1}")

print('STARTING server')
Server_start()