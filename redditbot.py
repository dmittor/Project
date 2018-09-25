import praw

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



subreddit = reddit.subreddit('worldnews')



top_python = subreddit.top(limit=5)
for submission in top_python:
    if not submission.stickied:

        id_submission_array.append(submission.id)
        author_submission_array.append(submission.author)
        num_comments_submission_array.append(submission.num_comments)
        permalink_submission_array.append(submission.permalink)
        score_submission_array.append(submission.score)
        title_submission_array.append(submission.title)
        over_18_submission_array.append(submission.over_18)
        upvote_ratio_submission_array.append(submission.upvote_ratio)

        url_submission_array.append(submission.url)

    str1 = ''.join(str(e) for e in list1)




    redditDbConnection = pymysql.connect(host="dbgrasshopper.cnh5suc8nb8k.us-east-1.rds.amazonaws.com", user="admin",  passwd="K!u2Z(z0",  database="dbGrasshopper")
    redditDbCursor = redditDbConnection.cursor()

    query_create = """CREATE TABLE redditRworldnews (name VARCHAR(255), age int)"""


    redditDbCursor.execute(query_create)


    query = """
        INSERT INTO customers
        (`name`, `age`)
        VALUES
        ('Mike', 21),
        ('Michael', 21),
        ('Imran', 21)
        """


    redditDbCursor.execute(query)

    select_query = """
        SELECT * FROM customers
        WHERE age = 21
        """

    redditDbCursor.execute(select_query)

    for person in redditDbCursor:
        print(person)

    redditDbCursor.close()
    redditDbConnection.close()






print(id_submission_array)
print(author_submission_array)
print(num_comments_submission_array)
print(permalink_submission_array)
print(url_submission_array)
print(score_submission_array)
print(title_submission_array)
print(over_18_submission_array)
print(upvote_ratio_submission_array)
