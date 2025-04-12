from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def unpad(data):
    return data.rstrip(b' ')

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode()))
    iv = cipher.iv
    encrypted = iv + ct_bytes
    return base64.b64encode(encrypted).decode()

def aes_decrypt(encrypted_data_b64, key):
    encrypted_data = base64.b64decode(encrypted_data_b64)
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(encrypted_data[16:])
    return unpad(pt).decode()

def main():
    key = get_random_bytes(16)  

    print("AES Encryption & Decryption Tool\n")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    choice = input("\nChoose option (1 or 2): ")

    if choice == "1":
        message = input("\nEnter message to encrypt: ")
        encrypted = aes_encrypt(message, key)
        print("\nEncrypted message (Base64):", encrypted)
        print("Save this key to decrypt later (Base64):", base64.b64encode(key).decode())

    elif choice == "2":
        encrypted_message = input("\nEnter Base64 encrypted message: ")
        key_b64 = input("Enter Base64 AES key: ")
        key = base64.b64decode(key_b64)
        try:
            decrypted = aes_decrypt(encrypted_message, key)
            print("\nDecrypted message:", decrypted)
        except Exception as e:
            print("\n❌ Decryption failed. Error:", e)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
