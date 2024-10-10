import pymongo
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    db = client['Onkar']
    collection = db['Student']
    rec = {'Name':'Sid'}
    collection.delete_one(rec)
    rec2 = {'Name':'Onkar'}
    collection.delete_many(rec2)