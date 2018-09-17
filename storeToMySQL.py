import MySQLdb


class Database:

    host = 'spiderdb.cnh5suc8nb8k.us-east-1.rds.amazonaws.com'
    user = 'admin'
    password = 'D!i9m9o)N'
    db = 'spiderDb'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":

    db = Database()

    #CleanUp Operation
    del_query = "DELETE FROM spiderDb"
    db.insert(del_query)

    # Data Insert into the table
    query = """
        INSERT INTO spiderDb
        (`name`, `age`)
        VALUES
        ('Mike', 21),
        ('Michael', 21),
        ('Imran', 21)
        """

    # db.query(query)
    db.insert(query)

    # Data retrieved from the table
    select_query = """
        SELECT * FROM spiderDb
        WHERE age = 21
        """

    people = db.query(select_query)

    for person in people:
        print ("Found %s " % person['name'])