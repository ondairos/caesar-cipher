from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = "" #create empty string
  for letter in plain_text: #pass through all letters in first argument
    position = alphabet.index(letter) #find the index of the letter
    new_position = position + shift_amount #calculate the new position
    new_letter = alphabet[new_position] #create the new encrypted letter
    cipher_text += new_letter #create the encrypted word
    cipher_text_solved = cipher_text
  print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
  decrypt_text =""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    new_letter = alphabet[new_position]
    decrypt_text += alphabet[new_position]
  print(f"Your decrypted word is: {decrypt_text}")

#encrypt function and pass in the user inputs.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction =="decode":
  decrypt(cipher_text=text,shift_amount=shift)
