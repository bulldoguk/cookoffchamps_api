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
        print(f'got user', info)
        record = user_collection.find_one_and_update(
            {"email": info.get("email")},
            {"$set": info},
            upsert=True,
            return_document=ReturnDocument.AFTER)
        # All member of the myhmbiz.com home domain are superusers here automatically
        if record.get("hd") == 'myhmbiz.com':
            record["superAdmin"] = True
        return record
    except Exception as e:
        print('Failed to update user record', e)
        return None


class UserActions:
    pass
