#!/usr/bin/python
#Este programa utiliza o IF para verificar se um número está entre 0 e 100 utilizando IF

#Realizando a leitura do número a ser processado
x = int(input("Entre com o valor inteiro: "))

#Validando se o número está entre 0 e 100
if (x>=0) and (x<=100):
	print("O valor está entre 0 e 100")
#else:
#	print("O Valor NÃO está entre 0 e 100")
elif (x<0):
	print("O valor é menor que 0")
elif (x>100):
	print("O valor é maior que 100")
