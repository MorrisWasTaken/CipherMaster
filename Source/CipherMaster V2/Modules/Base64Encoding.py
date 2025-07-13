def Base64Dec(text):
    text += "=" * ((4 - len(text) % 4) % 4)
    encoded = text.encode('utf-8')
    decoded = base64.b64decode(encoded)
    result = decoded.decode('utf-8')
    return result

def Base64Enc(text):
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded