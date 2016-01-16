# pip install pprintpp and pip install pp-ez
import pp

import connect_to_reddit


reddit = connect_to_reddit.connect('Chekkit')

#lets user choose subreddit
sub_reddit = connect_to_reddit.which_subreddit()

# get 5 most recent from the subReddit 'opensource'
submissions = reddit.get_subreddit(sub_reddit).get_hot(limit=connect_to_reddit.change_limitnumber())

user_keywords = connect_to_reddit.key_words()

for article in submissions:
    lower_selftext = article.selftext.lower()
    if any(string in lower_selftext for string in user_keywords):
        print('Id: ' + article.id + "\n")
        print('Title: ' + article.title + "\n")
        print('Text: ' + article.selftext + "\n\n")

