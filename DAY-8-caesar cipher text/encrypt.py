alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type encode to encrypt and decode to decrypt:")
text = input("Enter the word you want to encode:\n").lower()
shift = int(input("Enter the shift amount you want in your text:"))
def encrypt(text,shift):
    cipher_text = ""
    for letter in text:
        position = alphabets.index(letter)
        new_pos = position + shift
        new_letter = alphabets[new_pos]
        cipher_text += new_letter
    print(f"Encoded text is : {cipher_text}")   
encrypt(text,shift)     

        
    