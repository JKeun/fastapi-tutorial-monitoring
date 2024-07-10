from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SERVER_NAME = "fastapi"
DATABASE_NAME = "postgres"
SQLALCHEMY_DATABASE_URL = f"postgresql://{SERVER_NAME}:1234@localhost:5432/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()