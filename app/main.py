from fastapi import FastAPI
from pydantic import BaseModel

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
