# -*- coding: utf-8 -*-

# Python 3
# Bitcoin address validator

from hashlib import sha256

# Base58 alphabet
base58char = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'




# Base58 decoder function

def base58decode(str):
    # Cut the 1
    originalLen = len(str)
    str = str.lstrip(base58char[0])
    newLen = len(str)

    # Convert string to digit
    digit = 0
    for char in str:
        digit = digit * 58 + base58char.index(char)

    # Convert digit to bytes
    result = []
    while digit > 0:
        digit, modul = divmod(digit, 256)
        result.append(modul)

    return (b'\0' * (originalLen - newLen) + bytes(reversed(result)))




# Bitcoin address validator function

def bitcoinValidator(str):

    # convert string to bytes and handle non base58 input
    try:
        base58byteStr = base58decode(str)
    except:
        return False


    # separete hash part
    first_21_bytes = base58byteStr[:21]
    last_4_bytes = base58byteStr[21:]

    # double sha256 digest
    stringHash = sha256(first_21_bytes).digest()
    stringHash = sha256(stringHash).digest()

    # compare hashes
    if last_4_bytes == stringHash[:4]:
        return True
    else:
        return False



# Main

print("""Here some valid bitcoin addresses that you can copy and test:
1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i
1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX
3QzYvaRFY6bakFBW4YBRrzmwzTnfZcaA6E
""")

addr = input("Paste bitcoin address: ")

if bitcoinValidator(addr):
    print("Valid")
else:
    print("Invalid")

input("\nPress Enter to exit")

