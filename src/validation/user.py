from sqlalchemy.orm import Session
from model import UserModel

class UserValidation:
    def __init__(self, session: Session) -> None:
        self.session = session
        
        
    def exist_user(self, email: str) -> UserModel:
        user = self.session.query(UserModel).filter_by(email=email).first()
        
        return user
        