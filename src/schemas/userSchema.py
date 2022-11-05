from pydantic import BaseModel


class UserSchemaSignUP(BaseModel):
    username: str
    email: str
    password: str
    
    class Config:
        orm_mode = True