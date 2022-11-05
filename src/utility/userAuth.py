from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from providers import check_access_token
from fastapi import Depends, HTTPException, status
from jose import JWTError
from validation import UserValidation
from configuration import generate_session


oauth1_schema = OAuth2PasswordBearer(tokenUrl="token")

def get_authenticated_user(session: Session = Depends(generate_session), token: str = Depends(oauth1_schema)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail='Token invalido'
        )
    
    try:    
        token_decode = check_access_token(token)
    except JWTError: 
        raise exception
    
    if not token_decode:
        raise exception
    
    user = UserValidation(session=session).exist_user(token_decode)
    
    if not user:
        raise exception
    
    return user