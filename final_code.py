#lists of words in the alphabet for the encripting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art

#import logo from art.py
print(art.logo)

#Encripting function
def caesar(start_text, shift_amount, cipher_direction):
  if direction == "encode":
    cipher_text = ""
    for letter in start_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
      else:
        cipher_text += letter
    print(f"The word '{text}' would be encoded to '{cipher_text}'")
  elif direction == "decode":
    plain_text = ""
    for letter in start_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
      else:
        plain_text += letter
    print(f"The word '{text}' would translate to '{plain_text}'")

#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
should_continue = True
while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #for shifts that are over 25 (the lenght of the alphabet)
  shift = shift % 25

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  #restart the encripting:
  result = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

  if result == 'yes':
    should_continue = True
  else:
    print('Goodbye!')
    should_continue = False
