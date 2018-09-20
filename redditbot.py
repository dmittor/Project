import praw

reddit = praw.Reddit(client_id='81r5TPtAXFF5MA',
                     client_secret='8VwXqSQHgNvpNLzZbE30iSUppvo',
                     password='1guiwevlfo00esyy:955413',
                     user_agent='testscript by /u/grasshopper_api',
                     username='255255')

print(reddit.auth.scopes())