from fastapi import APIRouter, status, Depends
from services import service_get_user, service_get_user_id, service_add_user, service_update_user, service_delete_user, service_login_user
from schemas import UserSchemaSignUP, UserSchemaLogin, User
from sqlalchemy.orm import Session
from configuration import generate_session
from utility import get_authenticated_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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

@routes.post("/me", response_model=User)
def me(user: User = Depends(get_authenticated_user)):
    return user

# @routes.post("/token")
# async def token_generate(form: OAuth2PasswordRequestForm = Depends()):
#     print(form)
#     return{"access_token": form.username, "token_type": "bearer"}

# oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @routes.get("/self")
# async def self(token: str = Depends(oauth_scheme)):
#     print(token)
#     return{
#         "user": "teste",
#         "profile_pic": "my_face"
#     }