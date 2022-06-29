from sqlite3 import connect
import pymysql
import dbconfig


class DBhelper():

    def connect(self, database = "crimemap"):
        return pymysql.connect(host = "localhost",
                                user = dbconfig.db_user,
                                passwd=dbconfig.db_password,
                                db=database)

    def getAllInputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def addInput(self, data):
        connection = self.connect()
        try:
            #This following inroduces a delibrate security flas
            query = "INSERT INTO crimes (description) VALUES ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
    
    def clearAll(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()