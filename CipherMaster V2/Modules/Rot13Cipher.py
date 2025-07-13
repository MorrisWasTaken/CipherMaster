name = "ROT13"
info = "ROT13 Shifts each letter 13 positions back into the alphabet, wrapping around at the end."
command = "rot"

def encrypt(text):
    result = []
    for a in text:
        ASCIIcode = ord(a)
        if ASCIIcode >= 65 and ASCIIcode <= 90:
            ASCIIcode -= 65
            ASCIIcode += 13
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 65
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        elif ASCIIcode >= 97 and ASCIIcode <= 122:
            ASCIIcode -= 97
            ASCIIcode += 13
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 97
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        else:
            result.append(a)
    strRes = "".join(result)
    return strRes

def decrypt(text):
    result = []
    for a in text:
        ASCIIcode = ord(a)
        if ASCIIcode >= 65 and ASCIIcode <= 90:
            ASCIIcode -= 65
            ASCIIcode += 13
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 65
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        elif ASCIIcode >= 97 and ASCIIcode <= 122:
            ASCIIcode -= 97
            ASCIIcode += 13
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 97
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        else:
            result.append(a)
    strRes = "".join(result)
    return strRes