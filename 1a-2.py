import botometer

# Replace these with your own API keys
rapidapi_key = "123456"
twitter_app_auth = {
    "consumer_key": "123456",
    "consumer_secret": "123456",
    "access_token": "123456",
    "access_token_secret": "123456",
}

# Initialize botometer client
bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)

# Define the username of the user you want to check
username = "123456"

# Check the user's account
result = bom.check_account(username)

# Print the bot score
print("Bot Score: {}".format(result["scores"]["english"]))

# Print whether the user is a bot or not
if result["scores"]["english"] > 0.5:
  print("This user is likely a bot.")
else:
  print("This user is likely not a bot.")