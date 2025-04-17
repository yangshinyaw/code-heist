def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            encrypted += shifted
        else:
            encrypted += char
    return encrypted

def run_level():
    print("🔎 Challenge: Decrypt the message below.")
    secret = "xli uymgo sj xli csyvw gsqtsvx"
    print(f"\n📄 Encrypted Message: {secret}")
    print("Hint: Caesar Cipher. Try shifting letters to reveal the message.")

    answer = input("🔓 Enter the decrypted message: ").strip().lower()
    correct = "the quick of the yours comport"  # Actually wrong to mislead, adjust as needed

    if "quick" in answer and "fox" in answer:
        return True
    return False
