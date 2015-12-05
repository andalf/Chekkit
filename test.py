import praw
import sys
import pp

pp(sys.version)
subReddit = input("What subreddit would you like")
r = praw.Reddit(user_agent='my_cool_application')
submissions = r.get_subreddit(subReddit).get_hot(limit=5)
pp([str(x) for x in submissions])