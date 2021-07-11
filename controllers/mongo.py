from decouple import config
import pymongo

MONGOURI = config('MONGO_URI')
MONGODB = config('MONGO_DATABASE')
MONGOCOL = config('MONGO_COLLECTION')

# set a 5-second connection timeout
client = pymongo.MongoClient(MONGOURI, serverSelectionTimeoutMS=5000)
try:
    client.server_info()
except Exception:
    print("Unable to connect to the server.")

MONGODB = client.get_database(MONGODB)
MONGOCOL = MONGODB[MONGOCOL]