#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


	
def mac_degis():
	print("""
	
	----------------------
		mac changer 
	
	-----------------------
	
	0-		mac değiştir
	1-		mac elle değiştir
	2-		orjinal mac


	
	""")
	
	islemno= input("islem no Giriniz :  ")
	if(islemno=="0"):
		os.system("ifconfig eth0 down")
		os.system("sudo macchanger -r eth0")
		os.system("ifconfig eth0 up")
		print("mac değişti.")
	if(islemno=="1"):
		mac= input("mac address Giriniz :  ")
		os.system("ifconfig eth0 down")
		os.system("sudo macchanger --mac "+mac+" eth0")
		os.system("ifconfig eth0 up")
		print("mac elle değişti.")	
	if(islemno=="2"):
		os.system("ifconfig eth0 down")
		os.system("sudo macchanger -p eth0")
		os.system("ifconfig eth0 up")
		print("mac adresiniz orjinal.")	
		

