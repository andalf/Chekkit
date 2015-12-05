# pip install pprintpp and pip install pp-ez
import pp

import connect_to_reddit

reddit = connect_to_reddit.connect()

#lets user choose subreddit
subReddit = input("What Subreddit would you like to use?")

# get 5 most recent from the subReddit 'opensource'
submissions = reddit.get_subreddit(subReddit).get_hot(limit=5)

# print out the output
pp([str(x) for x in submissions])