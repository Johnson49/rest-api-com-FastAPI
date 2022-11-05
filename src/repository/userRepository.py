from sqlalchemy.orm import Session
from model import UserModel
from schemas import UserSchema
from sqlalchemy import select

class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
        
    def create(self, user: UserSchema) -> None:
        user = UserModel(
            username=user.username,
            email=user.email,
            passwords=user.passwords
        )
        
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user
    
    def getUser(self):
        stmt  = select(UserModel)
        users = self.session.execute(stmt).all()
        return users