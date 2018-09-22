import pymysql


class Database:

    host = 'dbgrasshopper.cnh5suc8nb8k.us-east-1.rds.amazonaws.com'
    user = 'admin'
    password = 'D!i9m9o)N'
    db = 'spiderDb'


spiderDbConnection = pymysql.connect(host="spiderdb.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="D!i9m9o)N",  database="spiderDb")
spiderDbCursor = spiderDbConnection.cursor()

query_create = """CREATE TABLE customers (name VARCHAR(255), age int)"""


spiderDbCursor.execute(query_create)


query = """
        INSERT INTO customers
        (`name`, `age`)
        VALUES
        ('Mike', 21),
        ('Michael', 21),
        ('Imran', 21)
        """


spiderDbCursor.execute(query)

select_query = """
        SELECT * FROM customers
        WHERE age = 21
        """

spiderDbCursor.execute(select_query)

for person in spiderDbCursor:
        print(person)

spiderDbCursor.close()
spiderDbConnection.close()

