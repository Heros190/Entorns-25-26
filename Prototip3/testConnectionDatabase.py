from dataclasses import dataclass, asdict
import hashlib
from flask import jsonify
import mysql.connector


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
        # update a BBDD camp token with the generated token
        # close connection
        cursor.close()
        con.close()

        def getHash(self, username):
            miliseconds = str(time()*1000)
            hash_object = hashlib.sha256(data.encode('utf-8'))
            return hash_object.hexdigest()




dao=UserDAO() 
u=dao.login("mare","mare")
print(u)

u=dao.login("dasdad","mare")
print(u)



from time import time
miliseconds = str(time()*1000)
print("Time in miliseconds since epoch:", miliseconds)
data = "Hola mundo "+miliseconds
print(data)

# 2. Crear el objeto hash SHA-256 y actualizarlo con los datos
hash_object = hashlib.sha256(data.encode('utf-8'))
#3. Obtener el resultado en formato hexadecimal
token = hash_object.hexdigest()
print(token)