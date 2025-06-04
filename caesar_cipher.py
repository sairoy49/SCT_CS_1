def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char 
    return result


def main():
    print("=== Caesar Cipher Tool ===")
    
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
    
    message = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
            break
        except ValueError:
            print("Please enter a valid integer shift value.")
    
    result = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed message): {result}")


if __name__ == "__main__":
    main()
