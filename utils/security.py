from pwdlib import PasswordHash

password_hash=PasswordHash.recommended()

def hash_password(password:str):
    return password_hash.hash(password)

def verify_password(password:str,hashed_password:str):
    return password_hash.verify(password,hashed_password)

password = "123456"

hashed = hash_password(password)

print("Original:", password)
print("Hashed:", hashed)
print("Correct:", verify_password("123456", hashed))
print("Wrong:", verify_password("wrong", hashed))


