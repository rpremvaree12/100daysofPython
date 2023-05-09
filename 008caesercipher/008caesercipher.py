import art

print(art.logo)

alphabet = "abcdefghijklmnopqrstuvwxyz"
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    cipher_text = ""
    for c in text:
            cipher_text += alphabet[(alphabet.index(c)+shift)%26]
    return cipher_text

def decrypt(text, shift):
     return encrypt(text,-1*shift)


if direction == "encode":
    print(encrypt(text, shift))
elif direction == "decode":
     print(decrypt(text,shift))