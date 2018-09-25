import praw
import pymysql

reddit = praw.Reddit(client_id='8WsvZGB6mbj7sw',
                     client_secret='h9rf_2wMOecGsvUrCbf7QUfCDq0',
                     password='255255',
                     user_agent='testscript by /u/grasshopper_api',
                     username='grasshopper_api')


id_submission_array = []
author_submission_array = []
num_comments_submission_array = []
permalink_submission_array = []
url_submission_array = []
score_submission_array = []
title_submission_array = []
over_18_submission_array = []
upvote_ratio_submission_array = []
L = []
insert_row = []

subreddit = reddit.subreddit('worldnews')



top_python = subreddit.top(limit=2)
for submission in top_python:
    if not submission.stickied:

        L.append('1')
        L.append('2')
        L.append('3')
        L.append('4')
        L.append('5')
        L.append('6')
        L.append('7')
        L.append('8')
        L.append('9')

        makeitastring = ','.join(map(str, L))

        insert_row.append('(' + makeitastring + ')')


redditDbConnection = pymysql.connect(host="dbgrasshopper.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="K!u2Z(z0",  database="dbGrasshopper")
redditDbCursor = redditDbConnection.cursor()


query_create = """DROP TABLE redditRworldnews """

try:
    redditDbCursor.execute(query_create)
except MySQLError as e:
    print('Got error {!r}, errno is {}'.format(e, e.args[0]))

query_create = """CREATE TABLE redditRworldnews ( submission_id VARCHAR(255),
submission_author VARCHAR(255),
submission_num_comments int,
submission_permalink VARCHAR(255),
submission_score int,
submission_title VARCHAR(255),
submission_over_18 VARCHAR(255),
submission_upvote_ratio float,
submission_url VARCHAR(512))"""


redditDbCursor.execute(query_create)


query = """
        INSERT INTO redditRworldnews
        (submission_id, submission_author, submission_num_comments,submission_permalink, submission_score, submission_title, submission_over_18, submission_upvote_ratio, submission_url)
        VALUES
        """+(','.join(map(str, insert_row)))



redditDbCursor.execute(query)

select_query = """
        SELECT * FROM redditRworldnews
        """

redditDbCursor.execute(select_query)

for row in redditDbCursor:
        print(row)

redditDbCursor.close()
redditDbConnection.close()



