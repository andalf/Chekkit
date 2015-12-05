# pip install pprintpp and pip install pp-ez
import pp

import connect_to_reddit

reddit = connect_to_reddit.connect('Chekkit')

#lets user choose subreddit
subReddit = connect_to_reddit.which_subreddit()

# get 5 most recent from the subReddit 'opensource'
submissions = reddit.get_subreddit(subReddit).get_hot(limit=5)

# print out the output
pp([str(x) for x in submissions])