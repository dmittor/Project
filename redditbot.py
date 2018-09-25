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

        makeitastring = "'%s','%s',%d,'%s',%d,'%s','%s',%f,'%s'" % (submission.id,submission.author,submission.num_comments,submission.permalink,submission.score,submission.title,submission.over_18,submission.upvote_ratio,submission.url)
        # print(makeitastring)
        insert_row.append('(' + makeitastring + ')')

print(insert_row)
redditDbConnection = pymysql.connect(host="dbgrasshopper.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="K!u2Z(z0",  database="dbGrasshopper")
redditDbCursor = redditDbConnection.cursor()


query_create = """DROP TABLE redditRworldnews """

try:
    redditDbCursor.execute(query_create)
except pymysql.InternalError as error:
    print('Got error {!r}, errno is {}'.format(error, error.args[0]))


query_create = """CREATE TABLE redditRworldnews ( submission_id VARCHAR(255),submission_author VARCHAR(255), submission_num_comments int, submission_permalink VARCHAR(255),submission_score int, submission_title VARCHAR(512),submission_over_18 VARCHAR(255),submission_upvote_ratio float, submission_url VARCHAR(512))"""
print(query_create)
try:
    redditDbCursor.execute(query_create)
except pymysql.InternalError as error:
    print('Got error {!r}, errno is {}'.format(error, error.args[0]))

query = """INSERT INTO redditRworldnews (submission_id, submission_author, submission_num_comments,submission_permalink, submission_score, submission_title, submission_over_18, submission_upvote_ratio, submission_url)
        VALUES"""+(','.join(map(str, insert_row)))
print(query)

try:
    redditDbCursor.execute(query)
except pymysql.InternalError as error:
    print('Got error {!r}, errno is {}'.format(error, error.args[0]))

select_query = """
        SELECT * FROM redditRworldnews
        """
try:
    redditDbCursor.execute(select_query)
except pymysql.InternalError as error:
    print('Got error {!r}, errno is {}'.format(error, error.args[0]))
print ('-----------------------------------------------------------')
for row in redditDbCursor:
        print(row)

redditDbCursor.close()
redditDbConnection.close()



