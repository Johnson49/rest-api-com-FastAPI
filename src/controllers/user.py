from fastapi import APIRouter, status, Depends
from services import service_get_user, service_get_user_id, service_add_user, service_update_user, service_delete_user
from schemas import UserSchema
from sqlalchemy.orm import Session
from configuration import generate_session
routes = APIRouter()

@routes.get("/api/user")
def get_user(session: Session = Depends(generate_session)):
    return service_get_user(session=session)

@routes.get("/api/user/{id}")
def get_user(id:int, session: Session = Depends(generate_session)):
    return service_get_user_id(session=session, id=id)


@routes.post("/auth/sign-up", status_code=status.HTTP_201_CREATED)
def add_user(user: UserSchema, session: Session = Depends(generate_session)):
    return service_add_user(user=user, session=session)

@routes.put("/api/user/edit/{id}", status_code=status.HTTP_200_OK)
def add_user(id:int, user: UserSchema, session: Session = Depends(generate_session)):
    return service_update_user(user=user, session=session, id=id)

@routes.delete("/api/user/{id}", status_code=status.HTTP_200_OK)
def add_user(id:int, session: Session = Depends(generate_session)):
    return service_delete_user(session=session, id=id)