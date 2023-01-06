#!/usr/bin/python

#Importando módulos
import socket
import struct
import binascii

#Preparando socket
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))


while True:
	pkt = s.recvfrom(2048)
	ethhead = pkt[0][0:14]
	eth = struct.unpack("!6s6s2s",ethhead)
	print("--------Ethernet Frame--------")
	print("desination mac",binascii.hexlify(eth[0]))
	print("Source mac",binascii.hexlify(eth[1]))
	binascii.hexlify(eth[2])
	ipheader = pkt[0][14:34]
	ip_hdr = struct.unpack("!12s4s4s",ipheader)
	print("-----------IP------------------")
	print("Source IP", socket.inet_ntoa(ip_hdr[1]))
	print("Destination IP", socket.inet_ntoa(ip_hdr[2]))
