import os
os.system("pip install stepic")
os.system("pip install colorama")
import stepic
from PIL import Image
from colorama import Fore

def encode(file):
    img = Image.open(file)
    text = input(" \033[01;32m Text : ")
    img_stegano = stepic.encode(img,text.encode())
    name = input(Fore.RED+"Output Name : ")
    img_stegano.save(name)
def decode(file):
    img = Image.open(file)
    decoded = stepic.decode(img)
    return decoded
file  = input(Fore.YELLOW+"name file : ")

print ("esfelurm")
print("")
print(Fore.RED+"Encode "+Fore.GREEN+"[A]")
print(Fore.RED+"Decode "+Fore.GREEN+"[B]")
mode = input("\033[01;32m A or B :")
if mode == "A":
    encode(file)
elif mode == "B":
    text = decode(file)
    print(" ")
    print("\t"+text)
else:
    print(Fore.RED+"Fuck off")