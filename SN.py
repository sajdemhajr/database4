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