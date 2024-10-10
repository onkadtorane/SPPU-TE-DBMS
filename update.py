import mysql.connector as c
con = c.connect(host = 'localhost', user = 'root', password = '914206', database = 'Onkar')
cursor = con.cursor()
Mark = int(input(" Enter updated Marks :"))
Roll_no =int(input(" Enter Student Rollno :"))
query = 'update Student set Mark = {} where Roll_no = {}'.format(Mark, Roll_no)
cursor.execute(query)
con.commit()
print("Successfully Updated Mark")