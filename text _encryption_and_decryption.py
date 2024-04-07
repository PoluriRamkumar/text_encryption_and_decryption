
class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        encrypted_text = ''
        for i in range(self.key):
            for j in range(i, len(plaintext), self.key):
                encrypted_text += plaintext[j]
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = [''] * len(ciphertext)
        num_rows = -(-len(ciphertext) // self.key) 
        # Ceiling division to calculate the number of rows
        num_cols = self.key

        # Fill the decrypted text matrix column by column
        for col in range(num_cols):
            for row in range(num_rows):
                index = col + row * num_cols
                if index < len(ciphertext):
                    decrypted_text[index] = ciphertext[col * num_rows + row]

        return ''.join(decrypted_text).rstrip()

# Get input from the user
key = int(input("Enter the key for encryption and decryption: "))
plaintext = input("Enter the plaintext message: ")

# Create an instance of TranspositionCipher with the user-provided key
cipher = TranspositionCipher(key)

# Encrypt the plaintext message
encrypted_text = cipher.encrypt(plaintext)

# Decrypt the encrypted text
decrypted_text = cipher.decrypt(encrypted_text)

# Print the encrypted and decrypted texts
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)