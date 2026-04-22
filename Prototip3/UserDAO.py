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
print(dao.getHash("user1"))

u=dao.login("mare","mare")
print(u)




'''miliseconds = str(time()*1000)
print("Time in miliseconds since epoch:", miliseconds)
data = "Hola mundo "+miliseconds
print(data) 

# 2. Crear el objeto hash SHA-256 y actualizarlo con los datos
hash_object = hashlib.sha256(data.encode('utf-8'))
#3. Obtener el resultado en formato hexadecimal
token = hash_object.hexdigest()
print(token) '''



#Cliente
# DAOclient --> login(username, password) --> webservice
#webservice --loginOK = token --> DAOclient
#DAOclient -->/getChildren(token) --> webservice
#webservice --> json(childrenList) --> DAOclient