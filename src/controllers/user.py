from fastapi import APIRouter, status, Depends
from services import service_get_user, service_add_user
from schemas import UserSchema
from sqlalchemy.orm import Session
from configuration import generate_session
routes = APIRouter()

@routes.get("/api/user")
def get_user(session: Session = Depends(generate_session)):
    return service_get_user(session=session)


@routes.post("/api/sign-up", status_code=status.HTTP_201_CREATED, )
def add_user(user: UserSchema, session: Session = Depends(generate_session)):
    return service_add_user(user=user, session=session)