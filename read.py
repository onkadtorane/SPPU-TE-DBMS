import pymongo
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    db = client['Onkar']
    collection = db['Student']
    one = collection.find_one({'Name':'Sid'})
    print(one)
    alldocs = collection.find()
    for item in alldocs:
        print(item)