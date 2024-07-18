from faker import Faker
import random
from database import collection

fake = Faker()

def generate_fake_trip_data(num_trips):
    trips = []
    for _ in range(num_trips):
        trip = {
            "source": random.choice(["driver_app", "cargoxchange", "retool"]),
            "trip_number": fake.uuid4(),
            "lat": float(fake.latitude()),
            "lon": float(fake.longitude()),
            "recordAt": fake.date_time_between(start_date='-1d', end_date='now').isoformat()
        }
        trips.append(trip)
    return trips

# Check if the collection is empty before inserting
if collection.count_documents({}) == 0:
    trips = generate_fake_trip_data(5)
    collection.insert_many(trips)
    print("Inserted initial set of trips.")
else:
    print("Trips already exist in the database.")
