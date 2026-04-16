import socket
import threading
import sys

#--CREATING GLOBAL CONSTANTS AND VARIABLES------------------------------------------------------------------------------------------------

HEADER =64                                                                    #Init len of packets
PORT = 5050                                                                         #reserved port for server 
server = socket.gethostbyname(socket.gethostname())                                 #gets the host machine IPV4
ADDR = (server , PORT)                                                              #A TUPLE of ip address and port of server
FORMAT = 'utf-8'                                                                    #decode and encode format
SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #created a SERVER obj
SERVER.bind(ADDR)                                                                   #binding port and server with server

#-----------------------------------------------------------------------------------------------------------------------------------------

#--Getting clients connection-------------------------------------------------------------------------------------------------------------

def clients(conn,addr): 
        i = 1
        print(f"Client connected {addr}")
        connection = True
        MESSAGE = str("Hi this is the msg from server to client")
        msg = MESSAGE.encode(FORMAT)
        data_len = len(msg)
        msg_len = str(data_len).encode(FORMAT)
        msg_len += b'' * (HEADER-len(msg_len))
        print(msg_len)
        conn.send(msg_len)
        conn.send(msg)
#--Reading the data of the clients--------------------------------------------------------------------------------------------------------
        #while connection:
        recived_data = conn.recv(HEADER).decode(FORMAT)
        print(recived_data)
        if recived_data:
                        recived_data = int(recived_data)
                        actual_data = conn.recv(recived_data).decode(FORMAT)
                        if actual_data == "DISCONNECT":
                                connection = False
                        if i == 1:
                                User = actual_data.upper()
                                i +=1
                                print(f"Client Name : {User}, Address = {ADDR}")

        conn.close()

#-----------------------------------------------------------------------------------------------------------------------------------------

#--Accepting the clients connection-------------------------------------------------------------------------------------------------------

def Server_start():
        SERVER.listen()                                                                 #initalization for accepting connections. #backlog = max connection
        print(f"SERVER IS LISTEING IN {server}")
        while True:                                                                     #infinite loop
                conn,addr = SERVER.accept()                                             #returened a server obj
                #client_list.append(conn)
                thread = threading.Thread(target=clients, args=(conn,addr))             #threading by targeting clients fun to thread and values to thread
                thread.start()
                print(f"ACTIVE NUMBER OF CLIENTS : {threading.active_count() - 1}")

#--Back to MAIN-----------------------------------------------------------------------------------------------------------------------------

print('STARTING server')
Server_start()

