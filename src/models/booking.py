from sqlalchemy import (DECIMAL, Column, Date, DateTime, ForeignKey, Integer,
                        String, func)
from sqlalchemy.orm import relationship

from .user import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    room_type_id = Column(Integer, ForeignKey("room_types.id"), nullable=False)
    check_in_date = Column(Date)
    check_out_date = Column(Date)
    num_guests = Column(Integer)
    total_price = Column(DECIMAL(10, 2))
    status = Column(String, default="confirmed")
    booking_reference = Column(String, unique=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    modifications = relationship("BookingModification", back_populates="booking")


class BookingModification(Base):
    __tablename__ = "booking_modifications"

    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    modification_type = Column(String)  # 'reschedule', 'cancel'
    old_check_in = Column(Date)
    old_check_out = Column(Date)
    new_check_in = Column(Date)
    new_check_out = Column(Date)
    fee_charged = Column(DECIMAL(10, 2))
    created_at = Column(DateTime, default=func.now())

    booking = relationship("Booking", back_populates="modifications")
