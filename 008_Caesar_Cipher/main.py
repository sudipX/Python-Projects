from resources import logo
from resources import alphabets
import os



# Encryption
# def encrypt(message_to_encrypt, shift_number):
#     encrypted_message = ""
#     for letters in message_to_encrypt:
#         original_index_of_letters = alphabets.index(letters) # Getting index number of the letters in original message
#         final_index_of_letters = original_index_of_letters + shift_number # adding original index postion with shift postiton
#         encrypted_letter = alphabets[final_index_of_letters] # getting encrypted letter from the alphabet list using final index position
#         encrypted_message += encrypted_letter # adding the encrypted letter into the string to output whole message
#     print(f"Encoded Message : {encrypted_message}")

# # Decryption
# def decrypt(message_to_decrypt, shift_number):
#     decrypted_message = ""
#     for letters in message_to_decrypt:
#         original_index_of_letters = alphabets.index(letters) # Getting index number of the letters in encrypted message
#         final_index_of_letters = original_index_of_letters - shift_number # subtracting original index postion with shift postiton
#         decrypted_letter = alphabets[final_index_of_letters] # getting decrypted letter from the alphabet list using final index position
#         decrypted_message += decrypted_letter # adding the decrypted letter into the string to output whole message
#     print(f"Decoded Message: {decrypted_message}")


def caesar():
    print(logo)
    direction_of_cipher = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message_input = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))
    program_end = False
    while not program_end:
        output_message = ""
        for letters in message_input:
            original_index_of_letters = alphabets.index(letters)
            if direction_of_cipher == "encode":
                final_index_of_letters = original_index_of_letters + shift_number
            elif direction_of_cipher == "decode":
                final_index_of_letters = original_index_of_letters - shift_number
            output_letter = alphabets[final_index_of_letters]
            output_message += output_letter
        print(f"{direction_of_cipher}d message: {output_message}")
        print("---------------------------------------------------")
        end_the_program = input("End the program (Y/N) :\n>> ").lower()
        if end_the_program == "y":
            program_end = True
        elif end_the_program == "n":
            os.system("cls")
            caesar()

caesar()


