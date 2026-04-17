import socket
import threading
import sys

HEADER = 64
Client_IP_list = []
Client_PORT_list = []

USER_CHOICE = int(input('Type 1 for custom IP / Type 2 for Local IP : '))
SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if USER_CHOICE == 1:
                Custom_ip = input('ENTER Custom IP/URL :')
                host_ip = Custom_ip
elif USER_CHOICE == 2:
                host_ip = socket.gethostbyname(socket.gethostname()) 
else:
        print('Please Choose a valid response')
        sys.exit()
PORT = int(input('ENTER THE PORT NUMBER : '))
try:
        ADDR =(host_ip,PORT)
        SERVER.bind(ADDR)
except ValueError:
        print('Please enter a valid response!')
       
except NameError:
        print("YOU MUST CHOOSE A VALID RESPONSE!")
except OverflowError:
        print('PORT must be in range')
Encoding_Format = "utf-8"

#---------------------------------------------------------------------------------------------------------------------------------------------#

def Threading(Client,Address):
   Succesful_Conection_Notify(Client,Address)
   Client_Work(Client,Address)
#---------------------------------------------------------------------------------------------------------------------------------------------#

def Succesful_Conection_Notify(Client,Address):

        Message = "Connection established succesfully with the server!" #only bytes can be send over network
        binary_message = Message.encode(Encoding_Format)                #and only strings canbe converted to bytes
        length_of_binary_message = str(len(binary_message)).encode(Encoding_Format).zfill(64)
        #sending_message_length = length_of_binary_message  ( INSTED OF USING ZFILL WE CAN DO MANUAL PADDING LIKE THIS)
        #sending_message_length += b' ' * (HEADER-len(length_of_binary_message))
        Client.send(length_of_binary_message)
        Client.send(binary_message)


#---------------------------------------------------------------------------------------------------------------------------------------------#

def Client_Work(Client,Address):
        Connection = True
        print(f"Client is connected at : {Address}")
        while Connection:
                String_DATA_LENGTH = Client.recv(HEADER).decode(Encoding_Format)
                if String_DATA_LENGTH:
                        Incoming_DATA_LENGTH = int(String_DATA_LENGTH)
                        Plain_data = Client.recv(Incoming_DATA_LENGTH).decode(Encoding_Format)
                        print(Plain_data)
        Client.close()
#---------------------------------------------------------------------------------------------------------------------------------------------#

def Start_Server():
        SERVER.listen()
        i = 0
        print(f"The server is listening in : [{host_ip}] with port number : [{PORT}]")
        while True:
                client_connection, client_address = SERVER.accept()
                thread = threading.Thread(target=Threading, args=(client_connection,client_address)) 
                thread.start()
                print(f'Client Successfully Connected [NUMBER OF ACTIVE CLIENTS : {threading.active_count()-1}]')
                Client_IP_list , Client_PORT_list = client_address
                print(Client_PORT_list)
                print(Client_IP_list)
                i +=1
#---------------------------------------------------------------------------------------------------------------------------------------------#

Start_Server()