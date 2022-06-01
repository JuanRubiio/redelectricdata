from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT
import time

class JWT_STATUS():
    JWT_VALID = True
    JWT_INVALID = False
    JWT_EXPIRED = -1
    JWT_NOTAUSER = -2
    JWT_ERROR1 = -3
    
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
        elif not credentials.scheme == "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authorization scheme")
        else:
            jwt_verification = self.verify_jwt(credentials.credentials)
            if jwt_verification == JWT_STATUS.JWT_VALID:
                return credentials.credentials
            elif jwt_verification == JWT_STATUS.JWT_INVALID:
                HTTPException(status_code=401, detail="Invalid token")
            elif jwt_verification == JWT_STATUS.JWT_EXPIRED:
                HTTPException(status_code=401, detail="Expired token")
            elif jwt_verification == JWT_STATUS.JWT_NOTAUSER:
                HTTPException(status_code=401, detail="Invalid user")
            
    def check_user_db(self, user_id):
        return True
    
    def verify_jwt(self, jwtoken:str) -> bool:
        try: payload = decodeJWT(jwtoken)
        except:payload=None
        
        if not payload: return JWT_STATUS.JWT_INVALID
        elif payload["expires"]<time.time():return JWT_STATUS.JWT_EXPIRED
        elif not self.check_user_db(payload["user_id"]): return JWT_STATUS.JWT_NOTAUSER
        else: return JWT_STATUS.JWT_VALID
        