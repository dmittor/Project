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
is_video_submission_array = []


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
        is_video_submission_array.append(submission.id)
        url_submission_array.append(submission.url)




print(id_submission_array)
print(author_submission_array)
print(num_comments_submission_array)
print(permalink_submission_array)
print(url_submission_array)
print(score_submission_array)
print(title_submission_array)
print(over_18_submission_array)
print(upvote_ratio_submission_array)
print(is_video_submission_array)