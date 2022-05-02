import jwt, config 
import time
from typing import Dict

settings = config.get_settings()

JWT_SECRET = settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = 1800

def token_response(token:str):
    return {"session_token":token}

def signJWT(user_id:str) -> Dict[str,str]:
    payload = {
        "user_id":user_id,
        "expires":time.time() + ACCESS_TOKEN_EXPIRE_MINUTES
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms = [JWT_ALGORITHM])
        return decode_token
    except:
        return None