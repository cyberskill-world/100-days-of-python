import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from art import logo

alphabet = list("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ ")

def substitution(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_positon = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_positon]
        else:
            end_text+=char
    print(f"Here's the {cipher_direction}d result: {end_text}")

run = True
while run:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message:")
    shift = int(input("Type the shift number:"))
    
    shift = shift % len(alphabet)

    substitution(start_text=text, shift_amount=shift, cipher_direction=direction)
    choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
    if choice == 'no':
        run = False
        print("Goodbye.")
