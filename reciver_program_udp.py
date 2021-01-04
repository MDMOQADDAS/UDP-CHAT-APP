import os
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.43.68"
port = 1234
s.bind( (ip ,  port) )



while True:
	print("""
		press 1 : To Send
		press 2 : To Recive
		press 3 : To Exit""")
	ch = int( input("Enter ur choice : "))
	if ch==1:
		msg = input("Ener the mesage : ")
		s.sendto(msg.encode() , ("192.168.8.115" , 12345) )
	elif ch==2:
		x = s.recvfrom(20)
		clientIP = x[1][0]
		data = x[0].decode()
		os.system("tput setaf 3")
		print(clientIP + " : " + data)	
		os.system("tput setaf 7")
	elif ch==3: break
	else:
		print("wrong input")
	input("done..")
	os.system("clear")


	
	
	
