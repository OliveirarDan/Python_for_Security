#!/usr/bin/python
#Este é o programa principal

#Imports
import sys
sys.path.append('/home/kali/Desktop/Python_Scripts/programa_cyber/modulos/') #definindo ambiente com módulos
import cyberUtils

continua = True



while continua == True:
	cyberUtils.menu()
	continua = cyberUtils.continuaPrograma()
	


cyberUtils.insereTexto("Até Mais!")
