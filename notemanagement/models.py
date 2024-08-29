from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from config import Config

client = MongoClient(Config.MONGO_URI)
database = client[Config.DATABASE]
users = database['users']
notes = database['notes']
counts = database['count']


def generate_id():
    current_count = counts.find_one({"name": "user_id"})["count"]
    new_count = current_count + 1
    counts.update_one({"name": "user_id"}, {"$set": {"count": new_count}})
    return new_count

