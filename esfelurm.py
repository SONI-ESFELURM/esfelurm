import sys
import os
os.system("pip install colorama")
from time import sleep
from colorama import Fore


print ("""




    \033[01;32m   Hello, thank you for looking at the esfelurm script""")

print (Fore.RED+"    [+] "+Fore.GREEN+"Script Filtering Rubika and SMS Bomber ")
print ("")
print (Fore.RED+"    [+] "+Fore.GREEN+"Written by Esfelurm ")
print ("")
print (Fore.RED+"    [+] "+Fore.YELLOW+"This script has an educational aspect, please refrain from any editing without mentioning the source ")


print (Fore.RED+ "")
K = """ 

SMS BOMBER and FILTERING and Hide text in photo                                              

"""
for c in K:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.02)

esfelurm = input("""\033[01;32m
Filtering Rubika [1]
\033[00;35m__________________
\033[01;32msms Bomber [2]
\033[00;35m__________________
\033[01;32mHide text in photo [3]
\033[00;35m__________________
\033[01;32m    number : """)

if esfelurm == "2":
	        os.system("python spam_bomber.py")

print ("""


      Bye Bye | i'm ESFELURM !!!!!!
      
""")
	
if esfelurm != "2":
        print("")

if esfelurm == "3":
            os.system("python text.py")

print ("""


      Bye Bye | i'm ESFELURM !!!!!!
      
""")
            
if esfelurm != "3":
        print("")  
        

if esfelurm == "1":
	        os.system("python Filtering.py")

print ("""


      Bye Bye | i'm ESFELURM !!!!!!
      
""")

os.system("exit")

if esfelurm != "1":
        print("")  
        
