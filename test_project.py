import project

def test_get_tweets():
    assert len(project.get_tweets("harvard")) == 100

def test_tweet_sentiment():
    assert project.tweet_sentiment("I love you") == "positive"

def test_perform_sentiments():
    assert project.perform_sentiments(["I love you"]) == {"positive": 1, "negative": 0, "neutral": 0}