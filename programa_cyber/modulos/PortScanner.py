#!/usr/bin/python

import sys
import socket

ipAddress = input("digite o endereço IP: ")

def scan_conhecidas(ip):
	print("---PORTAS CONHECIDAS - 1 - 1023---")
	for ports in range(1,1023):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		if s.connect_ex((ipAddress, ports)) == 0:
			print(f"Porta {ports} Aberta!")
			s.close()


def scan_registradas(ip):
	print("---PORTAS REGISTRADAS - 1024 - 49151---")
	for ports in range(1024,49151):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		if s.connect_ex((ipAddress, ports)) == 0:
			print(f"Porta {ports} Aberta!")
			s.close()

def scan_dinamicas(ip):
	print("---PORTAS DINÂMICAS 49152 - 65535---")
	for ports in range(49152,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		if s.connect_ex((ipAddress, ports)) == 0:
			print(f"Porta {ports} Aberta!")
			s.close()


scan_conhecidas(ipAddress)

scan_registradas(ipAddress)

scan_dinamicas(ipAddress)
