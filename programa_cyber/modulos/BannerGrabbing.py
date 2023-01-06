#!/usr/bin/python

#Ref: https://github.com/surajsinghbisht054/py_banner_grabber/blob/master/pyBannerGrab/bannergrab.py 
import socket






	#Lendo variáveis
	ip = input("Digite o IP: ")
	porta = int(input("Digite a porta: "))

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#Inicia socket
	s.settimeout(3)  						#Define o timeout


	if (s.connect_ex((ip, porta))) == 0:				#Valida a conexão
		print("PORTA ABERTA!")
		s.connect((ip, porta))					#Inicia conexão
		if porta==80 or porta==443:				#Valida se o protocolo é HTTP ou HTTPS
			print("\n[+] PROTOCOLO HTTP OU HTTPS ENCONTRADO. IP : {}| PORTA : {}".format(ip, porta))
			message = "GET / HTTP/1.1\r\n\r\n".encode()	#Define uma mensagem para o servidor HTTP/HTTPS
			s.sendall(message)				#Envia mensagem resposta
			banner = s.recv(4096)				#Recebe Banner
			print(banner)					#Exibe o Banner
		else:
			banner = s.recv(1024)				#Recebe Banner
			print(banner)					#Exibe o Banner
		s.close()
	else:
		print("PORTA FECHADA!")
		
except Exception as e:
	print (e)
	s.close()




