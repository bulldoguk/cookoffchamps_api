from modules.db.schema import template
from pymongo import MongoClient

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://cookoffchamps_api:dQBlGRuVkj1OGzD6@cluster0.gcoozxh.mongodb.net/?retryWrites=true&w=majority')

db = client.cookoffchamps
# Issue the serverStatus command and print the results
serverStatusResult = db.list_collection_names()
for collection in template.collections:
    if collection in serverStatusResult:
        print(f'Found {collection}')
    else:
        print(f'Failed to find collection {collection}')


def get_db():
    return db
