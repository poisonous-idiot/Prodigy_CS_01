def main():
    shift = int(input("Enter the shift you want to implement (must be between 1 and 26): "))

    # Write plain text to file
    plain_text = input("Enter text to encrypt: ")
    with open("Plain_text.txt", "w") as plain_file:
        plain_file.write(plain_text)

    # Encrypt plain text
    with open("Plain_text.txt", "r") as plain_file:
        plain_text = plain_file.read()
        with open("Cipher_text.txt", "w") as cipher_file:
            for char in plain_text:
                if char.isalpha():
                    ascii_offset = 97 if char.islower() else 65
                    encrypted = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    encrypted = char
                cipher_file.write(encrypted)

    # Decrypt cipher text
    with open("Cipher_text.txt", "r") as cipher_file:
        cipher_text = cipher_file.read()
        with open("Decrypted_text.txt", "w") as decrypted_file:
            for char in cipher_text:
                if char.isalpha():
                    ascii_offset = 97 if char.islower() else 65
                    decrypted = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                else:
                    decrypted = char
                decrypted_file.write(decrypted)

    # Display cipher text and decrypted text to user
    with open("Cipher_text.txt", "r") as cipher_file:
        cipher_text = cipher_file.read()
        print("\nCipher Text:")
        print(cipher_text)

    with open("Decrypted_text.txt", "r") as decrypted_file:
        decrypted_text = decrypted_file.read()
        print("\nDecrypted Text:")
        print(decrypted_text)

if __name__ == "__main__":
    main()