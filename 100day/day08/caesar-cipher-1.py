alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number \n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        encrypt_letter = alphabet[new_position]
        cipher_text += encrypt_letter
    return cipher_text

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position <= 0:
            new_position += len(alphabet)
        decrypt_letter = alphabet[new_position]
        plain_text += decrypt_letter
    return plain_text

# if direction == 'encode':
#     print("Encrypted text : "+ encrypt(text, shift))
# elif direction == 'decode':
#     print("Decrypted text : "+ decrypt(text, shift))
    
def caesar(direction, text, shift_amount):
    result_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == 'encode':
            new_position = position + shift_amount
            if new_position >= len(alphabet):
                new_position -= len(alphabet)
        elif direction == 'decode':
            new_position = position - shift_amount
            if new_position <= 0:
                new_position += len(alphabet)
        switch_letter = alphabet[new_position]
        result_text += switch_letter
    return result_text

def caesar_enhance(direction, text, shift_amount):
    result_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        elif new_position <= 0:
            new_position += len(alphabet)
        switch_letter = alphabet[new_position]
        result_text += switch_letter
    return result_text

    

print(f"The {direction}d text is "+ caesar_enhance(direction, text, shift))