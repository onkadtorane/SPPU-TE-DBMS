import pymongo
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    db = client['Onkar']
    collection = db['Student']
    dictionary2 = {'Roll_no':24, 'Name':'Sid', 'Address':'Junnar'}
    collection.insert_one(dictionary2)
    allthese = [{'Roll_no':52, 'Name':'Suraj', 'Address':'Siddhatek'},{'roll_no':54, 'Name':'Onkar', 'Address':'Akluj'}]
    collection.insert_many(allthese)