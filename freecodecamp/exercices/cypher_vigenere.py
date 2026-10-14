text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    """
    Core Vigenère cipher function.
    direction=1  → encryption (shift forward)
    direction=-1 → decryption (shift backward)
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # reference alphabet for index lookups
    final_message = ''

    for char in message.lower():  # process each character in lowercase

        # Non-letter characters (spaces, punctuation) are kept as-is
        if not char.isalpha():
            final_message += char
        else:
            # Cycle through the key using modulo to avoid index out of range
            # e.g. key='happy', key_index=6 → 6 % 5 = 1 → key[1] = 'a'
            key_char = key[key_index % len(key)]
            key_index += 1

            # Get the shift value from the key character's position in the alphabet
            # e.g. 'h' → index 7 → shift by 7
            offset = alphabet.index(key_char)

            # Get the position of the current character in the alphabet
            index = alphabet.find(char)

            # Apply the shift (forward for encryption, backward for decryption)
            # Modulo 26 ensures we wrap around the alphabet (z + 1 = a)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    """Encrypts a message using the Vigenère cipher."""
    return vigenere(message, key)  # direction=1 by default
    
def decrypt(message, key):
    """Decrypts a message using the Vigenère cipher."""
    return vigenere(message, key, -1)  # direction=-1 reverses the shift

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')