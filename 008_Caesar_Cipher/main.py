from resources import logo
from resources import alphabets

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encryption
def encrypt(message_to_encrypt, shift_number):
    encrypted_message = ""
    for letters in message_to_encrypt:
        original_index_of_letters = alphabets.index(letters) # Getting index number of the letters in original message
        final_index_of_letters = original_index_of_letters + shift_number # adding original index postion with shift postiton
        encrypted_letter = alphabets[final_index_of_letters] # getting encrypted letter from the alphabet list using final index position
        encrypted_message += encrypted_letter # adding the encrypted letter into the string to output whole message
    print(encrypted_message)

# Decryption
def decrypt(message_to_decrypt, shift_number):
    decrypted_message = ""
    for letters in message_to_decrypt:
        original_index_of_letters = alphabets.index(letters) # Getting index number of the letters in encrypted message
        final_index_of_letters = original_index_of_letters - shift_number # subtracting original index postion with shift postiton
        decrypted_letter = alphabets[final_index_of_letters] # getting decrypted letter from the alphabet list using final index position
        decrypted_message += decrypted_letter # adding the decrypted letter into the string to output whole message
    print(decrypted_message)







# encrypt(message_to_encrypt=text, shift_number=shift)
decrypt(message_to_decrypt=text, shift_number=shift)
