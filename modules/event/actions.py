from modules.db.mongodb import get_db
from pymongo import ReturnDocument
from bson import json_util
import json

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


def list_events(userguid):
    try:
        event_collection = get_db().events
        if userguid == 'None':
            user_filter = {}
        else:
            user_filter = {"$or": [
                {"ownerGUID": userguid},
                {"admin": userguid}
            ]}
        events = event_collection.find(user_filter)
        return json.loads(json_util.dumps(events))
    except Exception as e:
        print('Failed to list events', e)
        return None


class EventActions:
    pass
