from sqlalchemy.orm import Session
from schemas import UserSchema

class UserValidation:
    def __init__(self, session: Session) -> None:
        self.session = session
        
        
    def exist_user(self, email: str) -> UserSchema:
        user = self.session.query(UserSchema).filter_by(email=email).first()
        
        return user
        