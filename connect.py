import mysql.connector as c
con = c.connect(host = 'localhost', user = 'root', password = '914206', database = 'Onkar')
if con.is_connected():
    print('mysql successfully connected')
else:
    print('some connectivity issue')