from fastapi import APIRouter, status, Depends
from services import (service_get_user, 
                      service_get_user_id, 
                      service_add_user, 
                      service_update_user, 
                      service_delete_user, 
                      service_login_user,
                      service_info_user_private
                      )
from schemas import UserSchemaSignUP, UserSchemaLogin, User, UserBasic
from sqlalchemy.orm import Session
from configuration import generate_session
from utility import JwtBearer


routes = APIRouter()

@routes.get("/api/user")
def get_user(session: Session = Depends(generate_session)):
    return service_get_user(session=session)

@routes.get("/api/user/{id}")
def get_user(id:int, session: Session = Depends(generate_session)):
    return service_get_user_id(session=session, id=id)

@routes.post("/auth/sign-up", status_code=status.HTTP_201_CREATED)
def add_user(user: UserSchemaSignUP, session: Session = Depends(generate_session)):
    return service_add_user(user=user, session=session)

@routes.put("/api/user/edit/{id}", status_code=status.HTTP_200_OK)
def add_user(id:int, user: UserSchemaSignUP, session: Session = Depends(generate_session)):
    return service_update_user(user=user, session=session, id=id)

@routes.delete("/api/user/{id}", status_code=status.HTTP_200_OK)
def add_user(id:int, session: Session = Depends(generate_session)):
    return service_delete_user(session=session, id=id)

@routes.post("/auth/sign-in")
def login_user(user: UserSchemaLogin ,session: Session = Depends(generate_session)):    
    return service_login_user(user=user, session=session)

@routes.post("/auth/me", dependencies=[Depends(JwtBearer())])
def me(user: User, session: Session = Depends(generate_session)):
    user_located = service_info_user_private(session=session, user=user)
    
    return UserBasic(username=user_located.username, email  =user_located.email)