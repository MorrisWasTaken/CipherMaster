name = "Morse"
info = "Encodes text into dots and dashes."
command = "mor"

def decrypt(text):
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

def encrypt(text):
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