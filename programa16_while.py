#!/usr/bin/python
#Este programa lê, valida e exibe números enquanto eles estiverem entre 0 e 100

#Utilizando o input para leitura e armazenado do valor inteiro em X
x = int(input("Entre com o valor inteiro:" ))

while (x>=0) and (x<=100):
	print(f"O valor {x} está entre 0 e 100")
	x = int(input("Entre com o valor inteiro novamente:" ))
else:
	print(f"O valor {x} NÃO está entre 0 e 100, Tchau!")
