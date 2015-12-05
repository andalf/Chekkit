# pip install praw
import praw


def connect():
    # connect to Reddit as Chekkit
    return praw.Reddit(user_agent='chekkit')
