import pymongo
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    db = client['Onkar']
    collection = db['Student']
    refield = {'Name':'Sid'}
    setfield = {'$set':{'Address':'Shivneri'}}
    collection.update_one(refield, setfield)
    refield = {'Name':'Onkar'}
    setfield = {'$set':{'Address':'Sadashivnagar'}}
    collection.update_many(refield, setfield)