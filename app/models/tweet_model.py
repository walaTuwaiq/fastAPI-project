from database import Base
from sqlalchemy import Column, Integer,String


class Tweets(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    by = Column(String, index=True)
    post = Column(String, index=True)
    date = Column(String, index=True)