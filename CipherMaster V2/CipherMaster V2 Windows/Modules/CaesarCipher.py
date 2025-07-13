PROMPT = "\033[96m"      # Cyan
SUCCESS = "\033[92m"     # Green
ERROR = "\033[91m"       # Red
INFO = "\033[95m"        # Magenta
SEPARATOR = "\033[90m"   # Dark gray / dim white
RESET = "\033[0m" # Plain White
name = "Caesar"
info = "Shifts Each Letter back into the alphabet by a custom amount of positions"
command = "cae"

def encrypt(text):
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

def decrypt(text):
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
    colors = [SUCCESS, ERROR]
    for i in range(0, len(results), 5):
        row = results[i:i+5]
        line_parts = []
        for idx, item in enumerate(row):
            color = colors[idx % 2]
            line_parts.append(f"{color}{item}{RESET}")
        separator = f"{SEPARATOR}|{RESET}"
        print(separator.join(line_parts))
    fakeres = " "
    return fakeres
