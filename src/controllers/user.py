from fastapi import APIRouter, status
from services import service_get_user, service_add_user
from schemas import UserSchema

routes = APIRouter()

@routes.get("/api/user")
def get_user():
    return service_get_user()


@routes.post("/api/sign-up", status_code=status.HTTP_201_CREATED)
def add_user(user: UserSchema):
    return service_add_user(user=user)