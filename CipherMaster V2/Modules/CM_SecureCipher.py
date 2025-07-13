from Utils.CM_Secure import CaeEnc, CaeDec, Atbash

name = "CM Secure"
info = "A special cipher developed for this app"
command = "sec"

def encrypt(text):
    caeText = CaeEnc(text, 7)
    cabaText = Atbash(caeText)
    raiText = RailFenceEnc(cabaText, 5)
    rotText = Rot13(raiText)
    result = Base64Enc(rotText)
    return result

def decrypt(text):
    baseText = Base64Dec(text)
    rotText = Rot13(baseText)
    raiText = RailFenceDec(rotText, 5)
    atbText = Atbash(raiText)
    result = CaeDec(atbText)
    return result