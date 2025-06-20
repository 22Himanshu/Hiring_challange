import os
import sys
import unittest
from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.seed_data import seed_data
from src.models.hotel import Hotel, RoomType
from src.models.user import Base


class TestDataSeeding(unittest.TestCase):
    def setUp(self):
        """Set up a temporary in-memory database for testing."""
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def tearDown(self):
        """Tear down the database."""
        Base.metadata.drop_all(self.engine)

    def test_seed_data(self):
        """Test that the seed_data function populates the database correctly."""

        # We need to temporarily replace the SessionLocal in the script with our test session
        from scripts import seed_data as seeder

        original_session = seeder.SessionLocal
        seeder.SessionLocal = self.Session

        # Run the seeder
        seed_data()

        # Verify the data
        session = self.Session()
        hotel_count = session.query(Hotel).count()
        room_type_count = session.query(RoomType).count()

        self.assertGreater(hotel_count, 0, "No hotels were seeded.")
        self.assertEqual(hotel_count, 5, "Expected 5 hotels to be seeded.")
        self.assertGreater(room_type_count, 0, "No room types were seeded.")

        # Check a specific hotel
        hotel = session.query(Hotel).filter_by(name="Grand Plaza Hotel").one()
        self.assertEqual(hotel.star_rating, 5)
        self.assertEqual(len(hotel.room_types), 2)

        # Check a specific room type
        room = hotel.room_types[0]
        self.assertEqual(room.name, "Deluxe Room")
        self.assertEqual(room.base_price, Decimal("250.00"))

        session.close()

        # Restore the original session to avoid side effects
        seeder.SessionLocal = original_session


if __name__ == "__main__":
    unittest.main()
