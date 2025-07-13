import base64

def CaeEnc(text):
    result = []
    for a in text:
        ASCIIcode = ord(a)
        if ASCIIcode >= 65 and ASCIIcode <= 90:
            ASCIIcode -= 65
            ASCIIcode += 7
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 65
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        elif ASCIIcode >= 97 and ASCIIcode <= 122:
            ASCIIcode -= 97
            ASCIIcode += 7
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 97
            ASCIIcode = chr(ASCIIcode)
            result.append(ASCIIcode)
        else:
            result.append(a)
    strRes = "".join(result)
    return strRes

def CaeDec(text):
    results = []
    tempResult = []
    for a in text:
        ASCIIcode = ord(a)
        if ASCIIcode >= 65 and ASCIIcode <= 90:
            ASCIIcode -= 65
            ASCIIcode -= 7
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 65
            ASCIIcode = chr(ASCIIcode)
            tempResult.append(ASCIIcode)
        elif ASCIIcode >= 97 and ASCIIcode <= 122:
            ASCIIcode -= 97
            ASCIIcode -= 7
            ASCIIcode = ASCIIcode % 26
            ASCIIcode += 97
            ASCIIcode = chr(ASCIIcode)
            tempResult.append(ASCIIcode)
        else:
            tempResult.append(a)
    decrypted_string = "".join(tempResult)
    results.append(decrypted_string)
    return results

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

def RaiEnc(text):
    rails = 5
    fences = ["" for _ in range(rails)]
    step = 1
    current_rail = 0
    
    for char in text:
        fences[current_rail] += char
        current_rail += step
        if current_rail == 0 or current_rail == rails - 1:
            step = -step
    
    return "".join(fences)

def RaiDec(ciphertext):
    rails = 5
    grid = [[None] * len(ciphertext) for _ in range(rails)]
    row = 0
    direction = 1

    for col in range(len(ciphertext)):
        grid[row][col] = '*'
        row += direction
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if grid[r][c] == '*' and index < len(ciphertext):
                grid[r][c] = ciphertext[index]
                index += 1
    result = []
    row = 0
    direction = 1

    for col in range(len(ciphertext)):
        result.append(grid[row][col])
        row += direction
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

    return "".join(result)

def Rot13(text):
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

def Base64Dec(text):
    text += "=" * ((4 - len(text) % 4) % 4)
    encoded = text.encode('utf-8')
    decoded = base64.b64decode(encoded)
    result = decoded.decode('utf-8')
    return result

def Base64Enc(text):
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded