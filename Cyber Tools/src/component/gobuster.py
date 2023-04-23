#!/usr/bin/env python
# -*- coding utf-8 -*-

import os

def gobuster_hello():
   print("""  
    -----------------------------
              GOBUSTER
    -----------------------------
    0-         Genel         rockyou.txt
    1-         Directory     common.txt
    2-         Username      names.txt
    3-         Directory     apache-user-enum-1.0.txt
    4-         Directory     apache-user-enum-2.0.txt
    5-         Directory     directory-list-1.0.txt
    6-         Directory     directory-list-2.3-medium.txt
    7-         Directory     directory-list-2.3-small.txt
    8-         Directory     directory-list-lowercase-2.3-medium.txt
    9-         Directory     directory-list-lowercase-2.3-small.txt
    10-        Directory     medium.txt
    11-        Password      fasttrack.txt
    12-        Password      best110.txt

    """)
   
   ip = input(" IP adresi yada Web sitesi : ")
   islemno = input(" use : ")
   dosya =''
   if(islemno=='0'):
       dosya ="rockyou.txt"
   if(islemno=='1'):
       dosya ="common.txt"
   if(islemno=='2'):
       dosya ="names.txt"
   if(islemno=='3'):
       dosya ="apache-user-enum-1.0.txt"
   if(islemno=='4'):
       dosya ="apache-user-enum-2.0.txt"
   if(islemno=='5'):
       dosya ="directory-list-1.0.txt"
   if(islemno=='6'):
       dosya ="directory-list-2.3-medium.txt"
   if(islemno=='7'):
       dosya ="directory-list-2.3-small.txt"
   if(islemno=='8'):
       dosya ="directory-list-lowercase-2.3-medium.txt"
   if(islemno=='9'):
       dosya = "directory-list-lowercase-2.3-small.txt"
   if(islemno=='10'):
       dosya = "medium.txt"
   if(islemno=='11'):
       dosya = "fasttrack.txt"
   if(islemno=='12'):
       dosya = "best110.txt"
    
   os.system("gobuster dir -u "+ ip + " -w ./src/wordlist/"+ dosya)
