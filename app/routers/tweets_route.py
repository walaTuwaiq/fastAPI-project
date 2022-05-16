from fastapi import APIRouter,Response, status, HTTPException, Depends
import schemas.tweet_schema as tweet_schema
from models import tweet_model
import main
from typing import List, Optional
from database import get_db
from sqlalchemy.orm import Session
from controllers import tweet_controller


router = APIRouter(tags=["tweets"], prefix="/tweets")


@router.get('/all', response_model=List[tweet_schema.Tweets],status_code=200)
def get_all(db : Session = Depends(get_db)):
    return tweet_controller.show_all(db)


@router.get('/{tweet_id}',response_model=tweet_schema.Tweets,status_code=status.HTTP_200_OK)
def get_tweet(tweet_id:int,db : Session = Depends(get_db)):
    return tweet_controller.get_by_id(tweet_id, db)

###############    requirments    ###############

# @router.get('/all/',status_code=200)
# # Can i deleted response model?
# def get_all( item_id: Optional[int] = None ):
#     if item_id is None:
#         items= main.db.query(tweet_model.Tweets).all()
#         return items
#     else:
#         item = main.db.query(tweet_model.Tweets).filter(tweet_model.Tweets.id==item_id).first()
#         return item

###############    requirments    ###############


@router.post('/new-tweet', response_model=tweet_schema.Tweets, status_code=status.HTTP_201_CREATED)
def create(tweet: tweet_schema.Tweets, db : Session = Depends(get_db)):
    return tweet_controller.new_tweet(tweet,db)


@router.put('/update/{item_id}',response_model=tweet_schema.Tweets,status_code=status.HTTP_200_OK)
def update(item_id:int,item:tweet_schema.Tweets, db : Session = Depends(get_db)):

    item_to_update=main.db.query(tweet_model.Tweets).filter(tweet_model.Tweets.id==item_id).first()
    item_to_update.id=item.id
    item_to_update.by=item.by
    item_to_update.post=item.post
    item_to_update.date=item.date

    main.db.commit()

    return item_to_update


@router.delete('/remove/{item_id}')
def delete(item_id: int, db : Session = Depends(get_db)):
    item_to_delete = main.db.query(tweet_model.Tweets).filter(tweet_model.Tweets.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    main.db.delete(item_to_delete)
    main.db.commit()

    return item_to_delete