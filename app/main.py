from fastapi import FastAPI
import routers.tweets_route as tweets_route
from database import localsession, Base,engine


Base.metadata.create_all(engine)


app = FastAPI()

# db = localsession()

app.include_router(tweets_route.router)

# @app.get("/")
# def aa():
#     return " Hello!"