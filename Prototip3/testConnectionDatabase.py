from dataclasses import dataclass, asdict
import hashlib
from flask import jsonify
import mysql.connector
from time import time
import random

class UserDAO:
    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection

    def login(self, identifier, password):
        #connect to database
        con=self.connectBBDD()
        cursor=con.cursor(dictionary=True)
        query = """
        SELECT * FROM User
        WHERE (username = %s OR email = %s)
        """
        cursor.execute(query,(identifier, password))
        user=cursor.fetchone()
        cursor.close()
        con.close()
        return user
    


    def setTokenUser(self, username):
        #connect to database
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        # generate token
        token = self.getHash(username)
        # update a BBDD camp token with the generated token
        query = "UPDATE User SET token ='"  + token + "' WHERE username = '" + username
        print(query)
        cursor.execute(query)
        # close connection
        cursor.close()
        con.close()

    def getHash(self, username):
        miliseconds = str(time() * 1000)
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()

"""     def getHash(self, username):
        miliseconds = str(time() * random.randrange(100000))
        data = miliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()
 """


dao=UserDAO() 
print(dao.getHash("user1"))

u=dao.login("dasdad","mare")
print(u)




miliseconds = str(time()*1000)
print("Time in miliseconds since epoch:", miliseconds)
data = "Hola mundo "+miliseconds
print(data)

# 2. Crear el objeto hash SHA-256 y actualizarlo con los datos
hash_object = hashlib.sha256(data.encode('utf-8'))
#3. Obtener el resultado en formato hexadecimal
token = hash_object.hexdigest()
print(token)