#!/usr/bin/python
#Este programa contém funções de manipulação de arquivos

import CyberUtils

#Cria arquivo
def cria_arquivo(nome_arquivo,conteudo_inicial):
	try:
		f = open(nome_arquivo, 'w')
		f.write(conteudo_inicial + "\n")
	finally:
		f.close()

#Anexa conteúdo ao arquivo
def anexa_dado(nome_arquivo, conteudo):
	try:
		f = open(nome_arquivo, 'a')
		f.write(conteudo)
	finally:
		f.close()


#Le arquivo
def le_arquivo(nome_arquivo):
	try:
		f = open(nome_arquivo, 'r')
		print(f.readlines())
	finally:
		f.close()


#Menu de utilização do módulo
def menu_manipula_arquivo():
	CyberUtils.limpa_tela()
	CyberUtils.insere_titulo("Manipulando Arquivos")
	CyberUtils.insere_texto("Escolha uma opção:")
	CyberUtils.insere_texto("1 - Criar Arquivo \n2 - Anexar dado \n3 - Ler Aquivo")
	r = str(input(": "))
	if (r == "1"):
		nome_arquivo = input("Nome do arquivo: ")
		conteudo = input("Conteúdo inicial do arquivo: ")
		cria_arquivo(nome_arquivo,conteudo)
	elif (r == "2"): 
		nome_arquivo = input("Nome do arquivo: ")
		conteudo = input("Conteúdo adicional: ")
		anexa_dado(nome_arquivo,conteudo)
	elif (r == "3"):
		nome_arquivo = input("Nome do arquivo: ")
		le_arquivo(nome_arquivo)
	else:
		print("Opção Inválida!")


		
