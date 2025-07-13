# ------------------------------------------------------------------------[ MODULES	 ]------------------------------------------------------------------------ #
from Modules.CaesarCipher import CaesarEnc, CaesarDec
from Modules.Rot13Cipher import Rot13
from Modules.Base64Encoding import Base64Enc, Base64Dec
import base64
import pyperclip

# ------------------------------------------------------------------------[ VARIABLES ]------------------------------------------------------------------------ #

PROMPT = "\033[96m"      # Cyan
SUCCESS = "\033[92m"     # Green
ERROR = "\033[91m"       # Red
INFO = "\033[95m"        # Magenta
SEPARATOR = "\033[90m"   # Dark gray / dim white
RESET = "\033[0m" # Plain White
# ------------------------------------------------------------------------[ FUNCTIONS ]------------------------------------------------------------------------ #

def print_colored_results(results):
    colors = [SUCCESS, ERROR]
    for i in range(0, len(results), 5):
        row = results[i:i+5]
        line_parts = []
        for idx, item in enumerate(row):
            color = colors[idx % 2]
            line_parts.append(f"{color}{item}{RESET}")
        separator = f"{SEPARATOR}|{RESET}"
        print(separator.join(line_parts))



def cmds():
        print(f"{SEPARATOR}-" * 40)
        print(f"""
{INFO}Command Name {SEPARATOR}|{INFO} Command Use
{SEPARATOR}_____________{SEPARATOR}|____________________________________________________
{INFO}cmds         {SEPARATOR}|{INFO} Displays all Commands
{INFO}exit         {SEPARATOR}|{INFO} Exits the Application
{INFO}encrypt      {SEPARATOR}|{INFO} Encrypts a message with the chosen cipher
{INFO}decrypt      {SEPARATOR}|{INFO} Decrypts a message with any supported cipher
{RESET}""")

def Base64Dec(text):
    text += "=" * ((4 - len(text) % 4) % 4)
    encoded = text.encode('utf-8')
    decoded = base64.b64decode(encoded)
    result = decoded.decode('utf-8')
    return result

def Base64Enc(text):
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded

def MorseDec(text):
    result = []
    REVERSED_MORSE_CODE_DICT = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',
    '.': 'E',     '..-.': 'F',  '--.': 'G',   '....': 'H',
    '..': 'I',    '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',   '.--.': 'P',
    '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',
    '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z',

    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',

    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    '-....-': '-', '-..-.': '/',  '-.--.': '(',  '-.--.-': ')',
    '.-...': '&',  '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+',  '..--.-': '_', '.-..-.': '"', '...-..-': '$',
    '.--.-.': '@', '.----.': "'"
}
    parts = text.split(" ")
    for a in parts:
        if a == "/":
            result.append(" ")
        if a in REVERSED_MORSE_CODE_DICT:
            result.append(REVERSED_MORSE_CODE_DICT[a])
    strRes = "".join(result)
    return strRes

def MorseEnc(text):
    result = []
    MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '-': '-....-', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', "'": '.----.'
}
    text = text.upper()
    
    for a in text:
        if a in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[a])
        if a == " ":
            result.append("/")
    strRes = " ".join(result)
    return strRes

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

def CaesarEnc(text, shift):
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

def CaesarDec(text):
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

def CaebashEnc(Ctext, Cshift):
    CaeEnctext = CaesarEnc(Ctext, Cshift)
    Enctext = Atbash(CaeEnctext)
    return Enctext

def CaebashDec(Ctext):
    Enctext = Atbash(Ctext)
    Dectext = CaesarDec(Enctext)
    return Dectext

def RailFenceEnc(text, rails):
    fences = ["" for _ in range(rails)]
    step = 1
    current_rail = 0
    
    for char in text:
        fences[current_rail] += char
        current_rail += step
        if current_rail == 0 or current_rail == rails - 1:
            step = -step
    
    return "".join(fences)

def RailFenceDec(ciphertext, rails):
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

def CM_SecureEnc(text):
    cabaText = CaebashEnc(text, 7)
    raiText = RailFenceEnc(cabaText, 5)
    rotText = Rot13(raiText)
    result = Base64Enc(rotText)
    return result

def CM_SecureDec(text):
    baseText = Base64Dec(text)
    rotText = Rot13(baseText)
    raiText = RailFenceDec(rotText, 5)
    result = CaebashDec(raiText)
    return result

