"""
Implement classical ciphers using python.
"""


def encrypt(plaintext, key):
    cifertext = ""
    for i in plaintext:
        if i == " ":
            cifertext += " "
        else:
            cifertext += chr(ord(i) + key)
    return cifertext


plaintext = input("Enter a plaintext : ")
key = int(input("Enter a plaintext : "))

print("Encrypted text :", encrypt(plaintext, key))
