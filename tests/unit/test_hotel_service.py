import os
import sys
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.seed_data import seed_data
from src.models.user import Base
from src.services.hotel_service import HotelService


class TestHotelService(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

        # Seed the database
        from scripts import seed_data as seeder

        original_session = seeder.SessionLocal
        seeder.SessionLocal = self.Session
        # To test the service, we first need to re-seed the db with new mock data
        # Clearing the db before running the test
        self.db = self.Session()
        for table in reversed(Base.metadata.sorted_tables):
            self.db.execute(table.delete())
        self.db.commit()
        seed_data()
        seeder.SessionLocal = original_session

        # Create a session for the service
        self.session = self.Session()
        self.hotel_service = HotelService(self.session)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_get_all_hotels(self):
        hotels = self.hotel_service.get_all_hotels()
        self.assertEqual(len(hotels), 5)

    def test_find_hotel_by_name(self):
        hotel = self.hotel_service.find_hotel_by_name("Grand Plaza Hotel")
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.star_rating, 5)  # type: ignore

        # Test case-insensitivity
        hotel_lower = self.hotel_service.find_hotel_by_name("grand plaza hotel")
        self.assertIsNotNone(hotel_lower)
        self.assertEqual(hotel.id, hotel_lower.id)  # type: ignore

        hotel_none = self.hotel_service.find_hotel_by_name("Non Existent Hotel")
        self.assertIsNone(hotel_none)

    def test_search_hotels_by_location(self):
        hotels = self.hotel_service.search_hotels(location="Metropolis")
        self.assertEqual(len(hotels), 2)
        hotel_names = {h.name for h in hotels}
        self.assertIn("Grand Plaza Hotel", hotel_names)
        self.assertIn("City Center Inn", hotel_names)

    def test_search_hotels_by_rating(self):
        hotels = self.hotel_service.search_hotels(min_rating=5)
        self.assertEqual(len(hotels), 2)
        hotel_names = {h.name for h in hotels}
        self.assertIn("Grand Plaza Hotel", hotel_names)
        self.assertIn("Heritage Palace Hotel", hotel_names)

    def test_search_hotels_by_location_and_rating(self):
        hotels = self.hotel_service.search_hotels(location="Metropolis", min_rating=5)
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0].name, "Grand Plaza Hotel")

    def test_get_hotel_details(self):
        # First find a hotel to get its ID
        hotel_to_find = self.hotel_service.find_hotel_by_name("Seaside Resort & Spa")
        self.assertIsNotNone(hotel_to_find)

        hotel_details = self.hotel_service.get_hotel_details(hotel_to_find.id)  # type: ignore
        self.assertIsNotNone(hotel_details)
        self.assertEqual(hotel_details.name, "Seaside Resort & Spa")  # type: ignore
        self.assertEqual(len(hotel_details.room_types), 2)  # type: ignore
        self.assertEqual(hotel_details.room_types[0].name, "Ocean View Room")  # type: ignore


if __name__ == "__main__":
    unittest.main()
