from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

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

SECRET_KEY = "my-super-secret-key"
ALGORITHM="HS256"

def create_access_token(username:str,role:str):
    payload={
        "sub":username,
        "role":role,
        "exp":datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm = ALGORITHM
    )

token = create_access_token("darshan","user")
print("JWT:")
print(token)

decoded = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=[ALGORITHM]
)

print("Decoded JWT: ")
print(decoded)

def verify_access(token:str):
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )