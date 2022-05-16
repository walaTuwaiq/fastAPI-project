
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import tweet_model
import schemas.tweet_schema as tweet_schema


def show_all(db : Session):
    tweet= db.query(tweet_model.Tweets).all()

    return tweet

def get_by_id(tweet_id:int,db : Session):
    tweet = db.query(tweet_model.Tweets).filter(tweet_model.Tweets.id==tweet_id).first()

    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Item with id {tweet_id} is not Available")

    return tweet


def new_tweet(tweet: tweet_schema.Tweets, db : Session):

    new_tweet = tweet_model.Tweets(
        id = tweet.id,
        by = tweet.by,
        post = tweet.post,
        date = tweet.date
    )

    db.add(new_tweet)
    db.commit()

    return new_tweet