# pip install praw
import praw


def connect(user_agent):
    # connect to Reddit as script specified user agent
    return praw.Reddit(user_agent=user_agent)
