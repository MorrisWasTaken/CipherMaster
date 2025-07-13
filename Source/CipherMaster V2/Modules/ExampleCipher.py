# This is an Example on how to create Custom modules for CipherMaster.
# This Example is a Reverse Cipher

# Every module Requires a Name and a Info variable to be displayed in the app
name = "Reverse" # this is the name of the module in the app
info = "Reverses the string." # this is the explanation of the module in the app

# all modules Require a encrypt() and a decrypt() function
def encrypt(text): # currently you need to include the "text" variable in the function, but you cannot add other variables without hardcoding a input statement into the source code (wich you are free to do)
    return text[::-1] # then in the encrypt() function you run your ciphers logic, at the end you need to add a "return" statement with the encrypted text

def decrypt(text):
    return text[::-1]

# the app will then automatically detect your cipher and run it if you did everything correct
#
# example filestructure for reference:
#
# CipherMaster/
# ├── CipherMaster.py
# ├── Modules/
# │   ├── CaesarCipher.py
# │   ├── MorseCipher.py
# │   └── ExampleCipher.py  ← 🧩 you can base your own on this
