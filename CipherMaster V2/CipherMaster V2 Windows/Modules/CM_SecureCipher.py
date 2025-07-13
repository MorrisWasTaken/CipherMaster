from Utils.CM_Secure import CaeEnc, CaeDec, Atbash, RaiEnc, RaiDec, Rot13, Base64Enc, Base64Dec

name = "CM Secure"
info = "A special cipher developed for this app"
command = "sec"

def encrypt(text):
    caeText = CaeEnc(text)
    cabaText = Atbash(caeText)
    raiText = RaiEnc(cabaText)
    rotText = Rot13(raiText)
    result = Base64Enc(rotText)
    return result

def decrypt(text):
    baseText = Base64Dec(text)
    rotText = Rot13(baseText)
    raiText = RaiDec(rotText)
    atbText = Atbash(raiText)
    result = CaeDec(atbText)
    return result