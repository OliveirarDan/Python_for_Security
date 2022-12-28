#!/usr/bin/python
#Criando um conjunto chamado s
s = {'Banana', 'Maça', 'Banana', 'Maça', 'Uva', 'Pera'}

print(s)		#Exibe os valores do conjunto

print('Banana' in s)	#Exibe a validação - Se 'Banana' está no conjunto s

print('Avocado' in s)	#Exibe a validação - Se 'Avocado' está no conjunto s

print('Banana' not in s)	#Exibe a validação - Se 'Banana' não está no conjunto s

print('Avocado' not in s)	#Exibe a validação - Se 'Avocado' não está no conjunto s


#Criando conjuntos de nomes a e b
conjunto_nomes_a = {'Carlos', 'Pedro', 'Diego', 'Antonio', 'João', 'Mauro', 'Elizeu'}
conjunto_nomes_b = {'Pedro', 'Mauro', 'Luiz', 'Carlos', 'Diego', 'Joaquim', 'Juvenal'}

print(conjunto_nomes_a - conjunto_nomes_b) # Exibe - O que está em a e não está em b

print(conjunto_nomes_b - conjunto_nomes_a) # Exibe - O que está em b e não está em a

print(conjunto_nomes_b & conjunto_nomes_a) # Exibe - O que está em a e em b 

print(conjunto_nomes_b | conjunto_nomes_a) # Exibe - O que está em a ou em b

print(conjunto_nomes_a ^ conjunto_nomes_b)  # Exibe - O que está em a e em b, mas que não está nos dois 
