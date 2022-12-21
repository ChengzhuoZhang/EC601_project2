import tweepy
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Set up the Google Cloud client and authenticate using the service account key file
client = language.LanguageServiceClient.from_service_account_json('service_account.json')

# Set up the Twitter API client and authenticate using the API keys and access tokens
auth = tweepy.OAuth1UserHandler("123456", "123456", "123456", "123456")
api = tweepy.API(auth)

# Define the username of the user whose tweets you want to analyze
username = "123456"

# Search for the user's tweets
tweets = api.search_tweets(q=username, count=100)

# Analyze the sentiment of each tweet
for tweet in tweets:
  text = tweet.text

  # Create a document object
  document = types.Document(
      content=text,
      type=enums.Document.Type.PLAIN_TEXT
  )

  # Analyze the sentiment of the text
  sentiment = client.analyze_sentiment(document).document_sentiment

  # Print the sentiment score and magnitude
  print('Tweet: {}'.format(text))
  print('Sentiment score: {}'.format(sentiment.score))
  print('Sentiment magnitude: {}'.format(sentiment.magnitude))