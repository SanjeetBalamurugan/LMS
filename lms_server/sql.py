import mysql.connector as scon

class SQL():
    def __init__(self, user, passwd, host, database):
        try:
            self.conn = scon.connect(user=user, password=passwd, host=host, database=database)
        except scon.Error as err:
            if err.errno == scon.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == scon.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def query_books(self):
        cur = self.conn.cursor()
        result = cur.execute("SELECT * FROM books;")
        rows = cur.fetchall()
        print(type(rows))
        for row in rows:
            print(row)

        books = dict()
        for row in rows:
            book = {
                    'id': row[0],
                    'name':row[1],
                    'price':row[2]
                    }
            books[row[0]] = book
        return books

    def __del__(self):
        self.conn.close()
