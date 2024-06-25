import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "S@jedeh_1382"
)
mycursor = mydb.cursor()
try:
    mycursor.execute()
except Exception as e:
    print(e)
sj = "CREATE DATABASE db_class"
try:
    mycursor.execute(sj)
except Exception as e :
    print(e)