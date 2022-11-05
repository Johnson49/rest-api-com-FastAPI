from fastapi import APIRouter
from services import service_get_user


routes = APIRouter()

@routes.get("/api/user")
def get_user():
    return service_get_user()