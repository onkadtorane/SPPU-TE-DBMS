import pymongo
if __name__ == "__main__":
	print("Welcome to pyMongo")
	client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    #print(client)
	db = client['Onkar']
	collection = db['Student']
	a = int(input("Enter No. of Students"))
	for i in range(0,a):
	    Roll_no = int(input("Enter Rollno:"))
	    Name = input("Enter Student name:")
	    Address = input("Enter Address:")
	    dictionary2 = {'Roll_no': Roll_no, 'Name': Name, 'Address': Address}
	    collection.insert_one(dictionary2)

