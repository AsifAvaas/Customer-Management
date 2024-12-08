import mysql.connector


dataBase=mysql.connector.connect(
    host= 'localhost',
    user='root',
    passwd = 'mysql123'
    ) 

cursorObject= dataBase.cursor()

cursorObject.execute("CREATE DATABASE customar_management")


print("All done")