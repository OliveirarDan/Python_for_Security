#!/usr/bin/python 

#Este programa contém funções que manipulam arquivos

def le_arquivo(a):	
	f = open (str(a))	#equivalente a 'r' 
	return f
	
def escreve_arquivo(a):
	f = open (str(a), 'w')	#escreve em um arquivo no modo texto
	return f
	
def le_arquivo_binario(a):
	f = open(a, "r+b")
	return f
	
#print(le_arquivo("teste.txt").read())
#print(le_arquivo_binario("Senai.bmp").read())

try:
	f = open("teste.txt",'w')	# Abre o arquivo no modo de escrita
	f.write("Esse arquivo\n")	# Escreve a primeira linha no arquivo
	f.write("contém duas linhas\n")	# Escreve a segunda linha no arquivo
	f.write("contém três linhas\n")	# Escreve a terceira linha no arquivo
finally:
	f.close()			# Fecha o arquivo no modo de escrita	


g = open("teste.txt",'r')	# Abre o arquivo no modo leitura
print(g)			# Exibe informações do arquivo
print(g.read(4))		# Exibe somente os 4 primeiros itens do arquivo
print(g.read())			# Exibe o conteúdo do arquivo


