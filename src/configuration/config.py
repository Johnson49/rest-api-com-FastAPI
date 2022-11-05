from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./API.db"

engine = create_engine( SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  

def create_database():
    Base.metadata.create_all(bind=engine)

def generate_session():
    database_session = SessionLocal()
    try:
        yield database_session 
    finally:        
        database_session.close()