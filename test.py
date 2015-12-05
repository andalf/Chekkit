import sys

# pip install praw
import praw

# pip install pprintpp and pip install pp-ez
import pp

# output version of python. We are assuming version 3.
pp(sys.version)

# connect to Reddit as Chekkit
r = praw.Reddit(user_agent='chekkit')

#lets user choose subreddit
subReddit = input("What Subreddit would you like to use?")

# get 5 most recent from the subReddit 'opensource'
submissions = r.get_subreddit(subReddit).get_hot(limit=5)

# print out the output
pp([str(x) for x in submissions])