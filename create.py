import pymongo
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    db = client['Onkar']
    collection = db['Student']
    dictionary = {'Roll_no':1,'Name':'Aditya', 'Address':'Pune'}
    collection.insert_one(dictionary)