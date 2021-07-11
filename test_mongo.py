import pymongo

# replace this with your MongoDB connection string
conn_str = "mongodb+srv://user1:user1@quantcrunch.nv9sn.mongodb.net/quantcrunch?retryWrites=true&w=majority"


# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    client.server_info()
except Exception:
    print("Unable to connect to the server.")

db = client.get_database('quantcrunch')

col = db['tickers']

cnt = col.count_documents({})

print(cnt)
