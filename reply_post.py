#!/usr/bin/python
import praw
import pdb
import re
import os
from urllib import urlopen
from random import randint

reddit = praw.Reddit('glassbot')
RAWINPUT = "http://pastebin.com/raw/grKs4cDu"

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
        f = urlopen(RAWINPUT)
        f = f.read()
        f = f.split('$$$')
        submission.reply(f[randint(0, len(f)-1)])
        print(f[randint(0, len(f)-1)])
        print("Bot replying to : ", submission.title)

        posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
