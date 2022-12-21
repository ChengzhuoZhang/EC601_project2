# EC 601 - Project 2

## **Phase 1(a):   Twitter APIs**

### 1a-1: Exercise twitter APIs.

The code imports the tweepy library and defines a set of API keys and secrets that are required to authenticate with the Twitter API. It then creates an **`OAuth1UserHandler`** object and an **`API`** object. The code then defines the username of the user whose tweets you want to retrieve. You can replace it with the actual username of the user.

The code then calls the **`user_timeline`** method of the **`API`** object, passing in the username and the number of tweets to retrieve as arguments. This method sends a request to the Twitter API to retrieve the specified number of tweets from the user's timeline, and the response from the API includes a list of **`tweet`** objects, each representing a single tweet.

Finally, the code loops through the list of **`tweet`** objects and prints the text of each tweet.

### 1a-2: Botometer

This code imports the botometer library and defines a set of API keys that are required to use the library. It then creates a **`Botometer`** object and passes in the API keys as arguments.

The code then defines the username of the user you want to check. You can replace "twitter_username" with the actual username of the user.

The code then calls the **`check_account`** method of the **`Botometer`** object, passing in the username as an argument. This method sends a request to the botometer API to analyze the user's account, and the response from the API includes a **`result`** object that contains information about the user's bot score.

The code then prints the bot score and determines whether the user is a bot or not based on the bot score. If the bot score is greater than 0.5, the user is considered likely to be a bot. Otherwise, the user is considered likely to be not a bot.

When you run this code, it will send a request to the Botometer API to analyze the specified Twitter user and print the resulting bot score and a message indicating whether the user is likely a bot or not.

## **Phase 1(b):   Google NLP**

### 1b: Sentiment Analysis Using Google NLP

In order to use twitter API to analyze the sentiment of a given text, this is what I have done:

1. Sign up the Google Cloud account and enable the Natural Language API.
2. Set up authentication, create private key.
3. Install the Google Cloud Python client library and authenticate using the service account key file.
4. Use the **`analyze_sentiment`** method of the Natural Language API client to analyze the sentiment of the text.

The code 1b will print the sentiment score and magnitude of the text. The sentiment score is a value between -1 and 1, with negative values indicating a negative sentiment and positive values indicating a positive sentiment. The magnitude is a value that indicates the strength of the sentiment, with higher values indicating a stronger sentiment.

## **Phase 2:  Build your own social media analyzer**

### MVP

A social media analyzer that can output the sentiment of a given user’s tweets or a tweets about a given topic.

### User Stories

I, as a traveller, wants to know whether the reviews of a place from the local people. 

I, as a product manager, wants to about the real evaluation from customers who has purchased the product. 

I, as a politician, wants to know my approval rating in social media.  

### 2: Modular Design

The code is basic an integration of 1a-1 and 1b. When you run this code, it will search for the user's tweets using the Twitter API and analyze the sentiment of each tweet using the Google Cloud Natural Language API. It will then print the sentiment score and magnitude for each tweet.