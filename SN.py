import mysql.connector
import csv

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

#CERATE_DATABASE
sj = "CREATE DATABASE db_class"
try:
    mycursor.execute(sj)
except Exception as e :
    print(e)

#CONNECT_TO_DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S@jedeh_1382",
    database = "db_class"
)
mycursor = mydb.cursor()

#CREATE_TABLE_USERS
query = ("""CREATE TABLE users (
    code VARCHAR(50) ,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) ,
    PRIMARY KEY(code)
)
""")
try:
    mycursor.execute(query)
except Exception as e:
    print(e)

#CREATE_TABLE_IMAGES
query = """CREATE TABLE Images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_path VARCHAR(255) NOT NULL,
    title VARCHAR(100),
    tags VARCHAR(255),
    description TEXT,
    category VARCHAR(50),
    photographer_code VARCHAR(50) NOT NULL,
    photographer_name VARCHAR(100),
    photographer_email VARCHAR(100),
    FOREIGN KEY (photographer_code) REFERENCES users(code)
)
"""
try:
    mycursor.execute(query)
except Exception as e:
    print(e)

#CREATE_TABLE_ARTICLES
query = ("""CREATE TABLE Articles (
    content TEXT NOT NULL,
    keywords VARCHAR(255),
    title VARCHAR(100),
    category VARCHAR(50),
    writer_code VARCHAR(50) NOT NULL,
    writer_name VARCHAR(100),
    writer_email VARCHAR(100),
    FOREIGN KEY (writer_code) REFERENCES users(code)
)
""")
try:
    mycursor.execute(query)
except Exception as e:
    print(e)


#INSERT_TO_users
def insert_photographer(code, name, email):
    try:
        mycursor.execute(
            "INSERT INTO users (code, name, email) VALUES (%s, %s, %s) "
            "ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email)",
            (code, name, email)
        )
        #print(f"Inserted/Updated: {code}, {name}, {email}")
    except Exception as e:
        print(e)


#READ_FROM_CSV_FILE
try:
    with open('images.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_photographer(
                row['photographer_code'],
                row['photographer_name'],
                row['photographer_email'], 
            )
except Exception as e:
    print(e)
else:
      mydb.commit()



#INSERT_TO_WRITER
def insert_writer(code, name, email):
    try:
        mycursor.execute(
            "INSERT INTO users (code, name, email) VALUES (%s, %s, %s) "
            "ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email)",
            (code, name, email)
        )
    except Exception as e:
        print(e)


#READ_FROM_CSV_FILE
try:
    with open('articles.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_writer(
                row['writer_code'],
                row['writer_name'],
                row['writer_email']
            )
except Exception as e:
    print(e)

try:
    mydb.commit()
except Exception as e:
    print(e)

#CLOSE_DATABASE
mycursor.close()
mydb.close()