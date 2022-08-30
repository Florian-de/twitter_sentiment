import tweepy
import sys
from textblob import TextBlob

"""twitter API keys"""
BEARER_TOKEN = "" # add your own

def main():
    theme = input("Theme of sentiment research: ")
    tweets = get_tweets(theme)
    sentiments = perform_sentiments(tweets)
    count = sentiments["negative"] + sentiments["positive"] + sentiments["neutral"]
    p_positive = round(float(sentiments["positive"])/float(count)*100, 2)
    p_negative = round(float(sentiments["negative"])/float(count)*100, 2)
    p_neutral = round(float(sentiments["neutral"])/float(count)*100, 2)
    print(f"Positive tweets: {p_positive}%\n Negative tweets: {p_negative}%\n Neutral tweets: {p_neutral}%")

"""getting the tweets from twitter"""
def get_tweets(theme):
    try:
        client = tweepy.Client(bearer_token=BEARER_TOKEN)
    except:
        sys.exit("check your twitter keys")
    request = client.search_recent_tweets(query=theme, max_results=100)

    tweets = [tweet.text for tweet in request.data]
    return tweets

"""check if tweet if negativ/positiv/neutral"""
def tweet_sentiment(tweet):
    tweet_blob = TextBlob(tweet)
    sentiment = tweet_blob.sentiment.polarity
    if sentiment > 0.1:
        return "positive"
    elif sentiment < -0.1:
        return "negative"
    else:
        return "neutral"

"""counts the sentiments of the tweets"""
def perform_sentiments(tweets):
    sentiments = {"positive": 0, "negative": 0, "neutral": 0}
    for tweet in tweets:
        sentiments[tweet_sentiment(tweet)] += 1
    return sentiments

if __name__ == "__main__":
    main()