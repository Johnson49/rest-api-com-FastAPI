from configuration import Base
from sqlalchemy import Column, Integer, String


class UserModel(Base):
    __tablename__  = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    