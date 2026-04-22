import mysql.connector

class ChildDAO:

    def connectBBDD(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )

    # -------------------------
    # GET CHILDS BY USER
    # -------------------------
    def getChilds(self, user):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = "SELECT * FROM Child WHERE user_id = %s"
        cursor.execute(query, (user["id"],))

        childs = cursor.fetchall()

        cursor.close()
        con.close()

        return childs