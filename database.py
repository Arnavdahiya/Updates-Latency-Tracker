# app/database.py
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client.ttest
collection = db.get_collection("trips")
history_collection = db.get_collection("history_trips")