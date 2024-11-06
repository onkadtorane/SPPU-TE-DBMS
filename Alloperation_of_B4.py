'''Please Start the MongoDB Server first, Create database which name you will enter in program execution,
    then create collection which name you will enter in program execution
    and then Execute this Program'''

import pymongo
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    database = input("Enter Database Name you want to use:")
    db = client[database]
    createCollection = input("Enter Collection Name you want to use:")
    collection = db[createCollection]
    
    flag = True
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    flag5 = True
    while flag == True:
        a = int(input("1) Insert\n2) Update\n3) Delete\n4) Find \n5) Exit\nPlease Select Above Options:"))
        if a == 1:
            while flag1 == True:
                Roll_no = int(input("Enter Student Roll no.:"))
                Name = input("Enter Student Name:")
                Address = input("Enter Student Address:")
                dictionary = {'Roll_no':Roll_no,'Name':Name, 'Address':Address}
                collection.insert_one(dictionary)
                b=input("Do you want to insert another Data..(Y/N)")
                if b == 'y' or b =='Y':
                    flag1 =True
                else:
                    flag1 =False

            print("Thank You For inserting Data")
            input1 = input("Do you want to continue to Opteration (Y/N:)")
            if input1== 'y' or input1=='Y':
                flag =True
            else:
                flag = False

        elif a == 2:
            while flag2 == True:
                value = int(input("Update value of:\n1) Student Roll_no \n2) Student Name \n3) Student Address \nPlease select Above option: "))
                value1 = int(input("Update value by:\n1) Student Roll_no \n2) Student Name \n3) Student Address \nPlease select Above option: "))
                if value <= 3 and value1 <= 3:
                    if value == 1 and value1 == 1:
                        upRoll_no = int(input("Enter Stdent Roll No.:"))
                        Set_Roll_no = int(input("Enter Updated Roll no.:"))
                        refield = {'Roll_no':upRoll_no}
                        setfield = {'$set':{'Roll_no':Set_Roll_no}}
                        collection.update_one(refield, setfield)

                    elif value == 1 and value1 == 2:
                        upRoll_no = int(input("Enter Stdent Roll No.:"))
                        Set_Name = input("Enter Updated Name:")
                        refield = {'Roll_no':upRoll_no}
                        setfield = {'$set':{'Name':Set_Name}}
                        collection.update_one(refield, setfield)

                    elif value == 1 and value1 == 3:
                        upRoll_no = int(input("Enter Stdent Roll No.:"))
                        Set_Address = input("Enter Updated Address:")
                        refield = {'Roll_no':upRoll_no}
                        setfield = {'$set':{'Name':Set_Address}}
                        collection.update_one(refield, setfield)

                    elif value == 2 and value1 == 1:
                        upName = input("Enter Stdent Name:")
                        Set_Roll_no = int(input("Enter Updated Roll no.:"))
                        refield = {'Name':upName}
                        setfield = {'$set':{'Roll_no':Set_Roll_no}}
                        collection.update_one(refield, setfield)

                    elif value == 2 and value1 == 2:
                        upName = input("Enter Stdent Name:")
                        Set_Name = input("Enter Updated Name:")
                        refield = {'Name':upName}
                        setfield = {'$set':{'Name':Set_Name}}
                        collection.update_one(refield, setfield)

                    elif value == 2 and value1 == 3:
                        upName = input("Enter Stdent Name:")
                        Set_Address = input("Enter Updated Address:")
                        refield = {'Name':upName}
                        setfield = {'$set':{'Name':Set_Address}}
                        collection.update_one(refield, setfield)

                    elif value == 3 and value1 == 1:
                        upAddress = input("Enter Stdent Address:")
                        Set_Roll_no = int(input("Enter Updated Roll no.:"))
                        refield = {'Address':upAddress}
                        setfield = {'$set':{'Roll_no':Set_Roll_no}}
                        collection.update_one(refield, setfield)

                    elif value == 3 and value1 == 2:
                        upAddress = input("Enter Stdent Address:")
                        Set_Name = input("Enter Updated Name:")
                        refield = {'Address':upAddress}
                        setfield = {'$set':{'Name':Set_Name}}
                        collection.update_one(refield, setfield)

                    elif value == 3 and value1 == 3:
                        upAddress = input("Enter Stdent Address:")
                        Set_Address = input("Enter Updated Address:")
                        refield = {'Address':upAddress}
                        setfield = {'$set':{'Name':Set_Address}}
                        collection.update_one(refield, setfield)

                    print("Data updated successfully")
                    b=input("Do you want to update another Data..(Y/N)")
                    if b == 'y' or b =='Y':
                        flag2 =True
                    else:
                        flag2 =False

                else:
                    print("Please select correct option:")
                    b=input("Do you want to update Data..(Y/N)")
                    if b == 'y' or b =='Y':
                        flag2 =True
                    else:
                        flag2 =False
        
            print("Thank You For updating Data")
            input2 = input("Do you want to continue  to Operation (Y/N:)")
            if input2== 'y' or input2=='Y':
                flag =True
            else:
                flag = False

        elif a == 3:
            while flag3 == True:
                value3 = int(input("Delete data where:\n1) Student Roll_no \n2) Student Name \n3) Student Address \nPlease select Above option: "))
                if value3 == 1:
                    D_Roll_no = int(input("Enter Student Roll No. you want to delete:"))
                    rec = {'Roll_no':D_Roll_no}
                    collection.delete_one(rec)
                    print("Data deleted successfully")
                    c=input("Do you want to delete another Data..(Y/N)")
                    if c == 'y' or c =='Y':
                        flag3 =True
                    else:
                        flag3 =False
                    
                elif value3 == 2:
                    D_Name = input("Enter Student Name you want to delete:")
                    rec = {'Roll_no':D_Name}
                    collection.delete_one(rec)
                    print("Data deleted successfully")
                    c=input("Do you want to delete another Data..(Y/N)")
                    if c == 'y' or c =='Y':
                        flag3 =True
                    else:
                        flag3 =False

                elif value3 == 3:
                    D_Address = input("Enter Student Name you want to delete:")
                    rec = {'Roll_no':D_Address}
                    collection.delete_one(rec)
                    print("Data deleted successfully")
                    c=input("Do you want to delete another Data..(Y/N)")
                    if c == 'y' or c =='Y':
                        flag3 =True
                    else:
                        flag3 =False

                else:
                    print("Please select correct option:")
                    b=input("Do you want to Delete Data..(Y/N)")
                    if b == 'y' or b =='Y':
                        flag3 =True
                    else:
                        flag3 =False

            print("Thank You For Deleting Data")
            input2 = input("Do you want to continue  to Operation (Y/N:)")
            if input2== 'y' or input2=='Y':
                flag =True
            else:
                flag = False


        elif a == 4:
            while flag4 == True:
                value4 = int(input("1)Find All entries \n2)Find by \nPlease select Above option:"))
                if value4 == 1:
                    for document in collection.find():
                        print(document)
                    print("Data Found successfully")
                    c=input("Do you want to Find another Data..(Y/N)")
                    if c == 'y' or c =='Y':
                        flag4 =True
                    else:
                        flag4 =False

                elif value4 == 2:
                    while flag5 == True:
                        value5 = int(input("Find Data By:\n1) Student Roll_no \n2) Student Name \n3) Student Address \nPlease select Above option: "))
                        if value5 == 1:
                            F_Roll_no = int(input("Enter Student Roll no. whose data you want:"))
                            for document in collection.find({"Roll_no": F_Roll_no}):
                                print(document)
                            
                            print("Data Found successfully")
                            c=input("Do you want to Find another Data..(Y/N)")
                            if c == 'y' or c =='Y':
                                flag5 =True
                            else:
                                flag5 =False
                        

                        elif value5 == 2:
                            F_Name = input("Enter Student Name whose data you want:")
                            for document in collection.find({"Name": F_Name}):
                                print(document)
                            
                            print("Data Found successfully")
                            c=input("Do you want to Find another Data..(Y/N)")
                            if c == 'y' or c =='Y':
                                flag5 =True
                            else:
                                flag5 =False

                        elif value5 == 3:
                            F_Address = input("Enter Student Address whose data you want:")
                            for document in collection.find({"Address": F_Address}):
                                print(document)
                            
                            print("Data Found successfully")
                            c=input("Do you want to Find another Data..(Y/N)")
                            if c == 'y' or c =='Y':
                                flag5 =True
                            else:
                                flag5 =False

                        else:
                            print("Please select correct option:")
                            b=input("Do you want to Find Data..(Y/N)")
                            if b == 'y' or b =='Y':
                                flag5 =True
                            else:
                                flag5 =False
                    
                    if flag5 == False:
                        b=input("Do you want to Find Data..(Y/N)")
                        if b == 'y' or b =='Y':
                            flag4 =True
                        else:
                            flag4 =False
                else:
                    print("Please select correct option:")
                    b=input("Do you want to Find Data..(Y/N)")
                    if b == 'y' or b =='Y':
                        flag4 =True
                    else:
                        flag4 =False
            
            if flag4 == False:   
                print("Thank You For Finding Data")
                input2 = input("Do you want to continue to Operation (Y/N):")
                if input2== 'y' or input2=='Y':
                    flag =True
                else:
                    flag = False
        
        elif a == 5:
            flag = False

        else:
            print("Please select correct option:")
            input2 = input("Do you want to continue  to Operation (Y/N:)")
            if input2== 'y' or input2=='Y':
                flag =True
            else:
                flag = False

    if flag == False:
        print("Thak you!")