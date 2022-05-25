# mongodb+srv://cookoffchamps:pdTmw1QfihTyTgc6@cluster0.pljfk.mongodb.net/?retryWrites=true&w=majority

# public key: fefcuqpt
# private key: 40dd99f4-fc95-432e-a2a9-8818d7416985

from schema import template
from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://cookoffchamps:pdTmw1QfihTyTgc6@cluster0.pljfk.mongodb.net/?retryWrites=true&w=majority')
db = client.cookoffchamps
# Issue the serverStatus command and print the results
serverStatusResult = db.list_collection_names()
for collection in template.collections:
    if collection in serverStatusResult:
        print(f'Found {collection}')
    else:
        print(f'Failed to find collection {collection}')
