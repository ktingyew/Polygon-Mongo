from controllers.mongo import MONGOCOL

cnt = MONGOCOL.count_documents({})

print(cnt)
