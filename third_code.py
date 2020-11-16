alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(start_text, shift_amount, cipher_direction):
  if direction == "encode":
    cipher_text = ""
    for letter in start_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The word '{text}' would be encoded to '{cipher_text}'")
  elif direction == "decode":
    plain_text = ""
    for letter in start_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      plain_text += alphabet[new_position]
    print(f"The word '{text}' would translate to '{plain_text}'")

caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
