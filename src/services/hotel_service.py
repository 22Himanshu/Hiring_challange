from sqlalchemy.orm import Session, joinedload

from src.models.hotel import Hotel, RoomType


class HotelService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_hotels(self):
        """
        Retrieves all hotels from the database.
        """
        return self.db_session.query(Hotel).all()

    def find_hotel_by_name(self, name: str):
        """
        Finds a hotel by its exact name, case-insensitive.
        """
        return self.db_session.query(Hotel).filter(Hotel.name.ilike(name)).first()

    def search_hotels(self, location: str = None, min_rating: int = None):
        """
        Searches for hotels based on location and minimum star rating.
        """
        query = self.db_session.query(Hotel)
        if location:
            query = query.filter(Hotel.location.ilike(f"%{location}%"))
        if min_rating:
            query = query.filter(Hotel.star_rating >= min_rating)
        return query.all()

    def get_hotel_details(self, hotel_id: int):
        """
        Retrieves details for a specific hotel, including its room types.
        """
        return (
            self.db_session.query(Hotel)
            .options(joinedload(Hotel.room_types))
            .filter(Hotel.id == hotel_id)
            .first()
        )
