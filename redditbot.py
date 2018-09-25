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



top_python = subreddit.top(limit=5)
for submission in top_python:
    if not submission.stickied:

        L.append(submission.id)
        L.append(submission.author)
        L.append(submission.num_comments)
        L.append(submission.permalink)
        L.append(submission.score)
        L.append(submission.title)
        L.append(submission.over_18)
        L.append(submission.upvote_ratio)
        L.append(submission.url)

        makeitastring = ','.join(map(str, L))
        insert_row.append("(%)"%makeitastring)


redditDbConnection = pymysql.connect(host="dbgrasshopper.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="K!u2Z(z0",  database="dbGrasshopper")
redditDbCursor = redditDbConnection.cursor()

query_create = """CREATE TABLE redditRworldnews ( intsubmission_id VARCHAR(255),
submission_author VARCHAR(255),
submission_num_comments int,
submission_permalink VARCHAR(255),
submission_score int,
submission_title VARCHAR(255),
submission_over_18 VARCHAR(255),
submission_upvote_ratio float,
submission_url VARCHAR(255))"""


redditDbCursor.execute(query_create)


query = """
        INSERT INTO redditRworldnews
        (`name`, `age`)
        VALUES
        %
        """%(','.join(map(str, insert_row)))



redditDbCursor.execute(query)

select_query = """
        SELECT * FROM redditRworldnews
        """

redditDbCursor.execute(select_query)

for row in redditDbCursor:
        print(row)

redditDbCursor.close()
redditDbConnection.close()



