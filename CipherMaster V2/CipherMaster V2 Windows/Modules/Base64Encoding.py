import base64

name = "Base64"
info = "Converts text into a safe ASCII format, often used in data transfer."
command = "bas"

def decrypt(text):
    text += "=" * ((4 - len(text) % 4) % 4)
    encoded = text.encode('utf-8')
    decoded = base64.b64decode(encoded)
    result = decoded.decode('utf-8')
    return result

def encrypt(text):
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded