import pymysql


class Database:


    spiderDbConnection = pymysql.connect(host="dbgrasshopper.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="K!u2Z(z0",  database="dbGrasshopper")
    spiderDbCursor = spiderDbConnection.cursor()

# query_create = """CREATE TABLE customers (name VARCHAR(255), age int)"""


# spiderDbCursor.execute(query_create)


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

