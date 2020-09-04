import mysql.connector

class Connection:
    #constructor
    def __init__(self):
        # to access database / to connect database for use
        self._my_connection = mysql.connector.connect(user='root', password='',
                                                     host='localhost', database='es19a', port='3306')
        # to execute queries
        self._my_cursor = self.my_connection.cursor()
    def insert_update_delete(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
    def select(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data
    def select_p(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchall()
        return data

class Schedule(Connection):
    # c = Connection()
    def __init__(self):
        super().__init__()
        # self.c = Connection()
    def add_schedule(self):
        qry = "INSERT INTO schedule (timing, rate, status) VALUES (%s, %s, %s)"
        values = ('7-8', 1500, 'Active')
        self.insert_update_delete(qry, values)
    def update_schedule(self):
        qry = "UPDATE schedule SET timing = %s, rate = %s, status = %s WHERE id = %s"
        values = ('8-9', 1400, 'Inactive', 1)
        self.insert_update_delete(qry, values)
    def delete_schedule(self):
        qry = "DELETE FROM schedule WHERE id = %s"
        values = (1,)
        self.insert_update_delete(qry, values)
    def show_schedule(self):
        qry = "SELECT * FROM schedule"
        return self.select(qry)
    def search_schedule(self):
        qry = "SELECT * FROM schedule WHERE timing = %s"
        values = ('7-8',)
        return self.select_p(qry, values)

class staff:
    def __init__(self):
        self.username = un
        self.password = pw

    def username_staff(self):
        qry = "INSERT INTO staff (username) VALUES (%s)"
        values = ('Ram',)
        self.insert_username_staff(qry, values)

    def password_staff(self):
        qry = "INSERT INTO staff (password) VALUES (%s)"
        values = ('------',)
        self.insert_password_staff(qry, values)

    def type_staff(self):
        qry = "INSERT INTO staff (username) VALUES (%s)"
        values = ('Ram',)
        self.insert_username_staff(qry, values)


