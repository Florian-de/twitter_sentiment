# Twitter sentiment 
    #### Description: The sentiment on Twitter of an specific theme can be relevant in a lot of ways. It can be used for stock trading, political decisions, marketing, and more. In my project you can get the percentage of positive, negative and neutral tweets on a theme of your choice. It will get the recent 100 tweets on that topic from the twitter api and than evaluate them, using textblob. Be aware that most tweets will be neutral, so the percentages of positive and negative tweets are typically not that big. The get_tweets() function returns a list with the texts of the 100 most recent tweets of the choosen topic.
     The tweet_sentiment() function evaluates the sentiment of a tweet. The perform_sentiments() function counts how many tweets of a given array of tweet texts are positive, negative or neutral and returns it in form of a dict. The main() function first asks the user for a theme to do the researcn on. After that it performs the get_tweets() function. The next step is performing the perform_sentiments() function on the returned tweet texts. After that it counts the amount of tweet texts and calculates the percentages for positive, negative and neutral tweets. At the end it prints the percentages. The test_get_tweets() function checks if the get_tweets() returns 100 tweet texts as requested, if not, the test will fail. The test_tweet_sentiment() function checks if the sentiment check works. If the tweet_sentiment() function does not return positive with "I love you" as an input, the test will fail. The test_perform_sentiments() function checks if the perform_sentiments() function works. Note: You need your own twitter keys to use the project. You can get them over the Twitter dev website, you need to create a new app to get them. If your account isnt yet a dev account you need to follow the steps to register as one.