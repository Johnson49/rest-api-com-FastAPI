from sqlalchemy.orm import Session
from model import UserModel
from schemas import UserSchemaSignUP
from sqlalchemy import select

class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
        
    def create(self, user: UserSchemaSignUP) -> UserModel:
        user = UserModel(
            username=user.username,
            email=user.email,
            password=user.password
        )
        
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user
    
    def get(self) -> UserModel:
        stmt  = select(UserModel)
        users = self.session.execute(stmt).all()
        return users
    
    def get_id(self, id: int) -> UserModel:
        user = self.session.query(UserModel).filter_by(id=id).first()
        return user
    
    def update(self, id: int, user: UserSchemaSignUP) -> UserModel:
     
        stmt_updated = self.session.query(UserModel).filter(UserModel.id == id).update(
                { 
                    "username":user.username,
                    "email":user.email,
                    "password":user.password
                }, synchronize_session="fetch"
            )

        self.session.commit()
        return stmt_updated

    def delete(self, id: int) -> None:
        self.session.query(UserModel).filter_by(id = id).delete()
        self.session.commit()