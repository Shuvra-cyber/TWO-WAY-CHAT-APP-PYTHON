import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),5555))

#msg = s.recv(1024)
#print(msg.decode("utf-8"))

client_msg = input("Enter your message:\t")

while client_msg.lower() != "exit":
    s.send(client_msg.encode("utf-8"))
    data = s.recv(1024)
    print("From server: ",data.decode("utf-8"))
    client_msg = input("Enter your message:\t")

s.close()