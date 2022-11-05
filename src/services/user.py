from repository import UserRepository
from configuration import generate_session
from sqlalchemy.orm import Session
from fastapi import Depends, status
from schemas import UserSchema

def service_get_user(session: Session = Depends(generate_session)) :
    result = UserRepository(session=session).get_user()
    return result


def service_add_user(user: UserSchema,  session: Session = Depends(generate_session)):
    result = UserRepository(session=session).add_user(user)
    return result