def TryAll(text):
    print(f"""{INFO}
Due to the nature of a Rail Fence cipher you need to know how many rails where used, if not input a number at random and skip this section...
{PROMPT}How many rails would you like to use?{RESET}
""")
    UsrRails = input(">>> ")
    print(f"{SUCCESS}Decrypted text with Rail Fence Cipher, Shifted by {UsrRails} Rails. Result: {RailFenceDec(text, int(UsrRails))}{RESET}")
    results = CaesarDec(text)
    print(f"{SUCCESS}Decrypted text with Caesar Cipher, Results:")
    print_colored_results(results)
    try:
        results = CM_SecureDec(text)
        print(f"{SUCCESS}Decrypted text with CM_Secure Cipher, Results:")
        print_colored_results(results)
    except Exception as e:
        print(f"{ERROR}CM_Secure Decryption failed: {e}{RESET}")
    results = CaebashDec(text)
    print(f"{SUCCESS}Decrypted text with a Caebash Cipher, Results:")
    print_colored_results(results)
    try:
        print(f"{SUCCESS}Decrypted text with Base64 Encoding, Result: {Base64Dec(text)}{RESET}")
    except Exception as e:
        print(f"{ERROR}Base64 Decryption failed: {e}{RESET}")
    print(f"{SUCCESS}Decrypted Morse Code, Result: {MorseDec(text)}{RESET}")
    print(f"{SUCCESS}Decrypted text with an Atbash Cipher, Result: {Atbash(text)}{RESET}")
    print(f"{SUCCESS}Decrypted text with a ROT13 Cipher, Shifted by 13 Positions, Result: {Rot13(text)}{RESET}")
          

# ------------------------------------------------------------------------[ CODE ]------------------------------------------------------------------------ #

