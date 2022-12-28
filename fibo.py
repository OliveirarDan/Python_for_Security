# Módulo que executa a sequência de Fibonacci

#!/usr/bin/python
def fib(n):    # Essa função escreve os termos da sequência de Fibonacci até n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

def fib2(n):   # Essa função retorna os termos da sequência de Fibonacci até n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result
