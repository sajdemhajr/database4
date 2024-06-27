import mysql.connector
import csv

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "N@srin_1382"
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
    password="N@srin_1382",
    database = "db_class"
)
mycursor = mydb.cursor()

#CREATE_TABLE_PHOTOGRAFERS
query = ("""CREATE TABLE photographers (
    code VARCHAR(50) ,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) ,
    bio TEXT,
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
    FOREIGN KEY (photographer_code) REFERENCES photographers(code)
)
"""
try:
    mycursor.execute(query)
except Exception as e:
    print(e)

#CREATE_TABLE_WRITERS
query = ("""CREATE TABLE Writers (
    code VARCHAR(50) ,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) ,
    bio TEXT,
    PRIMARY KEY(code)
)
""")
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
    FOREIGN KEY (writer_code) REFERENCES Writers(code)
)
""")
try:
    mycursor.execute(query)
except Exception as e:
    print(e)


#INSERT_TO_PHOTOGRAPHERS
def insert_photographer(code, name, email, bio):
    try:
        mycursor.execute(
            "INSERT INTO photographers (code, name, email, bio) VALUES (%s, %s, %s, %s) "
            "ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), bio=VALUES(bio)",
            (code, name, email, bio)
        )
        print(f"Inserted/Updated: {code}, {name}, {email}, {bio}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


#READ_FROM_CSV_FILE
try:
    with open('images.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_photographer(
                row['photographer_code'],
                row['photographer_name'],
                row['photographer_email'],
                None  
            )
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"Error reading CSV file: {e}")

try:
    mydb.commit()
    print("Changes committed successfully.")
except mysql.connector.Error as err:
    print(f"Error committing changes: {err}")



#INSERT_TO_WRITER
def insert_writer(code, name, email, bio):
    try:
        mycursor.execute(
            "INSERT INTO writers (code, name, email, bio) VALUES (%s, %s, %s, %s) "
            "ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), bio=VALUES(bio)",
            (code, name, email, bio)
        )
    except mysql.connector.Error as err:
        print(err)


#READ_FROM_CSV_FILE
try:
    with open('articles.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_writer(
                row['writer_code'],
                row['writer_name'],
                row['writer_email'],
                None 
            )
except Exception as e:
    print(e)

try:
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

#CLOSE_DATABASE
mycursor.close()
mydb.close()