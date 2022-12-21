import tweepy

# Replace these with API keys and secrets
consumer_key = "123456"
consumer_secret = "123456"
access_key = "123456"
access_secret = "123456"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_key, access_secret)
api = tweepy.API(auth)

# Define the username of the user whose tweets you want to retrieve
username = "123456"

# Retrieve the user's tweets
tweets = api.user_timeline(screen_name=username, count=200)

# Print the text of each tweet
for tweet in tweets:
  print(tweet.text)