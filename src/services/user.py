from repository import UserRepository
from validation import UserValidation
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from schemas import UserSchemaSignUP, UserSchemaLogin
from providers import generate_hash, check_hash, create_access_token


def service_get_user(session: Session) :
    result = UserRepository(session=session).get()
    return result

def service_get_user_id(session: Session, id: int):
    result = UserRepository(session=session).get_id(id=id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário de {id} não foi encontrado.')
    return result

def service_add_user(user: UserSchemaSignUP,  session: Session):
    user_located = UserValidation(session=session).exist_user(user.email)
    
    if user_located:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Já existe um usuário com este email. "
                            )
    
    user.password = generate_hash(user.password)
    result = UserRepository(session=session).create(user)
    return result

def service_update_user(user: UserSchemaSignUP,  session: Session, id: int):
    result = UserRepository(session=session).update(user=user, id=id)
    return result

def service_delete_user(session: Session, id: int):
    return UserRepository(session=session).delete( id=id)
  

def service_login_user(user: UserSchemaLogin, session: Session):
    email = user.email
    password = user.password
    
    user_located = UserValidation(session=session).exist_user(email)
    
    if not user_located:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Email ou senha estão incorretos, verifique se digitou corretamente. "
                            )
        
    valid_pwd = check_hash(password, user_located.password)
    if not valid_pwd:   
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Email ou senha estão incorretos, verifique se digitou corretamente. "
                            )

    token = create_access_token({"sub": user_located.email})
    
    return {"info": user_located, "access_token": token, "token_type": "bearer"}