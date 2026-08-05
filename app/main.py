from fastapi import FastAPI

from app.routers import auth
from app.routers import hotels


app = FastAPI(
    title="StarHotel API",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(hotels.router)


@app.get("/")
def home():
    return {
        "message": "StarHotel API running"
    }