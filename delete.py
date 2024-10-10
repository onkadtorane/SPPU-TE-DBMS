import mysql.connector as c
con = c.connect(host = 'localhost', user = 'root', password = '914206', database = 'Onkar')

cursor = con.cursor()
Roll_no = int(input("Enter Student Rollno :"))
query = 'delete from Student where Roll_no = {}'.format(Roll_no)
cursor.execute(query)
con.commit()
print("Successfully Delete Data")