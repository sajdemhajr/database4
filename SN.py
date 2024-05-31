import mysql.connector
class DB:
    def __init__(self, user, password, host, datbase):
        self.user = user
        self.password = password
        self.host = host
        self.database = datbase
        self.connect = None

    def connection(self):
        self.connect = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host = self.host,
            database = self.database,
        )
  if __name__ == "__main__":
    obj1 = DB("root","pass","localhost","DBblog")
