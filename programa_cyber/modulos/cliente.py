#!/usr/bin/python

#importando o módulo socket
import socket

#Declarando variáveis
ip="127.0.0.1"			#Define endereço do servidor (local)
porta=43210			#Define a porta para o serviço

try: 	
	#Realiza a conexão, o envio e o recebimento de mensagens
	while True:
		obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Inicia um objeto do tipo Socket
		obj_socket.connect((ip, porta))			#Conecta ao socket através do endereço e porta
	 	
		mensagem = bytes(input("Mensagem: "), 'utf-8')	#Define a mensagem mensagem a ser enviada
		obj_socket.send(mensagem)			#Envia a mensagem através da conexão
	 	
		resposta = obj_socket.recv(1024)		#Recebe a mensagem através da conexão
		print("Recebido: ", str(resposta)[2:-1]) 	#Exibe mensagem recebida
		
finally: 
	obj_socket.close()
	
