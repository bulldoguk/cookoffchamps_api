from modules.db.mongodb import get_db
from pymongo import ReturnDocument


def add_or_update(info):
    try:
        user_collection = get_db().users

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