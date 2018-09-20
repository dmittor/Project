import praw

reddit = praw.Reddit(client_id='81r5TPtAXFF5MA',
                     client_secret='8VwXqSQHgNvpNLzZbE30iSUppvo',
                     password='255255',
                     user_agent='testscript by /u/grasshopper_api',
                     username='grasshopper_api')


submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')
for top_level_comment in submission.comments:
    print(top_level_comment.body)