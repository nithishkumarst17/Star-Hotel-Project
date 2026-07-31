from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
from app.api.chat import router

app = FastAPI(
    title="Hotel AI Assistant"
)

app.include_router(router)
app = FastAPI()

class Booking(BaseModel):
    name: str
    room: int

@app.get("/")
def home():
    return {"message": "Hotel AI Assistant"}

@app.get("/health")
def health():
    return {
        "status":"healthy"
    }

@app.get("/room/{room_id}")
def get_room(room_id: int):
    return {
        "room": room_id
    }
@app.get("/search")
def search(city: str):
    return {
        "city": city
    }

@app.post("/booking")
def create_booking(data: Booking):
    return data

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Star Hotel AI API Running"
    }