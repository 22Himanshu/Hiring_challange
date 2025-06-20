import os
import sys
import timeit

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.integrations.database_client import SessionLocal
from src.services.hotel_service import HotelService


def run_performance_test():
    """
    Runs a series of performance tests on the database query functions.
    """
    db = SessionLocal()
    hotel_service = HotelService(db)

    print("--- Starting Database Query Performance Test ---")

    # --- Test 1: Get all hotels ---
    get_all_hotels_stmt = "hotel_service.get_all_hotels()"
    get_all_hotels_time = timeit.timeit(
        stmt=get_all_hotels_stmt, globals={"hotel_service": hotel_service}, number=100
    )
    avg_time_all = (get_all_hotels_time / 100) * 1000
    print(f"[*] Get all hotels (100 runs): {avg_time_all:.4f} ms per run")

    # --- Test 2: Search by location ---
    search_location_stmt = "hotel_service.search_hotels(location='Metropolis')"
    search_location_time = timeit.timeit(
        stmt=search_location_stmt, globals={"hotel_service": hotel_service}, number=100
    )
    avg_time_location = (search_location_time / 100) * 1000
    print(f"[*] Search by location (100 runs): {avg_time_location:.4f} ms per run")

    # --- Test 3: Search by rating ---
    search_rating_stmt = "hotel_service.search_hotels(min_rating=4)"
    search_rating_time = timeit.timeit(
        stmt=search_rating_stmt, globals={"hotel_service": hotel_service}, number=100
    )
    avg_time_rating = (search_rating_time / 100) * 1000
    print(f"[*] Search by rating (100 runs): {avg_time_rating:.4f} ms per run")

    # --- Test 4: Get hotel details (with room types) ---
    hotel = hotel_service.find_hotel_by_name("Grand Plaza Hotel")
    if hotel:
        details_stmt = f"hotel_service.get_hotel_details(hotel_id={hotel.id})"
        details_time = timeit.timeit(
            stmt=details_stmt, globals={"hotel_service": hotel_service}, number=100
        )
        avg_time_details = (details_time / 100) * 1000
        print(f"[*] Get hotel details (100 runs): {avg_time_details:.4f} ms per run")

    print("\n--- Performance Test Completed ---")
    db.close()


if __name__ == "__main__":
    print("Ensuring database is seeded...")
    from scripts.seed_data import seed_data

    seed_data()

    print("\nStarting performance test...")
    run_performance_test()
