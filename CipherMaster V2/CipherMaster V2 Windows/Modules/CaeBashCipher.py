from Utils.CaeBash import Atbash, Caesarencrypt, Caesardecrypt

name = "Caebash"
info = "A mix of Caesar and Atbash"
command = "caba"

def encrypt(Ctext):
    Cshift = int(input("Enter shift amount: "))
    CaeEnctext = Caesarencrypt(Ctext, Cshift)
    Enctext = Atbash(CaeEnctext)
    return Enctext

def decrypt(Ctext):
    Enctext = Atbash(Ctext)
    Dectext = Caesardecrypt(Enctext)
    return Dectext