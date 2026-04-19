import socket
HEADER = 64      # fixed-size prefix telling the server how big the message is
PORT   = 5050    # port the server listens on
FORMAT = 'utf-8'  # text encoding for bytes conversion
DISCONNECT = 'Disconnect'  # magic string to signal end of session
server = "127.0.1.1"                               # server IP address
ADDR   = (server, PORT)                              # (IP, port) tuple for socket functions
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP socket
client.connect(ADDR)                                 # establish connection to server
name =''
i = True 
#---------------------------------------------------------------------------------------------------------------------------------------------#

def Starter(i):
    Connection_notify(i)



#---------------------------------------------------------------------------------------------------------------------------------------------#


def sending(data):
    msg = data.encode(FORMAT)            # str → bytes
    data_length = len(msg)                   # byte count of message
    send_len  = str(data_length).encode(FORMAT).zfill(64) #encoding with padding
    #send_len += b' ' * (HEADER - len(send_len))  # maual pad to exactly 64 bytes
    client.send(send_len)                    # ① header — server reads this first
    client.send(msg) 

#---------------------------------------------------------------------------------------------------------------------------------------------#

def Message(i):
    i = False
    while True:
        msg = input("--> ")
        sending(msg)

#---------------------------------------------------------------------------------------------------------------------------------------------#


def Connection_notify(i):
    if i == True:
        name =input('ENTER YOUR NAME : ')
        sending(name)
    while True:
        length_data = client.recv(64).decode(FORMAT) # IN CASE OF MANUAL PADDING USE .strip()
        length = int(length_data)
        if length:
            actual_message = client.recv(length).decode(FORMAT)
            print(actual_message)
            print("                                                     ")
        Message(i)
#---------------------------------------------------------------------------------------------------------------------------------------------#
Starter(i)
