from sqlalchemy import (DECIMAL, JSON, Column, DateTime, ForeignKey, Integer,
                        String, func)
from sqlalchemy.orm import relationship

from .user import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    star_rating = Column(Integer)
    description = Column(String)
    amenities = Column(JSON)
    policies = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    room_types = relationship("RoomType", back_populates="hotel")


class RoomType(Base):
    __tablename__ = "room_types"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    max_occupancy = Column(Integer)
    base_price = Column(DECIMAL(10, 2))
    features = Column(JSON)
    hotel = relationship("Hotel", back_populates="room_types")
