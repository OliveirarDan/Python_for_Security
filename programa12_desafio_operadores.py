#!/usr/bin/python
#Este programa compara faz a leitura de um valor e verifica se ele é maior 0 e menor que 100

#Utilizando o input para leitura e armazenado do valor inteiro em X
x = int(input("Entre com o valor inteiro:" ))

#Validando valor armazenado
print(x>=0)			#Exibe a validação: x é maior ou igual a 0
print(x<=100)			#Exibe a validação: x é menor ou igual a 100

resp =(x>=0) and (x<=100) 	#Valida: x é maior ou igual a 0 E menor ou igual a 100?
	
print("O valor é menor ou igual a 10? "+ str(resp))
