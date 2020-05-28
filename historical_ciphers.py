import math

def caesar(text, mode, s):
    result = ""
    if ( any(map(str.isdigit, text)) ):
        result="0"
    elif (type(s)!=int):
        result = "0"
    else:
        text=text.upper()
        if mode =="d":
            for t in text:
                # s%26 - if input is higher than the alphabet length
                result += chr((ord(t) - (s%26) - 65) % 26 + 65)
        elif mode =="e":
            for t in text:
                result += chr((ord(t) + (s%26) - 65) % 26 + 65)
        else:
            result = "0"

    return result

def vigenere(text,mode,key):
    result = ""
    if (any(map(str.isdigit, text))):
        result = "0"
    elif (any(map(str.isdigit, key))):
        result = "0"
    else:
        text=text.upper()
        key=key.upper()
        key_length = len(key)
        if mode =="d":
            for i in range(len(text)):
                result += chr((ord(text[i]) - ord(key[i%key_length])) % 26 +65)
        elif mode =="e":
            for i in range(len(text)):
                result += chr((ord(text[i]) + ord(key[i%key_length])) % 26 + 65)
        else:
            result ="0"

    return result

