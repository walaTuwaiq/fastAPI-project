from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


postgres_url = "postgresql://postgres:123@localhost:5432/Twitter"
engine = create_engine(postgres_url)
localsession = sessionmaker(bind=engine, autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    db = localsession()

    try:
        yield db
    finally:
        db.close()