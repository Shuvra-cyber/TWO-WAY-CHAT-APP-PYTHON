import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5555))

s.listen(5)
clt , add = s.accept()
print("Connection to ",str(add)," established")

while True:
    
    data = clt.recv(1024)
    if not data:
        break
    print("client: ",data.decode("utf-8"))
    send = input("Enter your message:\t")
    clt.send(send.encode("utf-8"))
    
clt.close()