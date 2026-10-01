from pwdlib import PasswordHash

passwordHash=PasswordHash.recommended()
dummy_password="dummy123"
hashedPassword=passwordHash.hash(dummy_password)
print("original",dummy_password)
print("hashed",hashedPassword)
verifyHashedPassword=passwordHash.verify(dummy_password, hashedPassword)
print(verifyHashedPassword)