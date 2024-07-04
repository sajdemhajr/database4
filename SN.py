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





class User:
    def __init__(self, code, name, email):
        self.code = code
        self.name = name
        self.email = email

    def __str__(self):
        return f"code: {self.code}, name: {self.name}, email: {self.email}"

class Image:
    def __init__(self, image_path, title, tags, description, category, photographer_code, photographer_name, photographer_email):
        self.image_path = image_path
        self.title = title
        self.tags = tags
        self.description = description
        self.category = category
        self.photographer_code = photographer_code
        self.photographer_name = photographer_name
        self.photographer_email = photographer_email

    def __str__(self):
        return f"path: {self.image_path}, title: {self.title}, tags: {self.tags}, description: {self.description}, category: {self.category}"

class Article:
    def __init__(self, content, keywords, title, category, writer_code, writer_name, writer_email):
        self.content = content
        self.keywords = keywords
        self.title = title
        self.category = category
        self.writer_code = writer_code
        self.writer_name = writer_name
        self.writer_email = writer_email

    def __str__(self):
        return f"title: {self.title}, content: {self.content}, keywords: {self.keywords}, category: {self.category}"

class Database:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connect = None

    def connection(self):
        self.connect = mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            database = self.database
        )

    def execute_query(self, query, data=None, fetch=False):
        try:
            self.connect = self.connection()
            mycursor = self.connect.cursor()
            mycursor.execute(query, data)
            if fetch:
                return mycursor.fetchall()
            self.connect.commit()
        except Exception as e:
            print(e)
        finally:
            mycursor.close()
            self.connect.close()

    def add_user(self, user):
        try:
            self.execute_query("SELECT COUNT(*) FROM users WHERE code = %s", (user.code))
            result = mycursor.fetchone()
            if result[0] == 0:
                query = "INSERT INTO users (code, name, email) VALUES (%s, %s, %s)"
                data = (user.code, user.name, user.email)
                self.execute_query(query, data)
        except Exception as e:
            print(e)
    

    def add_image(self, image):
        try:
            self.execute_query("SELECT COUNT(*) FROM images WHERE image_path = %s", (image.image_path,))
            result = mycursor.fetchone()
            if result[0] == 0:
                query = """INSERT INTO images (image_path, title, tags, description, category, photographer_code, photographer_name, photographer_email)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                data = (image.image_path, image.title, image.tags, image.description, image.category, image.photographer_code, image.photographer_name, image.photographer_email)
                self.execute_query(query, data)
        except Exception as e:
            print(e)
        

    def add_article(self, article):
        try:
            self.execute_query("SELECT COUNT(*) FROM articles WHERE content = %s", (article.content))
            result = mycursor.fetchone()
            if result[0] == 0:
                query = """INSERT INTO articles (content, keywords, title, category, writer_code, writer_name, writer_email)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                data = (article.content, article.keywords, article.title, article.category, article.writer_code, article.writer_name, article.writer_email)
                self.execute_query(query, data)
        except Exception as e:
           print(e)


    def list_users(self):
        query = "SELECT * FROM users"
        return self.execute_query(query, fetch=True)

    def list_images(self):
        query = "SELECT * FROM images"
        return self.execute_query(query, fetch=True)

    def list_articles(self):
        query = "SELECT * FROM articles"
        return self.execute_query(query, fetch=True)

    def remove_user(self, code):
        query = "DELETE FROM users WHERE code=%s"
        data = (code,)
        self.execute_query(query, data)

    def remove_image(self, image_path):
        query = "DELETE FROM images WHERE image_path=%s"
        data = (image_path,)
        self.execute_query(query, data)

    def remove_article(self, content):
        query = "DELETE FROM articles WHERE content=%s"
        data = (content,)
        self.execute_query(query, data)
        
if __name__ == "__main__":
    db = Database("root", "S@jedeh_1382", "localhost", "db_class")
    #READ_FROM_ARTICLES_CSV_FILE
    with open('articles.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_user = User(
                row['writer_code'],
                row['writer_name'],
                row['writer_email']
            )
            db.add_user(new_user)   
            new_article = Article(
                row['content'],
                row['keywords'],
                row['title'],
                row['category'],
                row['writer_code'],
                row['writer_name'],
                row['writer_email']
            )
            db.add_article(new_article)
    #READ_FROM_IMAGES_CSV_FILE
    with open('images.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_user = User(
                row['photographer_code'],
                row['photographer_name'],
                row['photographer_email']
            )
            db.add_user(new_user)
            new_image = Image(
                row['image_path'],
                row['title'],
                row['tags'],
                row['description'],
                row['category'],
                row['photographer_code'],
                row['photographer_name'],
                row['photographer_email']
            )
            db.add_image(new_image)