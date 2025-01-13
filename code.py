import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if _name_ == "_main_":
    password = generate_password()
    print("Generated Password:", password)
