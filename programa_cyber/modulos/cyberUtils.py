#!/usr/bin/python
#Este programa contém diversas utilizades(funções) para o Programa Cyber

import os

#Função para exibir cabeçalho com texto padronizado
def insereTexto(m):
	print(m)

def insereTitulo(m):
	m=m.upper()
	print("************ " + m + " ************")


def limpaTela():
	os.system("clear")

def continuaPrograma():
	r = input("Deseja voltar ao menu principal? (S/N)")	 
	if r == "S" or r =="s":
		return True
	elif r == "N" or r =="n":
		return False
	continuaPrograma()	

#Função para chamar o menu do programa
def menu(): 
	limpaTela()
	insereTitulo ("Menu principal")	
	insereTitulo ("Escolha uma opção:")

	


		

