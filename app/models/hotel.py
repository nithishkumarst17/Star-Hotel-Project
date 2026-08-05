from sqlalchemy import Column, Integer, String
from app.database import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    location = Column(
        String
    )