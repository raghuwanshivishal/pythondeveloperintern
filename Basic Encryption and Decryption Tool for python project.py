from cryptography.fernet import Fernet

# Function to generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("New encryption key generated and saved to 'secret.key'")

# Function to load the encryption key from a file
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Key file not found. Generate a new key first.")
        return None

# Function to encrypt a message
def encrypt_message():
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)
    message = input("Enter the message to encrypt: ").encode()
    encrypted_message = fernet.encrypt(message)
    print("Encrypted message:", encrypted_message.decode())

# Function to decrypt a message
def decrypt_message():
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)
    encrypted_message = input("Enter the encrypted message to decrypt: ").encode()
    try:
        decrypted_message = fernet.decrypt(encrypted_message)
        print("Decrypted message:", decrypted_message.decode())
    except Exception as e:
        print("Decryption failed:", e)

# Main program loop
def main():
    while True:
        print("\nBasic Encryption and Decryption Tool")
        print("1. Generate Encryption Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            encrypt_message()
        elif choice == '3':
            decrypt_message()
        elif choice == '4':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the tool
if __name__ == "__main__":
    main()
