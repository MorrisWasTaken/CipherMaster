def Atbash(text):
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

def Caesarencrypt(text):
    shift = int(input("Enter shift amount: "))
    result = []
    for a in text:
        ASCIIcode = ord(a)
        if ASCIIcode >= 65 and ASCIIcode <= 90:
            ASCIIcode -= 65
            ASCIIcode += shift
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 65
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        elif ASCIIcode >= 97 and ASCIIcode <= 122:
            ASCIIcode -= 97
            ASCIIcode += shift
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 97
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        else:
            result.append(a)
    strRes = "".join(result)
    return strRes

def Caesardecrypt(text):
    results = []
    for shift in range(1, 26):

        tempResult = []
        for a in text:
            ASCIIcode = ord(a)
            if ASCIIcode >= 65 and ASCIIcode <= 90:
                ASCIIcode -= 65
                ASCIIcode -= shift
                ASCIIcode = ASCIIcode % 26
                ASCIIcode += 65
                ASCIIcode = chr(ASCIIcode)
                tempResult.append(ASCIIcode)
            elif ASCIIcode >= 97 and ASCIIcode <= 122:
                ASCIIcode -= 97
                ASCIIcode -= shift
                ASCIIcode = ASCIIcode % 26
                ASCIIcode += 97
                ASCIIcode = chr(ASCIIcode)
                tempResult.append(ASCIIcode)
            else:
                tempResult.append(a)
        decrypted_string = "".join(tempResult)
        results.append(decrypted_string)
    return results