import praw

reddit = praw.Reddit(client_id='8WsvZGB6mbj7sw',
                     client_secret='h9rf_2wMOecGsvUrCbf7QUfCDq0',
                     password='255255',
                     user_agent='testscript by /u/grasshopper_api',
                     username='grasshopper_api')

appended_data = []

subreddit = reddit.subreddit('worldnews')

top_python = subreddit.top(limit=10)
for submission in top_python:
    if not submission.stickied:
        appended_data.append(submission.selftext)

print(appended_data)