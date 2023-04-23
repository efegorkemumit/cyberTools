#!/usr/bin/env python
# -*- coding utf-8 -*-

import os
	
def file_information():
	print("""
	
	----------------------
	 BINWALK FILE INFORMATION
	 -- Dosyanın masaüstünde olması lazım-- 
	
	-----------------------
	
	0-		use
	
	
	""")



	islemno= input("islem no Giriniz :  ")
	dosyaadi= input("Dosya adı Giriniz :  ")
	if(islemno=="0"):
		os.system("binwalk -e /home/kali/Desktop/"+dosyaadi)
	



	









