import google.cloud
import google.cloud.language

# Replace with API key
api_key = "123456"

# Initialize Google NLP client
client = google.cloud.language.LanguageServiceClient(credentials=api_key)

# Define text to analyze
text = """
The natural world is full of beauty and wonder, and it's up to us to protect it. Unfortunately, human actions are often harmful to the environment, and it's important that we work to minimize our impact. We can do this by reducing our consumption, using renewable energy sources, and supporting organizations that work to preserve natural habitats. Together, we can make a difference and ensure that the natural world is preserved for future generations.
"""

# Analyze sentiment of text
document = google.cloud.language.types.Document(content=text, type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(document=document).document_sentiment

# Print results
print("Sentiment Score: {}".format(sentiment.score))
print("Sentiment Magnitude: {}".format(sentiment.magnitude))