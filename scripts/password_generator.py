import random
import string

def generate_password(length=16):
    """Generate a secure random password"""
    characters=string.ascii_letters+string.digits+string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__" :
    password= generate_password()
    print(f"🔒 Secure Password: {password}")
