
import socket
HEADER = 64      # fixed-size prefix telling the server how big the message is
PORT   = 5050    # port the server listens on
FORMAT = 'utf-8'  # text encoding for bytes conversion
DISCONNECT = 'Disconnect'  # magic string to signal end of session
server = "127.0.1.1"                               # server IP address
ADDR   = (server, PORT)                              # (IP, port) tuple for socket functions
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP socket
client.connect(ADDR)                                  # establish connection to server

def sending(data):
    msg = data.encode(FORMAT)            # str → bytes
    data_length = len(msg)                   # byte count of message
    send_len  = str(data_length).encode(FORMAT)  # length as bytes
    send_len += b' ' * (HEADER - len(send_len))  # pad to exactly 64 bytes
    client.send(send_len)                    # ① header — server reads this first
    client.send(msg) 


   

name = input('ENTER YOUR USERNAME : ')
sending(name)   # first message = username handshake
while True:
          # send to server
    message = client.recv(1024).decode(FORMAT)
    print(message)
    if message:
        message = int(message)
        actual_message = client.recv(message).decode(FORMAT)
        print(actual_message)
    
    msg = input('')   # block until user types something
    sending(msg)