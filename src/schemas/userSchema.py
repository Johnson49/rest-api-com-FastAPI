from pydantic import BaseModel


class UserSchemaSignUP(BaseModel):
    username: str
    email: str
    password: str
    
    class Config:
        orm_mode = True
        
        
class UserSchemaLogin(BaseModel):
    email: str
    password: str
    
    class Config:
        orm_mode = True
        
class User(BaseModel):
    id: int
    username: str
    email: str