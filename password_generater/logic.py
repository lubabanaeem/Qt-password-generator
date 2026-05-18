import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_special):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return None

    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    return password


def get_strength(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in string.punctuation:
            has_special = True

    score = 0
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if length < 8 or score <= 1:
        return "Weak", "#e74c3c"
    elif length < 12 or score == 2:
        return "Medium", "#f39c12"
    elif length < 16 or score == 3:
        return "Strong", "#2ecc71"
    else:
        return "Very Strong", "#27ae60"