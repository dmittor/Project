import praw
import pymysql

reddit = praw.Reddit(client_id='8WsvZGB6mbj7sw',
                     client_secret='h9rf_2wMOecGsvUrCbf7QUfCDq0',
                     password='255255',
                     user_agent='testscript by /u/grasshopper_api',
                     username='grasshopper_api')

insert_row = []

subreddit = reddit.subreddit('worldnews')



top_python = subreddit.top(limit=1)
for submission in top_python:
    if not submission.stickied:

        row_string = "'%s','%s',%d,'%s',%d,'%s','%s',%f,'%s'" % (submission.id,submission.author,submission.num_comments,submission.permalink,submission.score,submission.title.replace("'", "\\'"),submission.over_18,submission.upvote_ratio,submission.url)

        insert_row.append('(' + row_string + ')')


redditDbConnection = pymysql.connect(host="dbgrasshopper.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="K!u2Z(z0",  database="dbGrasshopper")
redditDbCursor = redditDbConnection.cursor()



query = """REPLACE INTO redditRworldnews (submission_id, submission_author, submission_num_comments,submission_permalink, submission_score, submission_title, submission_over_18, submission_upvote_ratio, submission_url)
        VALUES"""+(','.join(map(str, insert_row)))


try:
    redditDbCursor.execute(query)
except pymysql.InternalError as error:
    print('Got error {!r}, errno is {}'.format(error, error.args[0]))
print ('-----------------------------------------------------------')
redditDbConnection.commit()
select_query = """
        SELECT * FROM redditRworldnews
        """
try:
    redditDbCursor.execute(select_query)
except pymysql.InternalError as error:
    print('Got error {!r}, errno is {}'.format(error, error.args[0]))

for row in redditDbCursor:
        print(row)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

redditDbCursor.close()
redditDbConnection.close()



