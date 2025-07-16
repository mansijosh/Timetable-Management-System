# app/auth/auth_handler.py
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "Ht-OtaO9ynBbhMRS_oFww4cVIk0w9nGKqBTmpzeFpzg"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
