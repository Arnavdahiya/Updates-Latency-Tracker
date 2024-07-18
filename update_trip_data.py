from faker import Faker
from database import collection
from datetime import datetime
import random

fake = Faker()

def update_trip_data():
    trips = collection.find()
    for trip in trips:
        # Simulate irregular updates by updating only some trips
        if random.choice([True, False]):
            new_location = {
                "lat": float(fake.latitude()),
                "lon": float(fake.longitude()),
                "recordAt": datetime.now().isoformat()
            }
            collection.update_one({"_id": trip["_id"]}, {"$set": new_location})
            print(f"Updated trip {trip['trip_number']} with new location data.")

if __name__ == "__main__":
    update_trip_data()
