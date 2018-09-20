import praw

reddit = praw.Reddit(client_id='81r5TPtAXFF5MA',
                     client_secret='8VwXqSQHgNvpNLzZbE30iSUppvo',
                     password='255255',
                     user_agent='testscript by /u/grasshopper_api',
                     username='grasshopper_api')


print(reddit.auth.scopes())