import json
import os
import sys
from decimal import Decimal

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.integrations.database_client import SessionLocal
from src.models.hotel import Hotel, RoomType


def seed_data():
    """
    Populates the database with mock hotel and room type data from a JSON file.
    """
    db = SessionLocal()

    # Check if data already exists to prevent duplicates
    if db.query(Hotel).first():
        print("Data already exists. Skipping seeding.")
        db.close()
        return

    print("Seeding hotel data...")

    try:
        # Construct the path to the JSON file
        json_path = os.path.join(
            os.path.dirname(__file__), "..", "data", "mock_hotels.json"
        )

        with open(json_path, "r") as f:
            hotels_data = json.load(f)

        for hotel_data in hotels_data:
            # Create Hotel object
            new_hotel = Hotel(
                name=hotel_data["name"],
                location=hotel_data["location"],
                star_rating=hotel_data["star_rating"],
                description=hotel_data["description"],
                amenities=hotel_data["amenities"],
                policies=hotel_data["policies"],
            )
            db.add(new_hotel)

            # Flush to get the new_hotel.id for the foreign key
            db.flush()

            # Create RoomType objects for the hotel
            for room_data in hotel_data["room_types"]:
                new_room_type = RoomType(
                    hotel_id=new_hotel.id,
                    name=room_data["name"],
                    description=room_data["description"],
                    max_occupancy=room_data["max_occupancy"],
                    base_price=Decimal(str(room_data["base_price"])),
                    features=room_data["features"],
                )
                db.add(new_room_type)

        db.commit()
        print("✅ Hotel data seeded successfully.")

    except Exception as e:
        print(f"❌ Error seeding data: {e}")
        db.rollback()

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
