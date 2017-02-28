#!/usr/bin/python
import praw
import pdb
import re
import os

reddit = praw.Reddit('glassbot')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('highqualityglass')
for submission in subreddit.hot(limit=10):

    if submission.id not in posts_replied_to:

        submission.reply("Hey man, that's some smooth looking glass. Really Jealous!")
        print("Bot replying to : ", submission.title)

        posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
