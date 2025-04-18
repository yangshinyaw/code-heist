import random
import string

def generate_caesar_cipher():
    shift = random.randint(1, 25)
    message = random.choice([
        "the quick brown fox",
        "secure the system",
        "follow the protocol",
        "access the vault",
        "decrypt the code"
    ])
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return {
        "type": "Caesar Cipher",
        "original": message,
        "encrypted": encrypted,
        "shift": shift
    }

def generate_reverse_string():
    message = random.choice([
        "firewall breach",
        "code override",
        "terminate trace",
        "decrypt channel",
        "stealth mode"
    ])
    return {
        "type": "Reverse String",
        "original": message,
        "encrypted": message[::-1]
    }

def generate_puzzle():
    puzzle_type = random.choice(["caesar", "reverse"])
    if puzzle_type == "caesar":
        return generate_caesar_cipher()
    elif puzzle_type == "reverse":
        return generate_reverse_string()
