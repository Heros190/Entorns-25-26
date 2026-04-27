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
    
    def getUserByToken(self, token):
         #connect to database
        con=self.connectBBDD()
        cursor=con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token = '" + token + "'"
        cursor.execute(query)
        user=cursor.fetchone()
        cursor.close()
        con.close()
        return user
    

    def login(self, identifier, password):
        #connect to database
        con=self.connectBBDD()
        cursor=con.cursor(dictionary=True)
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query,(identifier, identifier, password))
        user=cursor.fetchone()
        token=""
        if user:
            token = self.setTokenUser(user["username"])
            print(user)
            user['token'] = token
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
        print(type(token))
        query = "UPDATE User SET token = %s WHERE username = %s"
        print(query)
        cursor.execute(query, (token, username))
        con.commit()
        # close connection
        cursor.close()
        con.close()
        return token
    
    def getHash(self, username):
        miliseconds = str(time() * 1000)
        data = username + miliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""

    def getHash2(self, username):
        miliseconds = str(time() * random.randrange(100000))
        data = miliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""
 


dao=UserDAO() 

u=dao.getUserByToken("ba467e9ba69df8fc1ec5df681ab8024e19b0b57e68714281d1e4712772bd30c2")
print(u)

u=dao.getUserByToken("a")
print(u)