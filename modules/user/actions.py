from modules.db.mongodb import get_db
from pymongo import ReturnDocument
import uuid


def add_or_update(info):
    try:
        user_collection = get_db().users
        # must always have extended_info: True when we have our own user record
        info["extended_info"] = True
        record = user_collection.find_one_and_update(
            {"email": info.get("email")},
            {"$set": info},
            upsert=True,
            return_document=ReturnDocument.AFTER)
        # All member of the myhmbiz.com home domain are superusers here automatically
        if record.get("hd") == 'myhmbiz.com':
            record["superAdmin"] = True
        else:
            record["superAdmin"] = False
        # if this is a new user, we need to set a unique GUID
        if not record.get("guid"):
            finalRecord = user_collection.find_one_and_update(
                {"email": record.get("email")},
                {"$set":
                    {
                        "guid": str(uuid.uuid4()),
                        "superAdmin": record.get("superAdmin")
                    }
                },
                return_document=ReturnDocument.AFTER
            )
            return finalRecord
        else:
            return record
    except Exception as e:
        print('Failed to update user record', e)
        return None


class UserActions:
    pass
