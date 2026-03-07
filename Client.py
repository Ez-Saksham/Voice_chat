import socket

HEADER = 64 #len of byte packet 
PORT = 5050 #selection of port to use
FORMAT = 'utf-8'
DISCONNECT = 'Disconnect'
server = "127.0.1.1"
ADDR = (server,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def sending(data):
    msg = data.encode(FORMAT)
    data_length = len(msg)
    send_len = str(data_length).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(msg)
    print(client.recv(2048))