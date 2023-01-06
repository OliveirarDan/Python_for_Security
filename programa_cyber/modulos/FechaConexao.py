#!/usr/bin/python

#Importando o módulo socket
import socket 

servidor="127.0.0.1"		#Definindo endereço do servidor (local)
porta=43210			#Definindo a porta para o serviço

obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	#
obj_socket.bind((servidor,porta))
obj_socket.close()
