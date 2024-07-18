from datetime import datetime
from bson import ObjectId
from database import collection
from database import history_collection

def categorize_trips():
    current_time = datetime.now()
    trips = list(collection.find())

    categorized_trips = []

    for trip in trips:
        last_update = datetime.fromisoformat(trip["recordAt"])
        time_diff = (current_time - last_update).total_seconds() / 3600

        if time_diff < 3:
            alert_level = 0
        elif 3 <= time_diff < 4:
            alert_level = 1
        elif 4 <= time_diff < 7:
            alert_level = 2
        else:
            alert_level = 3

        trip['alert_level'] = alert_level
        categorized_trips.append(trip)
        # Print trip ID and alert level for debugging
        print(f"Trip {trip['_id']} - Alert Level: {alert_level}")

    #Move current records to history collection  
    if trips:
        for trip in trips:
            trip['_id'] = ObjectId()
        history_collection.insert_many(trips)
        collection.delete_many({})

    if categorized_trips:
        collection.insert_many(categorized_trips)
    return categorized_trips

if __name__ == "__main__":  
    categorized_trips = categorize_trips()
    print(f"Categorized {len(categorized_trips)} trips.")
    