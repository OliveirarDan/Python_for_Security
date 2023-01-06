#!/usr/bin/python
#Este programa contém diversas utilizades(funções) para o Programa Cyber

import os

#Função para exibir cabeçalho com texto padronizado
def insere_texto(m):
	print(m)

def insere_titulo(m):
	m=m.upper()
	print("************ " + m + " ************")


def limpa_tela():
	os.system("clear")

def continua_programa():
	r = input("Deseja voltar ao menu principal? (S/N)")	 
	if r == "S" or r =="s":
		return True
	elif r == "N" or r =="n":
		return False
	continuaPrograma()	

#Função para chamar o menu do programa
def menu_principal(): 
	limpaTela()
	insereTitulo ("Menu principal")	
	insereTitulo ("Escolha uma opção:")

	


		

