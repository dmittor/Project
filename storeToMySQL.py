import pymysql


class Database:

    host = 'spiderdb.cnh5suc8nb8k.us-east-1.rds.amazonaws.com'
    user = 'admin'
    password = 'D!i9m9o)N'
    db = 'spiderDb'


spiderDbConnection = pymysql.connect(host="spiderdb.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="D!i9m9o)N",  database="spiderDb")
spiderDbCursor = spiderDbConnection.cursor()


query = """
        INSERT INTO spiderDb
        (`name`, `age`)
        VALUES
        ('Mike', 21),
        ('Michael', 21),
        ('Imran', 21)
        """


spiderDbCursor.execute(query)

select_query = """
        SELECT * FROM spiderDb
        WHERE age = 21
        """

spiderDbCursor.execute(select_query)

for person in spiderDbCursor:
        print ("Found %s " % person['name'])
