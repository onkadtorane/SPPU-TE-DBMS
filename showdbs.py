import pymongo
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    alldbs = client.list_database_names()
    print(alldbs)
    col = client['Onkar']
    print(col.list_collection_names())