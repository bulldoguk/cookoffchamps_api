from modules.db.mongodb import get_db
from pymongo import ReturnDocument
import uuid


def add_or_update(info):
    try:
        event_collection = get_db().events
        if not info.get("guid"):
            info["guid"] = str(uuid.uuid4())
            # For a new event, this person is the owner
            info["ownerGUID"] = info.get("userGUID")
            # Add a blank array for our future admin users
            info["admin"] = []
            # Remove the userGUID - we don't want that left behind
            del info["userGUID"]

        record = event_collection.find_one_and_update(
            {"guid": info.get("guid")},
            {"$set": info},
            upsert=True,
            return_document=ReturnDocument.AFTER)
        return record
    except Exception as e:
        print('Failed to update event record', e)
        return None


class EventActions:
    pass
