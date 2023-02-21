"""
Implement classical ciphers using python.
"""


def encrypt(plaintext, key):
    cifertext = ""
    for i in plaintext:
        if i == " ":
            cifertext += " "
        else:
            cifertext += chr(((ord(i) + key) - 65) % 26 + 65)if i.isupper(i) else chr(((ord(i) + key) - 65) % 26 + 65)
    return cifertext


plaintext = input("Enter a plaintext : ")
key = int(input("Enter a plaintext : "))

print("Encrypted text :", encrypt(plaintext, key))
