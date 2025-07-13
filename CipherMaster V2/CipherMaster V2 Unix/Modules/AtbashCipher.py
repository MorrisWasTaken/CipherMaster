name = "Atbash"
info = "Replaces every character to its Mirrored position in the alphabet (A -> Z, B -> Y etc.)"
command = "atb"

def encrypt(text):
    result = []
    for a in text:
        ASCIIcode = ord(a)
        if ASCIIcode >= 65 and ASCIIcode <= 90:
            ASCIIcode -= 65
            mapdCode = 25 - ASCIIcode
            mapdCode += 65
            mapdCode = chr(mapdCode)
            result.append(mapdCode)
        elif ASCIIcode >= 97 and ASCIIcode <= 122:
            ASCIIcode -= 97
            mapdCode = 25 - ASCIIcode
            mapdCode += 97
            mapdCode = chr(mapdCode)
            result.append(mapdCode)
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
            mapdCode = 25 - ASCIIcode
            mapdCode += 65
            mapdCode = chr(mapdCode)
            result.append(mapdCode)
        elif ASCIIcode >= 97 and ASCIIcode <= 122:
            ASCIIcode -= 97
            mapdCode = 25 - ASCIIcode
            mapdCode += 97
            mapdCode = chr(mapdCode)
            result.append(mapdCode)
        else:
            result.append(a)
    strRes = "".join(result)
    return strRes