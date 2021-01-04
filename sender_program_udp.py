import socket
import threading
import os

s = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

s.bind ( ( "192.168.43.68" , 1234 ) ) 

os.system("tput setaf 4")
print("ME \t\t\t Other")
print("-- \t\t\t -----")
os.system("tput setaf 7")

def recver():
	while True:
		x = s.recvfrom(20)
		clientIP = x[1][0]
		data = x[0].decode()
		os.system("tput setaf 3")
		print("\t\t\t" , clientIP + " : "  + data)
		print("\t\t\t============================")
		os.system("tput setaf 7")

def sender():
	while True:
		input2 = input()
		s.sendto(input2.encode() , ("192.168.43.32" , 786) )


send = threading.Thread(target  = sender )

rcv = threading.Thread(target = recver)
	



rcv.start()

send.start()
