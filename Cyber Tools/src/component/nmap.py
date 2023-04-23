#!/usr/bin/env python
# -*- coding utf-8 -*-

import os

def nmap_hello():
	print("""
	
	----------------------
	NMAP 
	
	-----------------------
	
	0-		NMAP
	1-		-sC -sV
	2-
	
	
	""")
	
	ip = input(" İp Adresi Giriniz : ")
	islemno= input("islem no Giriniz :  ")
	if(islemno=="0"):
		os.system("nmap "+ip)
	if(islemno=="1"):
		os.system("nmap -sC -sV "+ip)
		
	







