#!/usr/bin/python
#Definindo lista de idades com 5 valores
idades = [10, 12, 14, 17, 20]

#Exibindo itens da lista
print(idades[0]) 		#Exibe o primeiro item da lista

print(idades[4])		#Exibe o ultimo item da lista

print(idades[0:3])		#Exibe do primeiro ao terceiro item da lista

idades[0] = 12			#Altera o valor do primeiro item da lista

print(idades)			#Exibe a lista completa


#Definindo a lista de listas de idades da escola
escola = [[10, 12, 13, 17, 20], 
	[8, 13, 12, 10, 9], 
	[7, 9, 11, 12, 13],	
	[9, 10, 11, 9, 12]]
print(escola) 			#Retorna a lista completa

print(escola[0][0])		#Retorna o primeiro valor da lista

print(escola[3][0])		#Retorna a primeira posição da última sala

print(escola[0][4])		#Retorna a última posição da primeira sala

print(escola[3][4])		#Retorna a última posição da última sala

print(escola[0][-4:-2])		#Retorna valores a partir de index negativo
