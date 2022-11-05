from datetime  import datetime, timedelta
from jose import jwt 
from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITMO = os.getenv('ALGORITMO')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')


def create_access_token(data: dict):
    to_encode  = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expiration})
    
    encoded_jwt  = jwt.encode(to_encode, SECRET_KEY, algorithm=[ALGORITMO])   
    return encoded_jwt


def check_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITMO])
    
    return payload.get("sub")