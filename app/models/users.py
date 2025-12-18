from sqlalchemy import Column, Integer, String, DateTime  #type: ignore
from datetime import datetime, timezone
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda:datetime.now(timezone.utc))
