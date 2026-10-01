import jwt
from datetime import datetime, timezone, timedelta
SECRET_KEY = "my-secret-key"
now =datetime.now(timezone.utc)
expire=now+ timedelta(minutes=30)

payload = {
    "user_id": 1,
    "iat":now,
    "exp":expire
}

token=jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)


def verify_token(token: str):
    try:
        decoded = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return True

    except jwt.InvalidTokenError:
        return False
print(verify_token(token))