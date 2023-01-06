#!/usr/bin/python
#Este é o programa principal

#Imports
import sys
sys.path.append('/home/kali/Desktop/Python_Scripts/programa_cyber/modulos/') #definindo ambiente com módulos
import CyberUtils

continua = True



while continua == True:
	CyberUtils.menu_principal()
	continua = CyberUtils.continua_programa()
	


CyberUtils.insere_texto("Até Mais!")
