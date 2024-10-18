import mysql.connector as c
con = c.connect(host = 'localhost', user = 'Your_username', password = 'ypur_password', database = 'your_database')
if con.is_connected():
    print('mysql successfully connected Now, You Can Perform verious opration:')
else:
    print('some connectivity issue')

flag = True
flag1 = True
flag2 = True
flag3 = True
while flag == True:
    a = int(input("1) Insert\n2) Update\n3) Delete\n4) Exit\nPlease Select Above Options:"))
    if a == 1:
        while flag1 == True:
            cursor=con.cursor('Employee')
            eid =int(input(" Enter Employee id: "))
            name = input(" Enter Employee Name: ")
            salary = int(input(" Enter Employee salary: "))
            query = " insert into Employee values({}, '{}', {}) ".format(eid, name, salary)
            cursor.execute(query)
            con.commit()
            print("Data inserted successfully")
            b=input("Do you want to insert another Data..(Y/N)")
            if b == 'y' or b =='Y':
                flag1 =True
            else:
                flag1 =False
                #break

        print("Thank You For inserting Data")
        input1 = input("Do you want to continue to Opteration (Y/N:)")
        if input1== 'y' or input1=='Y':
            flag =True
        else:
            flag = False
    
    
    elif a == 2:
        while flag2 == True:
            cursor=con.cursor('Employee')
            value = int(input("Update value of:\n1) Employee ID \n2) Employee Name\n3) Employee Salary\nPlease select Above option: "))
            value1 = int(input("Update value by:\n1) Employee ID \n2) Employee Name\n3) Employee Salary\nPlease select Above option: "))
            if value <= 3 and value1 <= 3:
                if value == 1 and value1 == 1:
                    E_id = int(input("Enter Employee ID:"))
                    upE_id = int(input("Enter updated Employee ID:"))
                    query = "update Employee set E_id = {} where E_id = {}".format(upE_id,E_id)
                    cursor.execute(query)
                    con.commit()

                elif value == 1 and value1 == 2:
                    E_id = int(input("Enter Employee ID:"))
                    upE_Name = input("Enter updated Employee Name:")
                    query = "update Employee set E_Name = '{}' where E_id = {}".format(upE_Name,E_id)
                    cursor.execute(query)
                    con.commit()

                elif value == 1 and value1 == 3:
                    E_id = int(input("Enter Employee ID:"))
                    upE_salary = int(input("Enter updated Employee Salary:"))
                    query = "update Employee set E_salary = {} where E_id = {}".format(upE_salary,E_id)
                    cursor.execute(query)
                    con.commit()

                elif value == 2 and value1 == 1:
                    E_Name = input("Enter Employee Name:")
                    upE_id = int(input("Enter updated Employee ID:"))
                    query = "update Employee set E_id = {} where E_Name = '{}' ".format(upE_id,E_Name)
                    cursor.execute(query)
                    con.commit()

                elif value == 2 and value1 == 2:
                    E_Name = input("Enter Employee Name:")
                    upE_Name = input("Enter updated Employee ID:")
                    query = "update Employee set E_Name = '{}' where E_Name = '{}' ".format(upE_Name,E_Name)
                    cursor.execute(query)
                    con.commit()

                elif value == 2 and value1 == 3:
                    E_Name = input("Enter Employee Name:")
                    upE_salary = int(input("Enter updated Employee salary:"))
                    query = "update Employee set E_salary = {} where E_Name = '{}' ".format(upE_salary,E_Name)
                    cursor.execute(query)
                    con.commit()

                elif value == 3 and value1 == 1:
                    E_salary = int(input("Enter Employee Salary:"))
                    upE_id = int(input("Enter updated Employee ID:"))
                    query = "update Employee set E_id = {} where E_salary = {}".format(upE_id,E_salary)
                    cursor.execute(query)
                    con.commit()

                elif value == 3 and value1 == 2:
                    E_salary = int(input("Enter Employee Salary:"))
                    upE_Name = input("Enter updated Employee Name:")
                    query = "update Employee set E_Name = '{}' where E_salary = {}".format(upE_Name,E_salary)
                    cursor.execute(query)
                    con.commit()

                elif value == 3 and value1 == 3:
                    E_salary = int(input("Enter Employee Salary:"))
                    upE_salary = int(input("Enter updated Employee Salary:"))
                    query = "update Employee set E_salary = {} where E_salary = {}".format(upE_salary,E_salary)
                    cursor.execute(query)
                    con.commit()
                
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
            cursor=con.cursor('Employee')
            value3 = int(input("Delete data where:\n1) Employee ID \n2) Employee Name\n3) Employee Salary\nPlease select Above option: "))
            if value3 == 1:
                E_id = int(input("Enter Employee ID whose data you want to delete: "))
                query = 'delete from Employee where E_id = {}'.format(E_id)
                cursor.execute(query)
                con.commit()
                print("Data deleted successfully")
                c=input("Do you want to delete another Data..(Y/N)")
                if c == 'y' or c =='Y':
                    flag3 =True
                else:
                    flag3 =False

            elif value3 == 2:
                E_Name = input("Enter Employee Name whose data you want to delete: ")
                query = 'delete from Employee where E_Name = {}'.format(E_Name)
                cursor.execute(query)
                con.commit()
                print("Data deleted successfully")
                c=input("Do you want to delete another Data..(Y/N)")
                if c == 'y' or c =='Y':
                    flag3 =True
                else:
                    flag3 =False

            elif value3 == 3:
                E_salary = int(input("Enter Employee Salary whose data you want to delete: "))
                query = 'delete from Employee where E_salary = {}'.format(E_salary)
                cursor.execute(query)
                con.commit()
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