from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from providers import check_hash

class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool  = True) -> None:
        super(JwtBearer, self).__init__(auto_error = auto_error)
        
    async def __call__(self, request: Request):
        credentials:  HTTPAuthorizationCredentials = await super(JwtBearer, 
                                                                 self).__call__(request)
        
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, details="Token inválido ou expirado.")
            
            return credentials.credentials
        
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, details="Token inválido ou expirado.")
        
    def verify_jwt(self, jwtoken: str):
        isTokenValid: bool = False
        payload = check_hash(jwtoken)
        if payload:
            isTokenValid = True