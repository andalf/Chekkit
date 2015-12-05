# pip install praw
import praw


def connect(user_agent):
    # connect to Reddit as script specified user agent
    return praw.Reddit(user_agent=user_agent)


def which_subreddit():
    # lets user choose subreddit
    sub_reddit = input("What Subreddit would you like to use?")

    sub_reddit = sub_reddit.lower()

    return sub_reddit

def change_limitnumber():
    #lets user choose the amount shown
    limit_number = input("How many would you like to see?")
    limit_number = int(limit_number)

    return limit_number

