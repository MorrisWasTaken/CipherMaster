# This is an Example on how to create Custom modules for CipherMaster.
# This Example is a Reverse Cipher

# Every module Requires a Name and a Info variable to be displayed in the app
name = "Reverse" # this is the name of the module in the app
info = "Reverses the string." # this is the explanation of the module in the app
command = "rev" # This is the command used to select this module

# all modules Require a encrypt() and a decrypt() function
def encrypt(text): # you need to include the "text" variable in the function to ge access to the users text input
    return text[::-1] # then in the encrypt() function you run your ciphers logic, at the end you need to add a "return" statement with the encrypted text

def decrypt(text):
    return text[::-1]

# Note: the app will automatically detect your cipher and run it if you did everything correct
# Note: if you need user input you can use "YourVariable = input("Your Prompt: ")"

# example filestructure for reference:
#
# CipherMaster/
# ├── CipherMaster.py
# ├── Modules/
# │   ├── CaesarCipher.py
# │   ├── MorseCipher.py
# │   └── ExampleCipher.py  ← 🧩 you can base your own on this