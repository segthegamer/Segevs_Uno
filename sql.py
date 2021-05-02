import sqlite3

class Users:
    """Creates database with users table includes:
       create query
       insert query
       select query
    """

    def __init__(self, tablename="users", userId="userId", password="password", username="username"):
        self.__tablename = tablename
        self.__userId = userId
        self.__password = password
        self.__username = username
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        query_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(" + self.__userId + " " + \
                    " INTEGER PRIMARY KEY AUTOINCREMENT ,"
        query_str += " " + self.__password + " TEXT    NOT NULL ,"
        query_str += " " + self.__username + " TEXT    NOT NULL );"

        # conn.execute("drop table users")
        conn.execute(query_str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        return self.__tablename

    def insert_user(self, username, password):
        conn = sqlite3.connect('test.db')
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__username + "," + self.__password + ") VALUES " \
                                                                                                            "(" + "'" + username + "'" + "," + "'" + password + "'" + ");"
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def delete_user(self,id):
        conn = sqlite3.connect('test.db')

        delete_query = "DELETE FROM " + self.get_table_name() + " WHERE " + self.__userId+ " = " + str(id)
        print(delete_query)
        conn.execute(delete_query)
        conn.commit()
        conn.close()
        print("record has been deleted")

    def Update_user_username(self, id1, username):
        conn = sqlite3.connect('test.db')

        update_query = "UPDATE " + self.get_table_name() + " SET "\
                       + self.__password + " = " + "\' " +str(username)+" \' " + " WHERE " + self.__userId + " = " + str(id1)+";"
        print(update_query)
        conn.execute(update_query)
        conn.commit()
        conn.close()
        print("record has been updated")

    def Update_user_password(self, id1, password):
        conn = sqlite3.connect('test.db')

        update_query = "UPDATE " + self.get_table_name() + " SET "\
                       + self.__username + " = " + "\' " +str(password)+" \' " + " WHERE " + self.__userId + " = " + str(id1)+";"
        print(update_query)
        conn.execute(update_query)
        conn.commit()
        conn.close()
        print("record has been updated")

    def select_user_by_id(self, userId):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select * from users;"

        """strsql = "SELECT userId, username, password  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(userId)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("userId = ", row[0])
            print("username = ", row[1])
            print("password = ", row[2])

        print("Operation done successfully")
        conn.close()


u = Users()

u.insert_user(input("Please input username"), input("Please input password"))
u.insert_user(input("Please input username"), input("Please input password"))
u.insert_user(input("Please input username"), input("Please input password"))
u.insert_user(input("Please input username"), input("Please input password"))

id = ""

while type(id) != int:
    try:
        id = int(input("Please input id"))
    except:
        print("Please enter a number")

u.delete_user(id)

id1 = ""
while type(id1) != int:
    try:
        id1 = int(input("Please input id"))
    except:
        print("Please enter a number")

username = input("Please input your new name")
u.Update_user_username(id1,username)

id2 = ""
while type(id2) != int:
    try:
        id2 = int(input("Please input id"))
    except:
        print("Please enter a number")

password = input("Please input your new name")
u.Update_user_password(id2,password)

u.select_user_by_id(1)