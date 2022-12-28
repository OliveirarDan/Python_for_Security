#!/usr/bin/python
#Utilzando operadores lógicos

#Utilizando o operador AND - E
print(True and False)		#Exibe a validação entre: Verdadeiro E Falso
print(True and True)		#Exibe a validação entre: Verdadeiro E Verdadeiro
print(False and False)		#Exibe a validação entre: Falso E Falso

#Utilizando o operador OR - OU
print(True or False)		#Exibe a validação entre: Verdadeiro OU Falso
print(True or True)		#Exibe a validação entre: Verdadeiro OU Verdadeiro
print(False or False)		#Exibe a validação entre: Falso OU Falso

#Utlizando o operador NOT - NÃO
print(not True)			#Exibe a validação com o operador NOT
print(not False)		#Exibe a validação com o operador NOT
print(not(True and False))	#Exibe a validação entre: NÃO (Verdadeiro E Falso)
print(not(True or True))	#Exibe a validação entre: NÃO (Verdadeiro OU Verdadeiro)
print(True and not False)	#Exibe a validação entre: Verdadeiro E NÃO Falso

#Utilzando operadores relacionais e lógicos
print((2<3) and (2<5)) 		#Exibe a validação de E entre duas expressões relacionais verdadeiras
print((2<3) and (2<1)) 		#Exibe a validação de E entre duas expressões relacionais, uma verdadeira e outra falsa
