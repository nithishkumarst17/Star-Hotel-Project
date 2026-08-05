from app.database import Base, engine

from app.models.hotel import Hotel
from app.models.user import User


Base.metadata.create_all(bind=engine)

print("All tables created")