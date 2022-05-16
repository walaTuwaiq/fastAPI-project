from pydantic import BaseModel
from typing import Optional

class Tweets(BaseModel):
    id:Optional[int]
    by:str
    post:str
    date:str

    class Config:
        orm_mode = True

