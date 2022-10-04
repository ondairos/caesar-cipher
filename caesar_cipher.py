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
  print(f"The encoded text is {cipher_text}")

#encrypt function and pass in the user inputs.
encrypt(plain_text=text, shift_amount=shift)