print(f"""{INFO}
Welcome to CipherMaster V2!
Use the "exit" Command to Quit the application and the "cmds" Command to view all Existing Commands
Your inputs are non Case-Sensitive{RESET}
""")
while True:
    command = input(">>> ").lower()
    if command == "exit":
        break
    elif command == "cmds":
        cmds()
    elif command == "encrypt":
        print(f"{PROMPT}Input Text to Encrypt{RESET}")
        UsrInput = input(">>> ")
        print(f"""{PROMPT}
What kind of Cipher would you like to Encrypt?
{INFO}
Cipher Name   | Input  | How Does it work?
______________|________|____________________________________________________________________________________________
Caesar        | cae    | Shifts each letter by a number of positions in the alphabet.
ROT13         | rot    | Caesar cipher with a fixed shift of 13 Positions.
Atbash        | atb    | Replaces each letter with its reverse in the alphabet (A ↔ Z)
--------------|--------|-------------------------------
Rail Fence    | rai    | Writes the message in a zig-zag pattern and reads it line by line.
--------------|--------|-------------------------------
Morse         | mor    | Encodes letters as sequences of dots and dashes.
Base64        | bas    | Converts binary data into a set of 64 printable characters.
--------------|--------|-------------------------------
Caebash       | caba   | A mix of a Caesar cipher and a Atbash Cipher
CM Secure     | sec    | A secure cipher that can only be decoded in this application.
{RESET}""")
        command = input(">>> ").lower()
        if command == "cae":
            print(f"""{INFO}
A Caesar cipher shifts each letter in the text by a fixed number of positions down the alphabet, wrapping around at the end.
{PROMPT}By how many positions would you like to shift?{RESET}
""")
            UsrShift = input(">>> ")
            print(f"{SUCCESS}Encrypted text, Shifted by {UsrShift} Positions, Result: {CaesarEnc(UsrInput, int(UsrShift))}{RESET}")
            pyperclip.copy(CaesarEnc(UsrInput, int(UsrShift)))
        elif command == "rot":
            print(f"""{INFO}
A ROT13 cipher shifts each letter in the text by 13 positions down the alphabet, wrapping around at the end.
""")
            print(f"{SUCCESS}Encrypted text, Shifted by 13 Positions, Result: {Rot13(UsrInput)}. The Result has been copied to your Clipboard!{RESET}")
            pyperclip.copy(Rot13(UsrInput))
        elif command == "atb":
            print(f"""{INFO}
An Atbash cipher replaces each letter with its opposite in the alphabet (A ↔ Z, B ↔ Y, etc.).
""")
            print(f"{SUCCESS}Encrypted text, Result: {Atbash(UsrInput)}{RESET}")
            pyperclip.copy(Atbash(UsrInput))
        elif command == "mor":
            print(f"""{INFO}
A Morse code cipher encodes letters and numbers as sequences of dots and dashes separated by spaces.
""")
            print(f"{SUCCESS}Encrypted text, Result: {MorseEnc(UsrInput)}{RESET}")
            pyperclip.copy(MorseEnc(UsrInput))
        elif command == "bas":
            print(f"""{INFO}
Base64 encoding converts binary data into a text format using 64 characters, making it safe for transmission over text-based systems.
""")
            print(f"{SUCCESS}Encrypted text, Result: {Base64Enc(UsrInput)}{RESET}")
            pyperclip.copy(Base64Enc(UsrInput))
        elif command == "caba":
            print(f"""{INFO}
A Caebash Cipher runs the text through a Caesar Cipher and then through a Atbash Cipher
{PROMPT}By how many positions would you like to shift?{RESET}
""")
            UsrShift = input(">>> ")
            print(f"{SUCCESS}Encrypted text, Shifted by {UsrShift} Positions, Result: {CaebashEnc(UsrInput, int(UsrShift))}{RESET}")
            pyperclip.copy(CaebashEnc(UsrInput, int(UsrShift)))
        elif command == "rai":
            print(f"""{INFO}
A Rail Fence Cipher writes the message in a zig-zag pattern across a number of rails and then reads it off row by row
{PROMPT}How many rails would you like to use?{RESET}
""")
            UsrRails = input(">>> ")
            print(f"{SUCCESS}Encrypted text, Shifted by {UsrRails} Rails. Result: {RailFenceEnc(UsrInput, int(UsrRails))}{RESET}")
            pyperclip.copy(RailFenceEnc(UsrInput, int(UsrRails)))
        elif command == "sec":
            print(f"{SUCCESS}Encrypted text. Result: {CM_SecureEnc(UsrInput)}{RESET}")
            pyperclip.copy(CM_SecureEnc(UsrInput))
        else:
            print(f'"{command}" {ERROR}is not a known command, reseting prompt...{RESET}')
    elif command == "decrypt":
        print(f"{PROMPT}Input Text to Decrypt{RESET}")
        UsrInput = input(">>> ")
        print(f"""{PROMPT}
What kind of Cipher would you like to Decrypt?
{INFO}
Cipher Name   | Input  | How Does it work?
______________|________|____________________________________________________________________________________________
Caesar        | cae    | Shifts each letter by a number of positions in the alphabet.
ROT13         | rot    | Caesar cipher with a fixed shift of 13 Positions.
Atbash        | atb    | Replaces each letter with its reverse in the alphabet (A ↔ Z)
--------------|--------|--------------------------------------------------------------------------------------------
Rail Fence    | rai    | Writes the message in a zig-zag pattern and reads it line by line.
--------------|--------|--------------------------------------------------------------------------------------------
Morse         | mor    | Encodes letters as sequences of dots and dashes.
Base64        | bas    | Converts binary data into a set of 64 printable characters.
--------------|--------|--------------------------------------------------------------------------------------------
Caebash       | caba   | A mix of Caesar cipher and Bash-style text formatting
CM Secure     | sec    | A secure cipher that can only be decoded in this application.
--------------|--------|--------------------------------------------------------------------------------------------
Try all       | all    | Runs the text through every cipher and generates a huge table with all the results.

{RESET}""")
        command = input(">>> ").lower()
        if command == "cae":
            print(f"""{INFO}
A Caesar cipher shifts each letter in the text by a fixed number of positions down the alphabet, wrapping around at the end.
{PROMPT}When Decrypting this Application lists every possible combination in a Table{RESET}
""")

            results = CaesarDec(UsrInput)
            print(f"{SUCCESS}Decrypted text, Results:")
            print_colored_results(results)

        elif command == "rot":
            print(f"""{INFO}
A ROT13 cipher shifts each letter in the text by 13 positions down the alphabet, wrapping around at the end.
""")
            print(f"{SUCCESS}Decrypted text, Shifted by 13 Positions, Result: {Rot13(UsrInput)}{RESET}")
        elif command == "atb":
            print(f"""{INFO}
An Atbash cipher replaces each letter with its opposite in the alphabet (A ↔ Z, B ↔ Y, etc.).
""")
            print(f"{SUCCESS}Decrypted text, Result: {Atbash(UsrInput)}{RESET}")
        elif command == "mor":
            print(f"""{INFO}
A Morse code cipher encodes letters and numbers as sequences of dots and dashes separated by spaces.
""")
            print(f"{SUCCESS}Decrypted text, Result: {MorseDec(UsrInput)}{RESET}")
        elif command == "bas":
            print(f"""{INFO}
Base64 encoding converts binary data into a text format using 64 characters, making it safe for transmission over text-based systems.
""")
            print(f"{SUCCESS}Decrypted text, Result: {Base64Dec(UsrInput)}{RESET}")
        elif command == "caba":
            print(f"""{INFO}
A Caebash Cipher runs the text through a Caesar Cipher and then through a Atbash Cipher
""")
            results = CaebashDec(UsrInput)
            print(f"{SUCCESS}Decrypted text, Results:")
            print_colored_results(results)
        elif command == "rai":
            print(f"""{INFO}
A Rail Fence Cipher writes the message in a zig-zag pattern across a number of rails and then reads it off row by row
{PROMPT}How many rails would you like to use?{RESET}
""")
            UsrRails = input(">>> ")
            print(f"{SUCCESS}Decrypted text, Shifted by {UsrRails} Rails. Result: {RailFenceDec(UsrInput, int(UsrRails))}{RESET}")
        elif command == "sec":
            results = CM_SecureDec(UsrInput)
            print(f"{SUCCESS}Decrypted text, Results:")
            print_colored_results(results)
        elif command == "all":
            TryAll(UsrInput)
        else:
            print(f'"{command}" {ERROR}is not a known command, reseting prompt...{RESET}')
else:
        print(f'"{command}" {ERROR}is not a known command, use "cmds" to list all commands{RESET}')