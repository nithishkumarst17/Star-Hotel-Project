from fastapi import APIRouter

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)

@router.get("/test")
def hotel_test():
    return {"message": "Hotel router working"}