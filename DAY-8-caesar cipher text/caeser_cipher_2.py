alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type encode to encrpyt and decode to decrpyt:")
text = input("Enter your message:").lower()
shift = int(input("Type the shift number:"))


def encrpyt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    print(f"Encoded text is {cipher_text}") 
encrpyt(plain_text=text , shift_amount=shift)       

def decrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position - shift_amount
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    print(f"Decoded text  is {cipher_text}") 
decrypt(plain_text=text , shift_amount=shift)    

if direction == "encode":
    encrpyt(text, shift)
elif direction == "decode":
    decrypt(text,shift) 
