import socket, pickle

host="10.250.86.32"
port = 19382                 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
st="Hello World im client1"
s.sendall(st.encode())
data = s.recv(1024)
s.close()
print((data.decode()))