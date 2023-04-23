#!/usr/bin/env python
# -*- coding utf-8 -*-


import os
import src.component.nmap as nmap
import src.component.gobuster as gobuster
import src.component.hydra as hydra
import src.component.file as files
import src.component.kriptoloji as kripto
import src.component.macchanger as macch
import src.component.firewall as firewall


def figlet():
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Efe Gorkem Umit")
	
def anaekran():
	print("""
	
	----------------------
	tools 
	
	-----------------------
	
	1-		NMAP
	2-		Gobuster
	3-		Hydra
	4-		Binwalk
	5-		kriptoloji
	6-		macchanger
	7-		Firewall 

	
	""")


figlet()
anaekran()

islemno= input("islem no Giriniz :  ")
if(islemno=="1"):
	nmap.nmap_hello()
if(islemno=="2"):
	gobuster.gobuster_hello()
if(islemno=="3"):
	hydra.hydra_hello()
if(islemno=="4"):
	files.file_information()
if(islemno=="5"):
	kripto.kriptoloji_hello()
if(islemno=="6"):
	macch.mac_degis()
if(islemno=="7"):
	firewall.firewall_hello()



	









