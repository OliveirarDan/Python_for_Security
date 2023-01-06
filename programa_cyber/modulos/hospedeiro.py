#!/usr/bin/python

#Importando o módulo socket
import socket 

#Declarando variáveis 
ip="127.0.0.1"			#Define endereço do servidor (local)
porta=43210			#Define a porta para o serviço

try:
	obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	#Inicia um objeto do tipo Socket
	obj_socket.bind((ip,porta))	#Vincula o socket ao endereço e porta
	obj_socket.listen()		#Habilita o servidor a receber conexões

	#Realiza a conexão
	print("Aguardando Conexão...")
	while True:
		con, cliente = obj_socket.accept() 	#Aceita a conexão e define a conexão com cliente
		print("Conectado com: ", cliente)	#Exibe cliente conectado
		
		#Recebe e envia mensagem
		while True:
			msg_recebida = str(con.recv(1024))		#Recebe a mensagem através da conexão
			print("Recebemos: " + str(msg_recebida)[2:-1])		#Exibe mensagem recebida
			msg_enviada = bytes(input("Sua resposta: "), 'utf-8')	#Define a mensagem mensagem a ser enviada
			con.send(msg_enviada)		#Envia a mensagem através da conexão
			break
		con.close()	#Fecha a conexão
finally: 
	obj_socket.close()	
	
	
