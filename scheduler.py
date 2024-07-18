# app/scheduler.py
from apscheduler.schedulers.blocking import BlockingScheduler
from categorize import categorize_trips
from update_trip_data import update_trip_data

def run_scheduler():
    scheduler = BlockingScheduler()

    # Schedule the categorize_trips function to run every 10 minutes
    scheduler.add_job(categorize_trips, 'interval', seconds=10, id='categorize_trips_job')
    
    # Schedule the update_all_trip_locations function to run every 5 minutes
    scheduler.add_job(update_trip_data, 'interval', seconds=5, id='update_location_job')

    try:
        print("Starting scheduler...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Stopping scheduler...")
        scheduler.shutdown()

if __name__ == "__main__":
    run_scheduler()
