from fastapi import FastAPI
from database import Base, engine
from routes.user import router as user_routes
from routes.post import router as post_routes


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes)
app.include_router(post_routes)
