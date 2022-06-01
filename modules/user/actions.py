from modules.db.mongodb import get_db
from pymongo import ReturnDocument
import uuid


def add_or_update(info):
    try:
        user_collection = get_db().users
        # must always have extended_info: True when we have our own user record
        info["extended_info"] = True
        if not info.get("guid"):
            info["guid"] = str(uuid.uuid4())

        record = user_collection.find_one_and_update(
            {"email": info.get("email")},
            {"$set": info},
            upsert=True,
            return_document=ReturnDocument.AFTER)
        return record
    except:
        print('Failed to update user record')
        return None


class UserActions:
    pass
