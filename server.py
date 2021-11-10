import socket, pickle
from _thread import *

host="10.250.86.32"
port=19382

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(host, port)

s.listen(1)

def RecieveData (conn):
	print(conn)
	print("Data recieved : ")
	x=conn.recv(1024)
	print(x.decode())
	x=x.decode()
	
	while 1:
		if not x:
			break
		print(type(x))
		print(x)
		reply= "Data successfully received" +x
		x="Welcome to server "
		conn.sendall(x.encode())
		conn.sendall(reply.encode())
	conn.close()

while True:
	conn, addr=s.accept()
	start_new_thread(RecieveData(conn))

s.close()