from repository import UserRepository
from configuration import generate_session
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas import UserSchema

def service_get_user(session: Session) :
    result = UserRepository(session=session).get()
    return result


def service_add_user(user: UserSchema,  session: Session):
    result = UserRepository(session=session).create(user)
    return result